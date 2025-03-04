from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os

# screenshot folder new
SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshot')
# screenshot folder new

class login_admin_page:

    textbox_username    = "//input[@id='user-name']"
    textbox_password    = "//input[@id='password']"
    
    input_button        = (By.XPATH, "//input[@id='login-button']")
    
    input_menu_btn      = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    input_logout        = (By.XPATH ,"//a[@id='logout_sidebar_link']")
    # input_logout        = (By.ID , "logout_sidebar_link")
    verify_success      = (By.XPATH, "//span[@class='title']")
        
    def __init__(self,driver):
        self.driver = driver
        
    def take_screenshot(self, name):
        # ambil screenshot
        screenshot_name = f"screenshot_{name}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
        # Membuat folder jika tidak ditemukan
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        self.driver.save_screenshot(screenshot_path
        )
        # Verifikasi screenshot di simpan
        assert os.path.exists(screenshot_path), f"Screenshot not saved at {screenshot_path}"
    
    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)
        
    def btn_login(self):
        self.driver.find_element(*self.input_button).click()
        
    def verify_login_success(self):
        self.driver.find_element(*self.verify_success).text
        
    def btn_logout(self):
        self.driver.find_element(*self.input_menu_btn).click()
        self.driver.find_element(*self.input_logout).click()
        # pass
