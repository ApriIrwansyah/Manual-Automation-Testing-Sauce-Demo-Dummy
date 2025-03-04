from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from time import sleep

SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshot')

class CheckoutPage:
    
    def __init__(self,driver):
        self.driver = driver
        self.firstname = (By.XPATH, "//input[@id='first-name']")
        self.lastname = (By.XPATH, "//input[@id='last-name']")
        self.zip = (By.XPATH, "//input[@id='postal-code']")
        
        self.con = (By.XPATH, "//input[@id='continue']")
        
        self.verify_info = (By.XPATH, "//div[normalize-space()='Payment Information:']")
        
        self.finish = (By.XPATH, "//button[@id='finish']")
        
        self.verify_success = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")
        
        self.backHome = (By.XPATH, "//button[@id='back-to-products']")
        
    def input_checkout(self, firstname, lastname, zip):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        sleep(2)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        sleep(2)
        self.driver.find_element(*self.zip).send_keys(zip)
        sleep(2)
        self.driver.find_element(*self.con).click()
    
    def take_screenshot(self, name):
        screenshot_name = f"screenshot_{name}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
        # Membuat Folder jika tidak ditemukan
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        # Verifikasi screenshot disimpan
        assert os.path.exists(screenshot_path), f"Screenshot tidak disimpan pada {screenshot_path}"
    def verify_information(self):
        self.driver.find_element(*self.verify_info).text
        
    def click_finish(self):
        self.driver.find_element(*self.finish).click()
        
    def verify_successfull(self):
        self.driver.find_element(*self.verify_success).text

    def click_backHome(self):
        self.driver.find_element(*self.backHome).click()
    
