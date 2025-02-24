# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSUBMITAPP():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sUBMITAPP(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("wulan")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("12345678")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.find_element(By.ID, "navbardrop").click()
    self.driver.find_element(By.LINK_TEXT, "Account Details").click()
    self.driver.find_element(By.CSS_SELECTOR, ".close").click()
    self.driver.find_element(By.LINK_TEXT, "Application").click()
    self.driver.find_element(By.LINK_TEXT, "Residence").click()
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    self.driver.find_element(By.LINK_TEXT, "Residence").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ibg-bg").click()
    self.driver.find_element(By.LINK_TEXT, "Submit Application").click()
    self.driver.find_element(By.NAME, "requiredMonth").click()
    self.driver.find_element(By.NAME, "requiredMonth").send_keys("December")
    self.driver.find_element(By.NAME, "requiredYear").send_keys("2021")
    self.driver.find_element(By.CSS_SELECTOR, ".form-inline").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-sm").click()
    self.driver.find_element(By.ID, "navbardrop").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
