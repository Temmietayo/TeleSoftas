from multiprocessing.connection import wait
import unittest
from selenium import webdriver
import json

from src.pages.search_page import SearchPage


class TiketaTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(r'C:\Users\DELL\Downloads\TeleSoftas\Task1\test\config.json') as config_file: 
            self.config = json.load(config_file)
        if self.config.get('browser') == "chrome":
            self.driver = webdriver.Chrome(r"C:\Users\DELL\Downloads\TeleSoftas\Task1\drivers\chromedriver")

    def test_detailed_search_functionality(self):
        url = self.config.get("url")
        wait = self.config.get("wait_time")
        self.driver.get("{0}/search".format(url))
        
        searchpage = SearchPage(self.driver, wait)

        searchpage.enter_caption()
        searchpage.select_event_place()
        searchpage.choose_from_date()
        searchpage.choose_to_date()
        searchpage.click_search()
        searchpage.click_buy()

    #def tearDown(self) -> None:
      #  self.driver.close()


if __name__ == '__main__':
    unittest.main()