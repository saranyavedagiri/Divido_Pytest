import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from testdata.Dividotestdata import dividotestdata
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def launch(request,browser, web=None):
    if browser == "chrome":
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
    elif browser == "firefox":
       driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=web)
    elif browser == "edge":
         driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=web)
    driver.get("https://merchant.staging.duologi.net/login?redirect=/61f17a3e-d676-466f-aa3b-5465c6194dd7/applications/new")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()

#Keyword

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--url")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

"""

@pytest.fixture(scope="class")
def url(request):
    return request.config.getoption("--url")

"""

@pytest.fixture(params=dividotestdata.logintestdata)
def logindata(request):
    return request.param

@pytest.fixture(params=dividotestdata.credential_excel_dic)
def createapplication_testdata(request):
    return request.param
