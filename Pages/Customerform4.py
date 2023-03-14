import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Common.Commonitem import Commonitem


class Customerform(Commonitem):
    global parent_window

    DOB_element = (By.XPATH,"//input[@class='css-1qsbc7n']")
    gender_element = (By.XPATH,"//span[text()='Female']")
    residentialstatus_element = (By.XPATH,"//select[@name='value.living_arrangements.value.occupancy_status.value']")
    employmentstatus_element = (By.XPATH,"//select[@name='value.employment_details.value[0].value.employment_status.value']")
    grossincome_element = (By.XPATH,"//select[@name='value.financial_details.value.gross_income.value']")
    dependent_element = (By.XPATH,"//select[@name='value.living_arrangements.value.number_of_dependants.value']")
    entermanually_element = (By.XPATH,"//span[text()='Enter manually']")
    buidingnumber_element = (By.NAME,"building_number")
    street_element = (By.XPATH,"//input[@name='street']")
    town_element = (By.XPATH,"//input[@name='town']")
    postcode_element = (By.XPATH,"//input[@name='postcode']")
    monthataddress_element = (By.XPATH,"//select[@name='months_at_address']")
    checkbox_element = (By.XPATH,"//div[@class='css-1us5qiv']")
    completepurchase_element = (By.XPATH,"//button[@data-testid='stepper-button-next']")


    def __init__(self, driver):
            self.driver = driver

    def select_open_opplication_button(self):
        self.explictiwaitbyxpathforclickable("//a[@class='css-ppqv9l']")
        open_application = self.driver.find_element(by=By.XPATH, value="//a[@class='css-ppqv9l']")
        self.parent_window=self.driver.current_window_handle
        open_application.click()

    def switch_window_to_customer_form_window(self):

        ALL_window = self.driver.window_handles
        print(ALL_window)
        for child in ALL_window:
            if child != self.parent_window:
                self.driver.switch_to.window(child)  # switch in to particular window
                # self.driver.maximize_window()
                print(child)
                time.sleep(2)
                elementpreset = self.driver.find_elements(by=By.XPATH,
                                                          value="//input[@class='css-1qsbc7n']")  # eleent identification in the window
                elementpresent_count = len(elementpreset)
                print(elementpresent_count)
                if elementpresent_count > 0:
                    # WebDriverWait(self.driver, 10).until(
                    # EC.visibility_of_element_located(self.driver.find_element_by_xpath("//input[@class='css-1qsbc7n']")))

                    break


    def enter_valid_date_of_birth(self,Dateofbirth):
        time.sleep(2)
        DOB = self.driver.find_element(*Customerform.DOB_element)
        DOB.send_keys(Dateofbirth)

    def select_gender(self):
            gender = self.driver.find_element(*Customerform.gender_element)
            gender.click()

    def select_residential_status_value(self,residential):

            residentialstatus = self.driver.find_element(*Customerform.residentialstatus_element)
            residentialstatusobj = Select(residentialstatus)
            residentialstatusobj.select_by_value(residential)

    def select_employment_status_value_from_dropdown(self,employment):

            employmentstatus = self.driver.find_element(*Customerform.employmentstatus_element)
            employmentstatusobj = Select(employmentstatus)
            employmentstatusobj.select_by_value(employment)

    def select_Gross_annual_income_value_from_dropdown(self,grossincome):
        print(grossincome)
        Grossannual = self.driver.find_element(*Customerform.grossincome_element)
        Grossannualobj = Select(Grossannual)
        Grossannualobj.select_by_value(str(grossincome))

    def select_number_of_dependents_from_dropdown(self,dependent):
            Numberofdep = self.driver.find_element(*Customerform.dependent_element)
            Numberofdepobj = Select(Numberofdep)
            Numberofdepobj.select_by_value(str(dependent))

    def click_on_enter_manually_for_current_address(self):
            Entermanually = self.driver.find_element(*Customerform.entermanually_element)
            Entermanually.click()

    def enter_building_number(self,buildingno):

            Buidingnumber = self.driver.find_element(*Customerform.buidingnumber_element)
            Buidingnumber.send_keys(buildingno)

    def enter_street_name(self,streetname):
            street = self.driver.find_element(*Customerform.street_element)
            street.send_keys(streetname)

    def enter_town_name(self,townname):
            town = self.driver.find_element(*Customerform.town_element)
            town.send_keys(townname)

    def enter_postcode(self,postalcode):
            postcode = self.driver.find_element(*Customerform.postcode_element)
            postcode.send_keys(postalcode)

    def select_month_at_address(self,monthataddress):
            Month_at_address = self.driver.find_element(*Customerform.monthataddress_element)
            Month_at_addressobj = Select(Month_at_address)
            Month_at_addressobj.select_by_value(str(monthataddress))

    def select_confirm_checkbox(self):
         checkbox = self.driver.find_element(*Customerform.checkbox_element)
         checkbox.click()

    def click_on_complete_purchase_button(self):
         completepurchase = self.driver.find_element(*Customerform.completepurchase_element)
         completepurchase.click()
         time.sleep(5)



