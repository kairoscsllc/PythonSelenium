from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testing123:
    def testcase():
        driver = webdriver.Chrome()
        driver.get("https://www.cnn.com")
        driver.get_screenshot_as_file("CNNscreen6.png")
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/header/div/div[1]/div/div[2]/nav/ul/li[9]/a").click()
        time.sleep(10)
        driver.get_screenshot_as_file("CNNScreenChrome.png")
        driver.close()

    def testcase2():
        driver = webdriver.Firefox()
        driver.get("https://www.nfl.com")
        driver.find_element(By.XPATH, "/html/body/div[4]/header/div/nav[1]/ul/li[1]/a/span").click()
        time.sleep(10)
        driver.get_screenshot_as_file("NFLsSreenFirefox.png")
        driver.quit()


    def testcase3():
        driver = webdriver.Safari()
        driver.get("https://www.fox.com")
        driver.fullscreen_window()
        time.sleep(10)
        driver.get_screenshot_as_file("FOXScreenSafari.png")
        driver.quit()


Testing123.testcase()
Testing123.testcase2()
Testing123.testcase3()
