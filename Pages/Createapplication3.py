import time
import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Createnewapplication():


    channel_element = (By.XPATH,"//div[@data-testid='channel' and @aria-expanded='false']")
    channellist_element = (By.XPATH,"//*[@class='css-ygyxn3']//child::div[@role='option']")
    productname_element = (By.XPATH, "//input[@data-testid='product-name']")
    quantity_element = (By.XPATH,"//input[@data-testid='product-quantity']")
    price_element = (By.XPATH,"//input[@data-testid='product-price']")
    addproduct_element = (By.XPATH,"//span[text()='Add product']")
    finance_element = (By.XPATH,"//div[@data-finance-id='4ffa8550-ab66-4300-bd90-710628ea0790']")
    deposit_element = (By.XPATH,"//input[@data-testid='deposit-amount']")
    firstname_element = (By.XPATH,"//input[@data-testid='first-name']")
    lastname_element = (By.XPATH,"//input[@data-testid='last-name']")
    email_element = (By.XPATH,"//input[@data-testid='email']")
    phonenumber_element = (By.XPATH,"//input[@data-testid='phone']")
    collectdeposit_element = (By.XPATH,"//div[text()='Collect deposit during application journey']")
    createapplication_element = (By.XPATH,"//span[text()='Create application']")

    def __init__(self,driver):
        self.driver = driver

    def select_channel(self, actualChannelName):
        self.driver.implicitly_wait(10)
        channel = self.driver.find_element(*Createnewapplication.channel_element)
        channel.click()
        print("channel clicked")
        time.sleep(2)
        channellist = self.driver.find_elements(*Createnewapplication.channellist_element)
        channelisllen = len(channellist)
        print(channelisllen)
        for i in range(1, channelisllen + 1):
           channelName = self.driver.find_element(by=By.XPATH,
                                               value="//*[@class='css-ygyxn3']//child::div[@role='option'][" + str(
                                                   i) + "]//div").text
           print(channelName)
           if (channelName == actualChannelName):
            self.driver.find_element(by=By.XPATH,
                                     value="//*[@class='css-ygyxn3']//child::div[@role='option'][" + str(
                                         i) + "]").click()
            break
    def add_products(self,Productdata,quantityitem,productprice):
        #Enter product name
        productname = self.driver.find_element(*Createnewapplication.productname_element)
        productname.send_keys(Productdata)



        #Enter quanity
        quantity = self.driver.find_element(*Createnewapplication.quantity_element)
        quantitycheck = ActionChains(self.driver)
        quantitycheck.move_to_element(productname).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.DELETE).key_up(
        Keys.DELETE).perform()
        time.sleep(1)
        quantity.send_keys(quantityitem)


        #Enter product cost
        price = self.driver.find_element(*Createnewapplication.price_element)
        quantitycheck.move_to_element(price).click().key_down(Keys.BACK_SPACE).key_up(
        Keys.BACK_SPACE).perform()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        price.send_keys(productprice)
        time.sleep(1)
        #select the Add Product button(optional)
    def addproduct_button(self):
        Addproduct = self.driver.find_element(*Createnewapplication.addproduct_element)
        Addproduct.click()

    #Select finance
    def select_finance(self):
        self.driver.implicitly_wait(10)
        finance = self.driver.find_element(*Createnewapplication.finance_element)
        finance.click()

    def deposit_field(self,depositamount):
        deposit = self.driver.find_element(*Createnewapplication.deposit_element)
        quantitycheck = ActionChains(self.driver)
        quantitycheck.move_to_element(deposit).click().key_down(Keys.BACK_SPACE).key_up(
        Keys.BACK_SPACE).perform()
        deposit.send_keys(depositamount)

    #Customer information

    #Enter firstname
    def firstname_field(self,Firstnamedata):
        firstname = self.driver.find_element(*Createnewapplication.firstname_element)
        firstname.send_keys(Firstnamedata)

    #Enter lastname
    def lastname_field(self,Surnamedata):
        lastname = self.driver.find_element(*Createnewapplication.lastname_element)
        print(Surnamedata)
        lastname.send_keys(Surnamedata)


    def email_field(self,emailid):
        time.sleep(2)
        print(emailid)
        email = self.driver.find_element(*Createnewapplication.email_element)
        print("navigating email id" )
        email.send_keys(emailid)

    def phone_field(self,Phoneno):
        phone = self.driver.find_element(*Createnewapplication.phonenumber_element)
        phone.send_keys(Phoneno)

    def deposit_collection(self):
        self.driver.implicitly_wait(10)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH,"//div[text()='Collect deposit during application journey']"))
        paidin = self.driver.find_element(*Createnewapplication.collectdeposit_element)
        paidin.click()

    def create_application_button(self):
        createapplication = self.driver.find_element(*Createnewapplication.createapplication_element)
        createapplication.click()
