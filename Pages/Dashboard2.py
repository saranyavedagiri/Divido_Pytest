import time
from selenium.webdriver.common.by import By
from Common.Commonitem import Commonitem


class Dashboard(Commonitem):
    merchantdropdown = (By.XPATH,"//button[@data-testid='merchant-dropdown']")
    #merchantelement = (By.XPATH,"//*[text()='Aainbolt']//parent::button")
    merchantelement = (By.XPATH, "//*[text()='Aainbolt']//parent::div[@role='button']")
    applicationelement = (By.XPATH,"//*[text()='Applications']")
    Newapplicationelement = (By.XPATH,"//button[@data-testid='applications-new-btn']")

    def __init__(self,driver):
        self.driver = driver

    def clickonnewapplication(self):
        #calling function from one class to another class
        time.sleep(2)
        #self.explictiwaitbyxpathforvisibilityofElement("//button[@data-testid='merchant-dropdown']")
        textname = self.driver.find_element(by=By.XPATH, value="//button[@data-testid='merchant-dropdown']//span").text
        if textname == 'Aainbolt':
         pass
        else:
         self.driver.find_element(*Dashboard.merchantdropdown).click()
         merchant = self.driver.find_element(*Dashboard.merchantelement)
         merchant.click()

        #self.explictiwaitbyxpathforvisibilityofElement("//*[text()='Aainbolt']//parent::div[@role='button']")
       # self.explictiwaitbyxpathforvisibilityofElement(
            #"//div[@class='MerchantPicker__MerchantOption-sc-lgbpvl-0 hBBsXz css-mc1fo4']")
        """
        merchant = self.driver.find_element(*Dashboard.merchantelement)
        if merchant.is_enabled():
           merchant.click()
           """
        #self.explictiwaitbyxpathforclickable("//*[text()='Applications']")
        time.sleep(2)
        self.driver.find_element(*Dashboard.applicationelement).click()
        #self.explictiwaitbyxpathforclickable("//button[@data-testid='applications-new-btn']")
        self.driver.find_element(*Dashboard.Newapplicationelement).click()
