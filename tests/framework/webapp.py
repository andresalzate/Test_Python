from selenium import webdriver
from urllib.parse import urljoin


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def load_website(self, website):
        self.driver.get(website)

    def verify_component_exists(self, component):
        assert component in self.driver.page_source, \
            "Component {} not found on page".format(component)


webapp = WebApp.get_instance()
