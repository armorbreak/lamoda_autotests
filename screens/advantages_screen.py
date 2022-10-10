from screens.base_screen import BaseScreen
from selenium.webdriver.common.by import By


class AdvantagesScreen(BaseScreen):

    def __init__(self, context):
        super().__init__(context)
        self.elements.update({
            "Advantages": "//android.view.ViewGroup[./*[@resource-id='com.lamoda.lite:id/fast_delivery_text'] "
                          "and ./*[@resource-id='com.lamoda.lite:id/delivery_with_tryon_text']"
                          "and ./*[@resource-id='com.lamoda.lite:id/all_goods_are_authentic_text']]",
            "AdvantagesOkButton": "com.lamoda.lite:id/advantages_ok"
        })
        self.required_elements.append(self.elements.get("Advantages"))

    def close(self):
        self.click_element(self.elements.get("AdvantagesOkButton"), by=By.ID)
