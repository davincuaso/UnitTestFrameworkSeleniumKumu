from locators import MainPageLocators
from element import BasePageElement

class LivestreamNavbarTextElement(BasePageElement):
# The id name of the search bar is q
    locator = "nav-link"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    # Descriptor

    def isTitleMatches(self):
        return "Kumu - Your Pinoy Livestreaming App" in self.driver.title
    
    def clickLivestreams(self):
        element = self.driver.find_element(*MainPageLocators.LIVESTREAMS)
        element.click

