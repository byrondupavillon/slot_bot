from PIL import ImageGrab
import cv2
import numpy as np


def capture_and_show_region(region):
    """
    Captures a screenshot of the specified region and displays it using OpenCV.

    Args:
        region (tuple): The region to capture (left, top, width, height).
    """
    left, top, width, height = region
    # Capture the region using PIL
    screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))

    # Convert the screenshot to a NumPy array
    screenshot_np = np.array(screenshot)

    # Convert RGB (Pillow) to BGR (OpenCV)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Display the image using OpenCV
    cv2.imshow("Captured Region", screenshot_cv)
    cv2.waitKey(0)  # Wait for any key to close
    cv2.destroyAllWindows()


# Example usage
# Define the region (left, top, width, height)
region = (781, 558, 357, 68)
capture_and_show_region(region)
