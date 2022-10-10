from helpers.screen_manager import ScreenManager
from config import capabilities, default_appium_executor
from appium import webdriver


class Context:
    def __init__(self):
        self.driver = webdriver.Remote(command_executor=default_appium_executor, desired_capabilities=capabilities)
        self.screen_manager = ScreenManager(self)
