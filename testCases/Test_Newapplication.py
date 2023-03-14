import pyautogui as pyautogui
import pytest

from Pages.Createapplication3 import Createnewapplication
from Pages.Customerform4 import Customerform
from Pages.Dashboard2 import Dashboard
from Pages.Loginpage1 import Loginpage
from Utlilties.ExcelRead import Excel_Read
from testdata.Dividotestdata import dividotestdata


@pytest.mark.usefixture("launch")
class Test_newapplication():
    #calling excelread for row and column
    #Variable=excelread.py(classname ).function name
     Createapplication_maxrow = Excel_Read.retrunmaxrow(dividotestdata.filepath,dividotestdata.sheet_name)
     Createapplication_maxcolumn = Excel_Read.retrunmaxcolumn(dividotestdata.filepath, dividotestdata.sheet_name)



     def test_createacceptapplication(self,launch,logindata,createapplication_testdata):

        #Login page
         login_page=Loginpage(self.driver)
         print(logindata)
         print(logindata[1])
         login_page.username(logindata[0])
         login_page.password(logindata[1])
         login_page.login()
        #Dashboard page
         Dashboard_page=Dashboard(self.driver)
         Dashboard_page.clickonnewapplication()
        #Create newapplication page

         print(self.Createapplication_maxrow)
         for eachvalue in range(1,self.Createapplication_maxrow + 1 ):
             Createnewapplication_page=Createnewapplication(self.driver)
             Createnewapplication_page.select_channel(createapplication_testdata["actualChannelName"+str(eachvalue)])
             Createnewapplication_page.add_products(createapplication_testdata["Productdata"+str(eachvalue)],createapplication_testdata["quantityitem"+str(eachvalue)],createapplication_testdata["productprice"+str(eachvalue)])
             #Createnewapplication_page.addproduct_button()
             Createnewapplication_page.select_finance()
             Createnewapplication_page.deposit_field(createapplication_testdata["depositamount"+str(eachvalue)])
             Createnewapplication_page.firstname_field(createapplication_testdata["Firstnamedata"+str(eachvalue)])
             Createnewapplication_page.lastname_field(createapplication_testdata["Surnamedata"+str(eachvalue)])

             Createnewapplication_page.email_field(createapplication_testdata["emailid"+str(eachvalue)])
             Createnewapplication_page.phone_field(createapplication_testdata["Phoneno"+str(eachvalue)])
             Createnewapplication_page.deposit_collection()
             Createnewapplication_page.create_application_button()
             Customerform_page = Customerform(self.driver)
             Customerform_page.select_open_opplication_button()
             Customerform_page.switch_window_to_customer_form_window()
             Customerform_page.enter_valid_date_of_birth(createapplication_testdata["Dateofbirth"+str(eachvalue)])
             Customerform_page.select_gender()
             Customerform_page.select_residential_status_value(createapplication_testdata["residential"+str(eachvalue)])
             Customerform_page.select_employment_status_value_from_dropdown(createapplication_testdata["employment"+str(eachvalue)])
             Customerform_page.select_Gross_annual_income_value_from_dropdown(createapplication_testdata["grossincome"+str(eachvalue)])
             Customerform_page.select_number_of_dependents_from_dropdown(createapplication_testdata["dependent"+str(eachvalue)])
             Customerform_page.click_on_enter_manually_for_current_address()
             Customerform_page.enter_building_number(createapplication_testdata["building_no"+str(eachvalue)])
             Customerform_page.enter_street_name(createapplication_testdata["streetname"+str(eachvalue)])
             Customerform_page.enter_town_name(createapplication_testdata["townname"+str(eachvalue)])
             Customerform_page.enter_postcode(createapplication_testdata["Postcode"+str(eachvalue)])
             Customerform_page.select_month_at_address(createapplication_testdata["Yearataddress"+str(eachvalue)])
             Customerform_page.select_confirm_checkbox()
             Customerform_page.click_on_complete_purchase_button()







     """
         #select the new application button
         page2=createnewapplication()
         page2.Applicationpage()
         page2.Newapplicationpage()
         page2.addproduct()
         page2.finance()
         page2.customerinformation()
         page2.depositcollection()
     """







