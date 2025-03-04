import os
import sys

sys.path.append("../") # mengambil file di dalam folder dan folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) # file di dalam folder


# pytest -s -x -v test_cases/test_shopping_cart.py
# pytest -s -x -v test_cases/test_shopping_cart.py --test-browser chrome ## 7
# pytest -s -x -v test_cases/test_shopping_cart.py --test-browser chrome -n 3 ## 8
# pytest -s -v -x test_cases/test_shopping_cart.py --html=reports/test_admin_login2.html --self-contained-html -n 4 ## perintah untuk laopran html
# pytest -s -v test_cases/test_shopping_cart.py --junitxml=reports/test_shopping_cart.pyl ## perintah untuk laporan xml
# pytest -s -m -v "sanity" --html=test-cases/test_shopping_cart.py --test-browser chrome --self-contained-html -n 4 

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base_pages.login_admin_pages import login_admin_page
from base_pages.shopping_cart_pages import shoppingCart
from utilities.custom_logger import LogMaker

from time import sleep

class Test_VerifikasiShoppingCart:
    
    pageURL                 = "https://www.saucedemo.com" # 4
    username_std            = "standard_user" #  4
    password                = "secret_sauce" # 4
    # Logs
    logger      = LogMaker.log_generated()
    
    def test_verifikasi_valid(self, setup:WebDriver):
        self.logger.info("**********Test 01 - Shopping Cart**********") # 6
        self.logger.info("**********Verifikasi halaman Shopping Cart **********") # 6
        self.driver = setup # 4
        self.driver.get(self.pageURL) # 4
        self.driver.implicitly_wait(10) # 4
        self.driver.maximize_window() # 4
        
        self.admin = login_admin_page(self.driver)
        self.cart = shoppingCart(self.driver)
        
        self.admin.enter_username(self.username_std)
        sleep(2)
        self.admin.enter_password(self.password) 
        self.admin.btn_login() 
        
        self.cart.click_itemLabel()    
        self.cart.click_btn_addToCart()
        self.cart.click_linkCart()
        self.cart.click_btnContinue()
        self.cart.click_btn_addToCart02()
        self.cart.click_btn_addToCart03()
        self.cart.click_linkCart()
        self.cart.click_btnCheckout()
        
        act_verifikasi_checkout = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        exp_verifikasi_checkout = "Checkout: Your Information"
        if act_verifikasi_checkout == exp_verifikasi_checkout:
            assert True
            print(f"Pesan Berhasil : {act_verifikasi_checkout}")
            self.logger.info("**********Verifikasi Halaman Checkout berhasil**********")
            self.cart.take_screenshot("test_verifikasi_shoppingCart")
            sleep(1)
            self.admin.btn_logout()
        else:
            self.logger.info("**********Verifikasi Halaman Checkout tidak berhasil**********")
            self.driver.close()
            assert False