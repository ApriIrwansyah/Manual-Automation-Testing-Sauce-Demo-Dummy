import pytest # 5
from selenium import webdriver # 5

# 7 - pada tahap ini kita akan modifikasi untuk bisa memanggil berbagai browser
# def pytest_addoption(parser):
#     parser.addoption("--test-browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")
    
# def browser(request):
#     return request.config.getoption("--test-browser")
# 7

@pytest.fixture(scope="function") # 5
def setup(): # 5
    driver = webdriver.Chrome() # 5
    # driver.get("https://www.saucedemo.com")
    # driver.maximize_window()
    # yield driver
    return driver # 5
    # driver.quit()

# 7 @