from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestScenarios:
    def testcase1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.cnn.com")
        driver.fullscreen_window()
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/header/div/div[1]/div/div[2]/nav/ul/li[9]/a").click()
        driver.get_screenshot_as_png("screensh")
        time.sleep(20)
        driver.quit

    def testcase2():
        driver = webdriver.Chrome()
        driver.get("https://www.scaledagileframework.com/system-team/")
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div/nav/div/div[1]/ul/li[6]/a").click()
        print (driver.get_screenshot_as_file("screenshottogo4.png"))
        time.sleep(20)
        driver.quit


    def testcase3():
        driver = webdriver.Chrome()
        driver.get("https://www.espn.com")
        driver.find_element(By.XPATH, "//span[@class='link-text'][contains(text(),'Watch')").click
        driver.get_screenshot_as_file("screenshottogo3.png"

ff = TestScenarios
ff.testcase1()
ff.testcase2()
ff.testcase3()