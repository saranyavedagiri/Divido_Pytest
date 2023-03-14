from selenium.webdriver.common.by import By


class Loginpage():

    usernameelement = (By.XPATH, "//input[@data-testid='login-email']")
    passwordelement = (By.XPATH, "//input[@data-testid='login-password']")
    loginelement = (By.XPATH, "//span[@class='css-5ihqdp']")

    def __init__(self,driver):
        self.driver = driver

    """To verify login page
    def verifysucessfullogin(self,logindata):
        self.driver.implicitly_wait(10)
        print(logindata)
        self.driver.find_element(*Loginpage.username).send_keys(logindata[0])

        self.driver.find_element(*Loginpage.password).send_keys(logindata[1])
        self.driver.find_element(*Loginpage.login).click()
     """
    #(reuse the variable to verify the successful login or not)
    def username(self,Usrname):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*Loginpage.usernameelement).send_keys(Usrname)
    def password(self,pwd):
        self.driver.find_element(*Loginpage.passwordelement).send_keys(pwd)
    def login(self):
        self.driver.find_element(*Loginpage.loginelement).click()




