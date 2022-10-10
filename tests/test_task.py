from helpers.swipe_helper import from_bottom_to_top


class TestTask:

    def test_search_results_sorting(self, context):
        advantages_screen = context.screen_manager.get_screen("AdvantagesScreen")
        advantages_screen.wait_for_screen_loaded().close()
        main_screen = context.screen_manager.get_screen("MainScreen")
        main_screen.close_premium_notification()
        main_screen.wait_for_screen_loaded()
        main_screen.click_element(main_screen.elements.get("SearchField"))
        search_screen = context.screen_manager.get_screen("SearchScreen")
        search_screen.wait_for_screen_loaded()
        search_screen.search("Gucci")
        results_before_sorting = search_screen.get_search_results()
        search_screen.sort_results_by_price_descending()
        results_after_sorting = search_screen.get_search_results()
        search_screen.results_should_not_be_equal(results_before_sorting, results_after_sorting)
        search_screen.results_should_be_sorted_by_price_descending(results_after_sorting)

    def test_swipe_search_results(self, context):
        search_screen = context.screen_manager.get_screen("SearchScreen")
        results_before_swipe = search_screen.get_search_results()
        search_screen.swipe(from_bottom_to_top, times=3)
        results_after_swipe = search_screen.get_search_results()
        search_screen.results_should_not_be_equal(results_before_swipe, results_after_swipe)
