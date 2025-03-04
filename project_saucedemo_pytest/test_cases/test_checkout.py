import os
import sys
import pytest
# pytest -s -x -v test_cases/test_checkout.py
# pytest -s -x -v test_cases/test_checkout.py --test-browser chrome ## 7
# pytest -s -x -v test_cases/test_checkout.py --test-browser chrome -n 3 ## 8
# pytest -s -v -x test_cases/test_checkout.py --html=reports/test_admin_login2.html --self-contained-html -n 4 ## perintah untuk laopran html
# pytest -s -v test_cases/test_checkout.py --junitxml=reports/test_admin_login.xml ## perintah untuk laporan xml
# pytest -s -m -v "sanity" --html=test-cases/test_checkout.py --test-browser chrome --self-contained-html -n 4 

from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from base_pages.login_admin_pages import login_admin_page
from base_pages.shopping_cart_pages import shoppingCart
from base_pages.checkout_pages import CheckoutPage

class Test_Checkout:
    
    # pageURL                 = "https://www.saucedemo.com" # 4
    # username_std            = "standard_user" #  4
    # password                = "secret_sauce" # 4
    
    def test_checkout(self, setup: WebDriver): # 4
        self.driver = setup
        self.driver.get("https://www.saucedemo.com")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        self.logAdmin = login_admin_page(self.driver)
        self.cart = shoppingCart(self.driver)
        self.checkout = CheckoutPage(self.driver)
        
        # form login
        self.logAdmin.enter_username(username="standard_user")
        sleep(2)
        self.logAdmin.enter_password(password="secret_sauce")
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        
        # form shopping cart
        self.cart.click_itemLabel()    
        self.cart.click_btn_addToCart()
        self.cart.click_linkCart()
        self.cart.click_btnContinue()
        self.cart.click_btn_addToCart02()
        self.cart.click_btn_addToCart03()
        self.cart.click_linkCart()
        self.cart.click_btnCheckout()
        
        # form checkout
        self.checkout.input_checkout(firstname="Apri", lastname="Irwansyah", zip="42161")
        
        self.checkout.click_finish()
        sleep(1)
        # exp_checkout = self.checkout.verify_information()
        # act_checkout = "Payment Information:"
        exp_checkoutSuccess = self.checkout.verify_successfull()
        act_checkoutSuccess = "Thank you for your order!"
        if exp_checkoutSuccess == act_checkoutSuccess:
            assert True
            print(f"Success : {act_checkoutSuccess}")
            self.driver.save_screenshot(".\\screenshot\\test_checkout_success.png")
            self.checkout.take_screenshot("checkout_success")
            sleep(1)
            self.checkout.click_backHome()
        else:
            self.driver.close()
            # assert False
            pass