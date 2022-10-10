from math import floor

from_left_to_right = "LEFT TO RIGHT"
from_right_to_left = "RIGHT TO LEFT"
from_top_to_bottom = "TOP TO BOTTOM"
from_bottom_to_top = "BOTTOM TO TOP"


def get_swipe_coordinates(direction, driver):
    screen_size = driver.get_window_size()
    if from_left_to_right == direction:
        start_x = floor(screen_size["width"] * 0.1)
        start_y = floor(screen_size["height"] * 0.5)
        end_x = floor(screen_size["width"] * 0.9)
        end_y = floor(screen_size["height"] * 0.5)
    elif from_right_to_left == direction:
        start_x = floor(screen_size["width"] * 0.9)
        start_y = floor(screen_size["height"] * 0.5)
        end_x = floor(screen_size["width"] * 0.1)
        end_y = floor(screen_size["height"] * 0.5)
    elif from_top_to_bottom == direction:
        start_x = floor(screen_size["width"] * 0.5)
        start_y = floor(screen_size["height"] * 0.1)
        end_x = floor(screen_size["width"] * 0.5)
        end_y = floor(screen_size["height"] * 0.9)
    elif from_bottom_to_top == direction:
        start_x = floor(screen_size["width"] * 0.5)
        start_y = floor(screen_size["height"] * 0.9)
        end_x = floor(screen_size["width"] * 0.5)
        end_y = floor(screen_size["height"] * 0.1)
    else:
        raise Exception("Unknown direction for swipe")
    return {"start_x": start_x, "start_y": start_y, "end_x": end_x, "end_y": end_y}
