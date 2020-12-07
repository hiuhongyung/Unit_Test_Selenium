import unittest
from selenium import webdriver
import page

PATH = "/Users/hiuhongyung/chromedriver"


class PythonOrgSearchTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")

    """
    def test_example(self):
        print("Test")
        assert True  # see if the condition on right side is true
        # tell whether the test case pass/fail
    """

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()  # run all the unit test we have defined
