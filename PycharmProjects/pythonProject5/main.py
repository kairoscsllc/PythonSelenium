from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testing123:
    def testcase():
        driver = webdriver.Chrome()
        driver.get("https://www.cnn.com")
        driver.get_screenshot_as_file("CNNScreenChrome1.png")
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/header/div/div[1]/div/div[2]/nav/ul/li[9]/a").click()
        time.sleep(20)
        driver.get_screenshot_as_file("CNNScreenChrome2.png")
        driver.close()

    def testcase2():
        driver = webdriver.Firefox()
        driver.get("https://www.nfl.com")
        driver.find_element(By.XPATH, "/html/body/div[4]/header/div/nav[1]/ul/li[1]/a/span").click()
        time.sleep(10)
        driver.get_screenshot_as_file("NFLScreenFirefox1.png")
        driver.quit()

    def testcase3():
        driver = webdriver.Safari()
        driver.get("https://www.fox.com")
        driver.fullscreen_window()
        time.sleep(10)
        driver.get_screenshot_as_file("FOXScreenSafari1.png")
        driver.quit()

    def testcase4():
        driver = webdriver.Chrome()
        driver.get("https://www.kairoscs.com/training")
        driver.get_screenshot_as_file("CKairsChrome1.png")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/section[8]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/a/span").click()
        time.sleep(10)
        driver.find_element(By.ID, "yourNameId").send_keys("Niyitest")
        driver.find_element(By.ID, "emailId").send_keys("email.comtest")
        driver.get_screenshot_as_file("CNNScreenChrome2.png")
        driver.close()


Testing123.testcase()
Testing123.testcase2()
Testing123.testcase3()
Testing123.testcase4()

