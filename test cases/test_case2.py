import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Pytest:

    @pytest.mark.regrassion
    def test_sum_005(self):
        a = 7
        b = 4
        sum = a + b
        print(sum)
        if sum == 11:
            assert True
        else:
            assert False

    @pytest.mark.regrassion
    def test_credence_006(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
       #print(l)
        Contact_num_list = []
        for r in range(1, l + 1):
            Contact_Number = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a[" + str(r) + "]").text
            #print(Contact_Number)
            Contact_num_list.append(Contact_Number)
        #print(Contact_num_list)
        if "+91 9091929355" in Contact_num_list:
            print(Contact_num_list.index("+91 9091929355"))
            assert True
        else:
            assert False



