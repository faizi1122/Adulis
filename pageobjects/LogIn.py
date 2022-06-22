from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

from utils.general import *
import time


class LogIn(BASEPAGE):
    username = ""
    locator_dictionary = {
        "email": (By.ID, 'id_username'),
        "password1": (By.ID, 'id_password'),
        "signInBtn": (By.XPATH, '//button[@type= "submit"]'),
        "otp": (By.ID, 'id_otp'),
        "verifyOtpBtn": (By.XPATH, '//button[@type= "submit"]'),
        "profileBtn": (By.XPATH, '//*[@id="profileImg"]/img'),
        "stripeBtn": (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div/div/div[2]/a'),
        "typeEntityBtn": (By.XPATH, '//*[@id="connect-light"]/div/div/main/div[2]/div/div[2]/form/span/div['
                                    '1]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div['
                                    '2]/div[2]/span/label/span'),
        "phone": (By.ID, 'phone_number'),
        "stripeEmail": (By.ID, 'email'),
        "testPhoneNumberBtn": (By.XPATH, '//*[@id="connect-light"]/div/div/main/div[2]/div/div[2]/form/span/div['
                                         '1]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/span/span['
                                         '2]/button'),

        "continueBtn": (By.XPATH, '//button[@type= "submit"]'),
        "testOTP": (By.XPATH, '//*[@id="connect-light"]/div/div/main/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div['
                              '1]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/button'),
        # test otp button should be there

        "companyName": (By.ID, 'company[name]'),
        "businessName": (By.ID, 'business_profile[name]'),
        "businessURL": (By.ID, 'business_profile[url]'),
        "stripePageHeading": (By.CLASS_NAME, 'db-ConsumerUITitle')
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
        self.browser.get(base_url + "/signin/")
        # print(self.browser.title)
        if self.browser.title == self.constants["sign_in_page_title"]:
            return True
        else:
            return False

    def click_on(self, element):
        self.click_element(
            self.find_element(self.locator_dictionary[self.constants[element]])
        )

    def sign_in(self):

        # self.send_text_to_element(self.find_element(self.locator_dictionary["email"]), "yoyo")
        # self.find_element(self.locator_dictionary["email"]).clear()
        self.send_text_to_element(self.find_element(self.locator_dictionary["email"]), get_setting("CREDS", "username"))
        self.send_text_to_element(self.find_element(self.locator_dictionary["password1"]),
                                  get_setting("CREDS", "password"))
        # self.find_element(self.locator_dictionary["email"]).clear()
        self.click_element(self.find_element(self.locator_dictionary["signInBtn"]))

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

        # self.send_text_to_element(self.find_element(self.locator_dictionary["city"]), "NY")
        # self.click_element(self.find_element(self.locator_dictionary["stateBtn"]))
        # self.send_text_to_element(self.find_element(self.locator_dictionary["phone"]), "3184754597")
        # self.send_text_to_element(self.find_element(self.locator_dictionary["first_name"]), "test_first_name")
        # self.send_text_to_element(self.find_element(self.locator_dictionary["last_name"]), "test_last_name")
        # self.send_text_to_element(self.find_element(self.locator_dictionary["companyName"]), "Adulis")
        self.click_element(self.find_element(self.locator_dictionary["profileBtn"]))
        self.browser.get("https://adulis.com/profile/")
        self.click_element(self.find_element(self.locator_dictionary["stripeBtn"]))
        self.click_element(self.find_element(self.locator_dictionary["testPhoneNumberBtn"]))

        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.locator_dictionary["stripePageHeading"]))

        self.click_element(self.find_element(self.locator_dictionary["continueBtn"]))
        time.sleep(15)
        # self.find_element(self.locator_dictionary["stripeBtn"]).send_keys(Keys.CONTROL + "a")
        # self.find_element(self.locator_dictionary["stripeBtn"]).send_keys(Keys.BACK_SPACE)
        # self.browser.find_element_by_id('email').clear()
        self.find_element(self.locator_dictionary["stripeEmail"])
        #
        self.find_element(self.locator_dictionary["stripeEmail"]).clear()
        self.send_text_to_element(self.find_element(self.locator_dictionary["stripeEmail"]),
                                  get_setting("CREDS", "username"))

        # password = self.find_element(self.locator_dictionary["stripeBtn"]).send_keys(Keys.CONTROL + "a")
        # password.clear()
        # password.send_keys(password)
        # password.send_keys(Keys.RETURN)
        # password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        # or
        # time.sleep(1)
        # for i in range(len(password)):
        #     password.send_keys(Keys.BACKSPACE)

        # self.send_text_to_element(e, get_setting("CREDS", "username"))

        # self.send_text_to_element(self.find_element(self.locator_dictionary["stripeEmail"]), "abs")

        # self.find_element(self.locator_dictionary["stripeEmail"]).sendKeys(Keys.CONTROL + "a", Keys.DELETE)

        time.sleep(30)
        self.click_element(self.find_element(self.locator_dictionary["continueBtn"]))
        self.click_element(self.find_element(self.locator_dictionary["testOTP"]))

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
