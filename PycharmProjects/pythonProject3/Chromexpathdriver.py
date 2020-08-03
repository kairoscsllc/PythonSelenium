from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RuffTests():
    def test1():
        driver = webdriver.Chrome()
        driver.get("https://www.cnn.com")
        driver.fullscreen_window()
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/header/div/div[1]/div/div[2]/nav/ul/li[9]/a").click()
        time.sleep(20)
        driver.quit

    def test2():
        driver = webdriver.Chrome()
        driver.get("https://www.scaledagileframework.com/system-team/")
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div/nav/div/div[1]/ul/li[6]/a").click()
        time.sleep(20)
        driver.quit


ff = RuffTests
ff.test1()
ff.test2()

# https://selenium-python.readthedocs.io/locating-elements.html


# 3 +6 hf
