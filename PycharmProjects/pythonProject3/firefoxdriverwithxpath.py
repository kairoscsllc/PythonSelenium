from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testing123:
    def testcase():
        driver = webdriver.Chrome()
        driver.get("https://www.scaledagileframework.com/system-team/")
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[2]/div/nav/div/div[1]/ul/li[6]/a").click()
        time.sleep(10)



Testing123.testcase()





#class RuffTests():
    #def test1():
        #driver =webdriver.Chrome()
        #driver.get("https://www.cnn.com")
        #driver.fullscreen_window()
        #driver.quit

    #def test2():
        #driver =webdriver.Firefox()
        #driver.get("https://www.msn.com")
        #driver.fullscreen_window()
        #driver.refresh()
        #driver.quit()



#ff1 = Testing123
#ff.test1()
#ff1.testcase()




3 +6

