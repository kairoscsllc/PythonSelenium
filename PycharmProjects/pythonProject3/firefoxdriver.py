from selenium import webdriver

class RuffTests():
    #def test1():
        #driver =webdriver.Chrome()
        #driver.get("https://www.cnn.com")
        #driver.fullscreen_window()
        #driver.quit

    def test2():
        driver =webdriver.Firefox()
        driver.get("https://www.cnn..com")
        driver.fullscreen_window()
        driver.refresh()
        driver.quit()



ff = RuffTests
#ff.test1()
ff.test2()


