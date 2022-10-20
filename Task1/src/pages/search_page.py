from seleniumpagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class SearchPage(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        driver.maximize_window()
        sleep(3)
        self.wait = WebDriverWait(driver, wait)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'cookiescript_accept'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='covid-notification']//a"))).click()
        

        #driver.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})

    locators = {
        "caption" : (By.XPATH, "//*[@class='search-name']//input[@name='sf_TextFilter']"),
        "caption_menu": (By.XPATH, "(//*[@class='search-name']//div[@class='tt-suggestion'])[1]"),
        "eventplace_dropdown": (By.XPATH, "//*[@id='search-location']//button"),
        "eventplace" : (By.XPATH, "//*[@id='search-location']//ul//a[text() = 'Artūro Areimos teatras (Ateities g. 10)']"),
        "from_date" : (By.XPATH, "//*[@class='search-time']//input[@name='sf_DateFrom']"),
        "to_date" : (By.XPATH, "//*[@class='search-time']//input[@name='sf_DateTo']"),
        "search" : (By.XPATH, "//*[@id='advSearchForm']//button[@type='submit']"),
        "buy" : (By.XPATH, "(//*[@id='eventsContainter']//div[@class='row-article row']//button[text() = 'Buy'])[1]")
    }

    def enter_caption(self):
        #self.caption.set_text("THE HAMLETMACHINE")
        by, locator = self.locators.get('caption')
        self.send_keys(by, locator, "THE HAMLETMACHINE")
        #self.caption_menu.click()
        by, locator = self.locators.get('caption_menu')
        self.click(by, locator)
        self.take_screenshot("enter_caption.png")

    def select_event_place(self):
        by, locator = self.locators.get('eventplace_dropdown')
        self.click(by, locator)
        by, locator = self.locators.get('eventplace')
        self.click (by, locator)
        self.take_screenshot("select_event_place.png")

    def choose_from_date(self):
        by, locator = self.locators.get('from_date')
        self.send_keys(by, locator, "2022-11-01")
        self.take_screenshot("choose_from_date.png")

    def choose_to_date(self):
        by, locator = self.locators.get('to_date')
        self.send_keys(by, locator, "2022-11-12")
        self.take_screenshot("choose_to_date.png")

    def click_search(self):
        by, locator = self.locators.get('search')
        self.click(by, locator)
        self.take_screenshot("click_search.png")

    def click_buy(self):
        by, locator = self.locators.get('buy')
        self.click(by, locator)
        self.take_screenshot("click_buy.png")
    
    # helper functions
    def click(self, by, locator):
        print(by, locator)
        self.wait.until(EC.element_to_be_clickable((by, locator))).click()

    def send_keys(self, by, locator, text):
        print(by, locator)
        self.wait.until(EC.element_to_be_clickable((by, locator))).send_keys(text)
    
    def take_screenshot(self, label):
        path = "./Task1/screenshots/"
        self.driver.get_screenshot_as_file(path + label)