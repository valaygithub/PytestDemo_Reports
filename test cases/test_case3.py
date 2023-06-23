import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_Pytest:

    @pytest.mark.group1
    def test_Orange_HRM_007(self):
        driver = webdriver.Chrome()

        # 2 opening url
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        time.sleep(5)
        # 3 enter username
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")

        # 4 enter password

        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")

        # 5 click to login button

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # 6 click on menu button

        driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()

        # 7 click on logout button

        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    @pytest.mark.group1
    def test_Credence_kart_008(self):
        driver = webdriver.Chrome()

        driver.get("https://automation.credence.in/shop")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Credence class")

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("credence144@credence.com")

        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("credence@1234")

        driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys("credence@1234")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(4)
        # if driver.title == 'CredKart':
        #     print("Registration completed")
        # else:
        #     print("registration failed")

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration completed")
        except NoSuchElementException:
            print("registration failed")
