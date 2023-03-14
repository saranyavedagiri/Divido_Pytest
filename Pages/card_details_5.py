import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Carddetails():


  def Complete_your_purchase(self):


    # WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.driver.find_element(by=By.XPATH, value="//button[@data-testid='stripe-button']")))
    # print("executed")
    print(self.driver.current_window_handle)
    frame_to = self.driver.find_elements(by=By.TAG_NAME, value="iframe")  # mentioned elements
    frame_count = len(frame_to)
    print("framecount = " + str(frame_count))
    time.sleep(5)
    for sat in range(0, frame_count):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(sat))
        self.driver.switch_to.frame(sat)  # switch over in to frame
        # WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.driver.find_element(by=By.XPATH, value="//input[@name='cardnumber']")))
        self.driver.implicitly_wait(60)
        value = self.driver.find_elements(by=By.XPATH, value="//input[@name='cardnumber']")
        elementos = len(value)
        print("element  " + str(elementos))
        if elementos > 0:
            self.driver.find_element(by=By.XPATH, value="//input[@name='cardnumber']").send_keys("4242424242424242")
            break
        self.driver.switch_to.default_content()