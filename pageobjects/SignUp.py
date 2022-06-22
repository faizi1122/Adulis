from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

from utils.general import *
import time


class SignUp(BASEPAGE):
    username = ""
    locator_dictionary = {
        "email": (By.ID, 'id_email'),
        "agreeCheckbox": (By.ID, 'id_terms_accepted'),
        "joinNowBtn": (By.XPATH, '//button[@type= "submit"]'),

        "password1": (By.ID, 'id_password1'),
        "password2": (By.ID, 'id_password2'),
        "city": (By.ID, 'id_city'),
        "stateBtn": (By.XPATH, '//select[@name="state"]/option[@value="AL"]'),
        "phone": (By.ID, 'id_phone_number'),
        "first_name": (By.ID, 'id_first_name'),
        "last_name": (By.ID, 'id_last_name'),
        "companyName": (By.ID, 'id_company_name'),
        "signUpBtn": (By.XPATH, '//button[text() = "Sign Up"]'),

        "otp": (By.ID, 'id_otp'),
        "verifyOtpBtn": (By.XPATH, '//button[@type= "submit"]'),

        "homePageLogo": (By.XPATH, '//nav/a/img'),
        "troubleshootBtn": (By.ID, 'id_resend_email')
    }

    constants = {
        "sign_in_page_title": "Sign in | Adulis",
        "sign_up_page_title": "Join Us | Adulis",
        "account_page_title": "My Account"
    }
    urls = {
        "SignUp": '/join_us/',
        "SignIn": 'signin/',
        "Gucci": '/gucci-accessories-belts---blue-27504.html'
    }

    def go_to(self, link):
        base_url = get_setting("URL", "url")
        self.browser.get(base_url + self.urls[link])
        # print(self.browser.title)
        if self.browser.title == self.constants["sign_up_page_title"]:
            return True
        else:
            return False

    def click_on(self, element):
        self.click_element(
            self.find_element(self.locator_dictionary[self.constants[element]])
        )

    def sign_up(self):
        self.username = "qa+" + self.generate_uuid() + "@" + get_setting("MAILOSAUR", "server_domain")
        self.send_text_to_element(self.find_element(self.locator_dictionary["email"]), self.username)
        self.click_element(self.find_element(self.locator_dictionary["agreeCheckbox"]))
        self.click_element(self.find_element(self.locator_dictionary["joinNowBtn"]))

    def getEmailVerificationLink(self, email_sms):
        mailosaur = MailosaurClient(get_setting("MAILOSAUR", "api_key"))
        criteria = SearchCriteria()
        # criteria.sent_from = "account-update@adulis.com"
        print(email_sms)
        criteria.sent_from = get_setting("MAILOSAUR", email_sms)
        criteria.sent_to = self.username
        try:
            email = mailosaur.messages.get(get_setting("MAILOSAUR", "server_id"), criteria, timeout=60000)
        except:
            try:
                self.click_element(self.find_element(self.locator_dictionary["troubleshootBtn"]))
                email = mailosaur.messages.get(get_setting("MAILOSAUR", "server_id"), criteria, timeout=120000)
            except:
                assert False, "The verification email was not sent"

        first_link = email.html.links[0].href

        print(first_link)
        self.browser.get(first_link)

        # Deleting all messages in the end.
        mailosaur.messages.delete_all(get_setting("MAILOSAUR", "server_id"))

    def onboarding(self):
        self.send_text_to_element(self.find_element(self.locator_dictionary["password1"]), get_setting("CREDS", "password"))
        self.send_text_to_element(self.find_element(self.locator_dictionary["password2"]), get_setting("CREDS", "password"))
        self.send_text_to_element(self.find_element(self.locator_dictionary["city"]), "NY")
        self.click_element(self.find_element(self.locator_dictionary["stateBtn"]))
        self.send_text_to_element(self.find_element(self.locator_dictionary["phone"]), "3184754597")
        self.send_text_to_element(self.find_element(self.locator_dictionary["first_name"]), "test_first_name")
        self.send_text_to_element(self.find_element(self.locator_dictionary["last_name"]), "test_last_name")
        self.send_text_to_element(self.find_element(self.locator_dictionary["companyName"]), "Adulis")
        self.click_element(self.find_element(self.locator_dictionary["signUpBtn"]))

    def getSMSOtpCode(self, email_sms):
        mailosaur = MailosaurClient(get_setting("MAILOSAUR", "api_key"))
        criteria = SearchCriteria()
        # criteria.sent_from = "account-update@adulis.com"
        print(email_sms)
        criteria.sent_from = get_setting("MAILOSAUR", email_sms)
        criteria.sent_to = "13184754597"
        email = mailosaur.messages.get(get_setting("MAILOSAUR", "server_id"), criteria, timeout=120000)
        sms = email.text.body
        sms = sms.split()[0]
        print(sms)
        self.send_text_to_element(self.find_element(self.locator_dictionary["otp"]), sms)
        self.click_element(self.find_element(self.locator_dictionary["verifyOtpBtn"]))
        try:
            WebDriverWait(self.browser, self.WAIT).until(
                EC.presence_of_element_located(self.locator_dictionary["homePageLogo"]))
        except:
            print("Exception: The user is not navigated to Gamil Login screen.")

        # Deleting all messages in the end.
        mailosaur.messages.delete_all(get_setting("MAILOSAUR", "server_id"))