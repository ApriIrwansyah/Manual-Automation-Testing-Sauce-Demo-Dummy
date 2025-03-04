import sys
import os

from selenium.webdriver.chrome.webdriver import WebDriver
sys.path.append("../") # file di dalam folder - diluar folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) # file di dalam folder

import pytest
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_pages.login_admin_pages import login_admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import LogMaker


# pytest -s -x -v test_cases/test_admin_login.py
# pytest -s -x -v test_cases/test_admin_login.py --test-browser chrome ## 7
# pytest -s -x -v test_cases/test_admin_login.py --test-browser chrome -n 3 ## 8
# pytest -s -v -x test_cases/test_admin_login.py --html=reports/test_admin_login2.html --self-contained-html -n 4 ## perintah untuk laopran html
# pytest -s -v test_cases/test_admin_login.py --junitxml=reports/test_admin_login.xml ## perintah untuk laporan xml
# pytest -s -m -v "sanity" --html=test-cases/test_admin_login.py --test-browser chrome --self-contained-html -n 4 

class Test_Admin_Login: # 4
    
    pageURL                 = "https://www.saucedemo.com" # 4
    username_std            = "standard_user" #  4
    username_locked         = "locked_out_user" # 4 
    username_problem        = "problem_user" # 4
    username_performance    = "performance_glitch_user" # 4
    username_error          = "error_user" # 4
    username_visual         = "visual_user" # 4
    password                = "secret_sauce" # 4
    
    # untuk mengambil logs
    logger = LogMaker.log_generated()
    
    def test_title_verifikasi(self, setup: WebDriver): # 4
        # pass
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login **********") # 6
        self.driver = setup # 4
        self.driver.get(self.pageURL) # 4
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # //div[@class='login_logo']
        act_title = self.driver.find_element(By.XPATH, "//div[@class='login_logo']").text
        exp_title = "Swag Labs" # 4
        if act_title == exp_title: # 4
            assert True # 4
            self.logger.info("**********Verifikasi Pesan test_title berhasil**********") # 6
            self.driver.save_screenshot(".\\screenshot\\test_verifikasi_halaman login.png") # 4
            self.driver.close() # 4
        else:
            self.logger.info("**********Verifikasi Pesan test_title tidak berhasil**********") # 6
            self.driver.close() 
            assert False
        
    def test_verifikasi_loginStd(self, setup: WebDriver):
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login Standars**********") # 6
        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logAdmin = login_admin_page(self.driver)
        sleep(2)
        self.logAdmin.enter_username(self.username_std)
        sleep(2)
        self.logAdmin.enter_password(self.password)
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        act_login_Std = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        exp_login_Std = "Products"
        if act_login_Std == exp_login_Std:
            assert True
            print(f"Pesan Berhasil : {act_login_Std}")
            self.logger.info("**********Verifikasi Pesan test_valid_loginStandars berhasil**********") # 6
            # self.driver.save_screenshot(".\\screenshot\\test_success_loginError.png")
            self.logAdmin.take_screenshot("test_loginStd")
            self.logAdmin.btn_logout()
        else:
            self.logger.info("**********Verifikasi Pesan test_valid_loginStandars tidak berhasil**********") # 6
            self.driver.close()
            assert False
            # pass
    
    def test_verifikasi_loginLocked(self, setup: WebDriver):
        # pass
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login Locked**********") # 6
        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logAdmin = login_admin_page(self.driver)
        sleep(2)
        self.logAdmin.enter_username(self.username_locked)
        sleep(2)
        self.logAdmin.enter_password(self.password)
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        act_login_failed = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        exp_login_failed = "Epic sadface: Sorry, this user has been locked out."
        if act_login_failed == exp_login_failed:
            assert True
            print(f"Pesan Kesalahan : {act_login_failed}")
            # self.driver.save_screenshot(".\\screenshot\\test_success_loginLocked.png")
            self.logger.info("**********Verifikasi Pesan test_valid_loginStandars berhasil**********") # 6
            self.logAdmin.take_screenshot("test_loginLocked")
            self.driver.close()
        else:
            self.logger.info("**********Verifikasi Pesan test_valid_loginLocked tidak berhasil**********") # 6
            self.driver.close()
            assert False
            # pass
    
    def test_verifikasi_loginProblem(self, setup: WebDriver):
        # pass
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login Problem**********") # 6
        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logAdmin = login_admin_page(self.driver)
        sleep(2)
        self.logAdmin.enter_username(self.username_problem)
        sleep(2)
        self.logAdmin.enter_password(self.password)
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        act_login_problem = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        exp_login_problem = "Products"
        if act_login_problem == exp_login_problem:
            assert True
            print(f"Pesan Berhasil : {act_login_problem}")
            self.logger.info("**********Verifikasi Pesan test_valid_loginProblem berhasil**********") #6
            # self.driver.save_screenshot(".\\screenshot\\test_success_loginProblem.png")
            self.logAdmin.take_screenshot("test_loginProblem")
            self.logAdmin.btn_logout()
        else:
            self.logger.info("**********Verifikasi Pesan test_valid_loginProblem tidak berhasil**********") # 6
            self.driver.close()
            assert False
            # pass
    
    def test_verifikasi_loginPerformance(self, setup: WebDriver):
        # pass
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login Performance**********") # 6
        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logAdmin = login_admin_page(self.driver)
        sleep(2)
        self.logAdmin.enter_username(self.username_performance)
        sleep(2)
        self.logAdmin.enter_password(self.password)
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        act_login_problem = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        exp_login_problem = "Products"
        if act_login_problem == exp_login_problem:
            assert True
            print(f"Pesan Berhasil : {act_login_problem}")
            self.logger.info("**********Verifikasi Pesan test_valid_loginPerforemance berhasil**********") # 6
            # self.driver.save_screenshot(".\\screenshot\\test_success_loginPerformance.png")
            self.logAdmin.take_screenshot("test_loginPerformance")
            self.logAdmin.btn_logout()
        else:
            self.logger.info("**********Verifikasi Pesan test_valid_loginPerformace tidak berhasil**********") # 6
            self.driver.close()
            assert False
            # pass
            
    def test_verifikasi_loginError(self, setup: WebDriver):
       # pass
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login Error**********") # 6
        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logAdmin = login_admin_page(self.driver)
        sleep(2)
        self.logAdmin.enter_username(self.username_error)
        sleep(2)
        self.logAdmin.enter_password(self.password)
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        act_login_problem = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        exp_login_problem = "Products"
        if act_login_problem == exp_login_problem:
            assert True
            print(f"Pesan Berhasil : {act_login_problem}")
            # self.driver.save_screenshot(".\\screenshot\\test_success_loginError.png")
            self.logger.info("**********Verifikasi Pesan test_valid_loginError berhasil**********") # 
            self.logAdmin.take_screenshot("test_loginError")
            self.logAdmin.btn_logout()
        else:
            self.logger.info("**********Verifikasi Pesan test_valid_loginError tidak berhasil**********")
            self.driver.close()
            assert False
            # pass
        
    def test_verifikasi_loginVisual(self, setup: WebDriver):
        # pass
        self.logger.info("**********Test 01 - Admin Login**********") # 6
        self.logger.info("**********Verifikasi halaman login Visual**********") # 6
        self.driver = setup
        self.driver.get(self.pageURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logAdmin = login_admin_page(self.driver)
        sleep(2)
        self.logAdmin.enter_username(self.username_visual)
        sleep(2)
        self.logAdmin.enter_password(self.password)
        sleep(2)
        self.logAdmin.btn_login()
        sleep(2)
        act_login_problem = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        exp_login_problem = "Products"
        if act_login_problem == exp_login_problem:
            assert True
            print(f"Pesan Berhasil : {act_login_problem}")
            # self.driver.save_screenshot(".\\screenshot\\test_success_loginError.png")
            self.logger.info("**********Verifikasi Pesan test_valid_loginVisual berhasil**********") #
            self.logAdmin.take_screenshot("test_loginError")
            self.logAdmin.btn_logout()
        else:
            self.logger.info("**********Verifikasi Pesan test_valid_loginVisual tidak tidak berhasil**********") #
            self.driver.close()
            assert False
            pass