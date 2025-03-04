from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

# inisisiakan screenshot
SCREENSHOT_DIR = os.path.join(os.getcwd(), 'screenshot') 

class shoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.itemLabel = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
        self.btn_addToCart = (By.XPATH, "//button[@id='add-to-cart']")
        self.btn_addToCart02 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
        self.btn_addToCart03 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.linkCart = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.btnContinue = (By.XPATH, "//button[@id='continue-shopping']")
        self.btnCheckout = (By.XPATH, "//button[@id='checkout']")
        
    def take_screenshot(self, name):
        # take screenshot
        screenshot_name = f"screenshot_{name}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
        # membuat folder jika tidak ditemukan
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        # Verifikasi screenshot di simpan
        assert os.path.exists(screenshot_path), f"Screenshot not saved at {screenshot_path}"
    
    def click_itemLabel(self):
        # self.driver.find_element(*self.itemLabel).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.itemLabel)).click()
        
    def click_btn_addToCart(self):
        # self.driver.find_element(*self.btn_addToCart).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.btn_addToCart)).click()
        
    def click_btn_addToCart02(self):
        # self.driver.find_element(*self.btn_addToCart02).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.btn_addToCart02)).click()
    
    def click_btn_addToCart03(self):
        # self.driver.find_element(*self.btn_addToCart03).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.btn_addToCart03)).click()
    
    def click_linkCart(self):
        # self.driver.find_element(*self.linkCart).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.linkCart)).click()
        
    def click_btnContinue(self):
        # self.driver.find_element(*self.btnContinue).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.btnContinue)).click()
        
    def click_btnCheckout(self):
        # self.driver.find_element(*self.btnCheckout).click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.btnCheckout)).click()
        