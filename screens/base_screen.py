import time
from helpers.swipe_helper import get_swipe_coordinates
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BaseScreen:

    def __init__(self, context):
        self.context = context
        self.elements = {}
        self.required_elements = []

    def wait_for_element_is_visible(self, locator, by=By.XPATH, timeout=15):
        WebDriverWait(self.context.driver, timeout).until(ec.visibility_of_element_located((by, locator)))

    def wait_for_screen_loaded(self, timeout=15):
        for locator in self.required_elements:
            self.wait_for_element_is_visible(locator, timeout=timeout)
        return self

    def element_is_displayed(self, locator, by=By.XPATH, timeout=0):
        try:
            self.wait_for_element_is_visible(locator, by=by, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def click_element(self, locator, by=By.XPATH):
        self.context.driver.find_element(value=locator, by=by).click()

    def send_keys_to_element(self, locator, text, by=By.XPATH):
        self.context.driver.find_element(value=locator, by=by).send_keys(text)

    def swipe(self, direction, times=1, duration=500):
        coordinates = get_swipe_coordinates(direction, self.context.driver)
        for i in range(times):
            self.context.driver.swipe(coordinates['start_x'], coordinates['start_y'],
                                      coordinates['end_x'], coordinates['end_y'], duration)
            time.sleep(1)
