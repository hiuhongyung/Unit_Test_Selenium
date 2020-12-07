from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title #inherit from the BasePage 
    
    def click_go_button(self):
        element = self.driver.find_element(*MainMageLocators.GO_BUTTON) # * means unpacked (1,2) && ((1), (2))
        element.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found" not in self.driver.page_source