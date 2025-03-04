import os 
import sys
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

# pytest -s -x -v test_cases/test_sosial_media.py
# pytest -s -x -v test_cases/test_sosial_media.py --test-browser chrome ## 7
# pytest -s -x -v test_cases/test_sosial_media.py --test-browser chrome -n 3 ## 8
# pytest -s -v -x test_cases/test_sosial_media.py --html=reports/test_admin_login2.html --self-contained-html -n 4 ## perintah untuk laopran html
# pytest -s -v test_cases/test_sosial_media.py --junitxml=reports/test_admin_login.xml ## perintah untuk laporan xml
# pytest -s -m -v "sanity" --html=test-cases/test_sosial_media.py --test-browser chrome --self-contained-html -n 4 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from base_pages.login_admin_pages import login_admin_page
from base_pages.social_media_pages import SocialMedia
from time import sleep

class Test_SosialMedia:
    
    def test_sosialmedia(self, setup: WebDriver):
        try:
            self.driver = setup
            self.driver.get("https://www.saucedemo.com")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            
            self.logAdmin   = login_admin_page(self.driver)
            self.sosmed     = SocialMedia(self.driver)
            
            # form login
            self.logAdmin.enter_username(username="standard_user")
            sleep(1)
            self.logAdmin.enter_password(password="secret_sauce")
            sleep(2)
            self.logAdmin.btn_login()
            sleep(2)
            
            # form sosial media
            self.sosmed.click_sosialmedia()
            self.driver.save_screenshot(".\\screenshot\\test_checkout_success.png")
        except:
            self.driver.close()
            assert False