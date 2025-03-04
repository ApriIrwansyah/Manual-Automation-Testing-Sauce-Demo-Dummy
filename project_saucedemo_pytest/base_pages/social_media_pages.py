from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

class SocialMedia:
    
    def __init__(self,driver):
        self.driver     = driver
        
        self.twitter    = (By.XPATH, "//a[normalize-space()='Twitter']")
        self.facebook   = (By.XPATH, "//a[normalize-space()='Facebook']")
        self.linked     = (By.XPATH, "//a[normalize-space()='LinkedIn']")
        
        
    def click_sosialmedia(self):
        self.driver.find_element(*self.twitter).click()
        sleep(2)
        self.driver.find_element(*self.facebook).click()
        sleep(2)
        self.driver.find_element(*self.linked).click()
        