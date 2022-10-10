from screens.base_screen import BaseScreen


class MainScreen(BaseScreen):

    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "PremiumPopupCloseButton": "//android.widget.Button[@resource-id='com.lamoda.lite:id/closeButton']",
            "NavigationBarMainButtonSelected": "//android.widget.FrameLayout[@resource-id='com.lamoda.lite:id/action_home'"
                                               "and @selected='true']",
            "SearchField": "//*[@resource-id='com.lamoda.lite:id/searchView']"
        })
        self.required_elements.append(self.elements.get("NavigationBarMainButtonSelected"))
        self.required_elements.append(self.elements.get("SearchField"))

    def close_premium_notification(self):
        while not self.element_is_displayed(self.elements.get("NavigationBarMainButtonSelected"), timeout=2):
            self.context.driver.back()
