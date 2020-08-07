import unittest
from selenium import webdriver
import page

class KumuWeb(unittest.TestCase):
# setUp and tearDown will be called once for every testcase
    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("https://kumu.ph/site")
    
    def testPressLivestreamNavbar(self):
        mainPage = page.MainPage(self.driver)
        mainPage.clickLivestreams()


    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()
