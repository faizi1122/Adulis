import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.general import *
from .common.basepage import BASEPAGE


class Product(BASEPAGE):
    username = ""
    locator_dictionary = {

        "productBtn": (By.XPATH, '//*[@id="navbarSupportedContent"]/ul[1]/li[3]'),
        "addProduct": (By.CLASS_NAME, 'btn-warning'),
        "productTitle": (By.NAME, 'title'),
        "coffeeType": (By.XPATH, '//*[@id="id_coffee_type"]/option[2]'),
        "coffeeForm": (By.XPATH, '//*[@id="id_coffee_form"]/option[2]'),
        "coffeeOrigin": (By.XPATH, '//*[@id="id_coffee_origin"]/option[12]'),
        "wareHouseLocation": (By.XPATH, '//*[@id="id_warehouse_location"]/option[6]'),
        "processBtn": (By.XPATH, '//*[@id="id_processing"]/option[2]'),
        "coffeeGrade": (By.XPATH, '//*[@id="id_coffee_grade"]/option[4]'),
        "certificationSelection": (By.XPATH, '//*[@id="id_product_form"]/div[2]/div/div/div[8]/span/span[1]/span'),
        "certificate": (By.XPATH, '//*[@id="select2-id_certification-result-qqrg-FT"]'),
        "tags": (By.XPATH, '//*[@id="id_product_form"]/div[2]/div/div/div[10]/tags/span'),
        "continueBtn": (By.XPATH, '//*[@id="id_product_form"]/div[2]/div/div/div[13]/button'),
        "samplePrice": (By.NAME, 'sample_price'),
        "Price": (By.NAME, 'price'),
        "minQty": (By.NAME, 'minimum_order_qty'),
        "availableQty": (By.NAME, 'available_qty'),
        "nextBtn": (By.XPATH, '//*[@id="id_product_form"]/div[3]/div/div/div[7]/button'),
        "desc": (By.NAME, 'description'),
        "addFaq": (By.XPATH, '//*[@id="id_product_form"]/div[4]/div/div/div[2]/div[1]/div[2]/a'),
        "question": (By.NAME, 'question'),
        "answer": (By.NAME, 'answer'),
        "saveBtn": (By.XPATH, '//*[@id="exampleModal"]/div/div/div[2]/button[2]'),
        "contBtn": (By.XPATH, '//*[@id="id_product_form"]/div[4]/div/div/div[5]/button'),
        "browseImg": (By.XPATH, '(//input[@type="file"])[1]'),
        "submitBtn": (By.XPATH, '//button[@id="submit_btn"]')

    }

    def product_addition(self):
        self.click_element(self.find_element(self.locator_dictionary["productBtn"]))
        self.click_element(self.find_element(self.locator_dictionary["addProduct"]))
        self.send_text_to_element(self.find_element(self.locator_dictionary["productTitle"]), "Black Coffee Test")
        self.click_element(self.find_element(self.locator_dictionary["coffeeType"]))
        self.click_element(self.find_element(self.locator_dictionary["coffeeForm"]))
        self.click_element(self.find_element(self.locator_dictionary["coffeeOrigin"]))
        self.click_element(self.find_element(self.locator_dictionary["wareHouseLocation"]))
        self.click_element(self.find_element(self.locator_dictionary["processBtn"]))
        self.click_element(self.find_element(self.locator_dictionary["coffeeGrade"]))
        # self.send_text_to_element(self.find_element(self.locator_dictionary["certificationSelection"]), "Fair Trade")
        self.click_element(self.find_element(self.locator_dictionary["certificationSelection"]))
        self.find_element(self.locator_dictionary["certificationSelection"]).send_keys(Keys.ARROW_DOWN)
        self.find_element(self.locator_dictionary["certificationSelection"]).send_keys(Keys.ENTER)
        self.find_element(self.locator_dictionary["certificationSelection"]).send_keys(Keys.TAB)
        # self.click_element(self.find_element(self.locator_dictionary["tags"]))
        self.send_text_to_element(self.find_element(self.locator_dictionary["tags"]), "test1, test2, test3,")
        self.find_element(self.locator_dictionary["tags"]).send_keys(Keys.TAB)
        self.click_element(self.find_element(self.locator_dictionary["continueBtn"]))
        time.sleep(2)
        self.send_text_to_element(self.find_element(self.locator_dictionary["samplePrice"]), "23")
        self.send_text_to_element(self.find_element(self.locator_dictionary["Price"]), "50")
        self.send_text_to_element(self.find_element(self.locator_dictionary["minQty"]), "2")
        self.send_text_to_element(self.find_element(self.locator_dictionary["availableQty"]), "530")
        self.click_element(self.find_element(self.locator_dictionary["nextBtn"]))
        time.sleep(2)

        self.send_text_to_element(self.find_element(self.locator_dictionary["desc"]),
                                  "test is going on completion stage is just in few step.")
        self.click_element(self.find_element(self.locator_dictionary["addFaq"]))

        self.send_text_to_element(self.find_element(self.locator_dictionary["question"]),
                                  "test question?")
        self.send_text_to_element(self.find_element(self.locator_dictionary["answer"]),
                                  "test is going on completion stage just last step remaining.")
        self.click_element(self.find_element(self.locator_dictionary["saveBtn"]))
        self.click_element(self.find_element(self.locator_dictionary["contBtn"]))
        time.sleep(2)

        # # to identify element
        s = self.find_element(self.locator_dictionary["browseImg"])
        # file path specified with send_keys
        s.send_keys(os.path.join(os.getcwd(), 'monitor-1.png'))
        time.sleep(3)
        self.click_element(self.find_element(self.locator_dictionary["submitBtn"]))


