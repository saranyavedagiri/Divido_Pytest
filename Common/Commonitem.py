import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixture("launch")
class Commonitem():

      def explictiwaitbyxpathforvisibilityofElement(self, xpathAttribute):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpathAttribute)))

      def explictiwaitbyxpathforclickable(self, xpathAttribute):
          WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpathAttribute)))
