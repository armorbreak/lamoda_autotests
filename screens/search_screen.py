from screens import BaseScreen
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SearchScreen(BaseScreen):

    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "SearchField": "//android.widget.EditText[@resource-id='com.lamoda.lite:id/searchEditTextCurrent']"
                           " | //android.widget.TextView[@resource-id='com.lamoda.lite:id/searchTitle']",
            "SearchResultsContainer": "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.lamoda.lite:id/recyclerView']",
            "SingleResultContainer": "//android.view.ViewGroup[@resource-id='com.lamoda.lite:id/container']",
            "Tooltip": "//android.widget.TextView[@resource-id='com.lamoda.lite:id/tooltip_text']",
            "SingleResultPrice": "(//android.view.ViewGroup[@resource-id='com.lamoda.lite:id/container'])[%s]"
                                 "//android.widget.TextView[@resource-id='com.lamoda.lite:id/priceTextView']",
            "SingleResultName": "(//android.view.ViewGroup[@resource-id='com.lamoda.lite:id/container'])[%s]"
                                 "//android.widget.TextView[@resource-id='com.lamoda.lite:id/nameTextView']",
            "SortingButton": "//android.widget.LinearLayout[@resource-id='com.lamoda.lite:id/sortingsButton']",
            "SortingByPriceDescending": "//android.widget.ScrollView"
                                        "/android.view.View[./android.view.View[contains(@text, 'по убыванию цены')]]"
        })
        self.required_elements.append(self.elements.get("SearchField"))

    def search(self, text):
        self.send_keys_to_element(self.elements.get("SearchField"), text)
        self.context.driver.execute_script("mobile: performEditorAction", {"action": "search"})

    def get_search_results(self):
        self.close_tooltip()
        self.wait_for_element_is_visible(self.elements.get("SingleResultContainer"))
        results = self.context.driver.find_elements(By.XPATH, self.elements.get("SingleResultContainer"))
        prices = {}
        for i in range(1, len(results) + 1):
            try:
                price_str = self.context.driver.find_element(By.XPATH, self.elements.get("SingleResultPrice") % i).text
                price = "".join(filter(str.isdigit, price_str))
                name = self.context.driver.find_element(By.XPATH, self.elements.get("SingleResultName") % i).text
                prices[name] = price
            except NoSuchElementException:
                break
        return prices

    def close_tooltip(self):
        if self.element_is_displayed(self.elements.get("Tooltip"), timeout=3):
            self.context.driver.back()

    def sort_results_by_price_descending(self):
        self.context.driver.find_element(By.XPATH, self.elements.get("SortingButton")).click()
        self.wait_for_element_is_visible(self.elements.get("SortingByPriceDescending"))
        self.context.driver.find_element(By.XPATH, self.elements.get("SortingByPriceDescending")).click()

    def results_should_not_be_equal(self, first, second):
        if isinstance(first, dict):
            first = list(first.keys())
        if isinstance(second, dict):
            second = list(second.keys())
        assert first != second, "Results are equal"

    def results_should_be_sorted_by_price_descending(self, results):
        if isinstance(results, dict):
            results = list(results.values())
        for i in range(len(results) - 1):
            assert results[i] >= results[i + 1], "Results are not ordered by price descending"
