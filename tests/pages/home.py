from framework.webapp import webapp
from selenium.webdriver.common.keys import Keys

class Home():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Home()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.textbox_find = '//*[@title="Buscar"]'
        self.label_results = 'resultStats'

    def fill_find(self, value):
        textbox_find = self.driver.find_element_by_xpath(self.textbox_find)
        textbox_find.send_keys(value)
        textbox_find.send_keys(Keys.ENTER)

    def text_results(self):
        text_results = self.driver.find_element_by_id("resultStats")
        return text_results.text


home = Home.get_instance()
