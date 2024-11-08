import cv2
import numpy as np
import pyautogui
import os
import random
import time
import webbrowser
from datetime import datetime
from PIL import ImageGrab


def open_url_and_wait_for_image(url, image_path, region, timeout=5):
    """
    Opens a URL and waits for a specific image to appear on the screen.

    Args:
        url (str): The URL to open.
        image_path (str): Path to the image file to detect.
        region (tuple): The region (left, top, width, height) to search for the image.
        timeout (int): Maximum time (in seconds) to wait for the image. Default is 30 seconds.

    Returns:
        bool: True if the image is found within the timeout, False otherwise.
    """
    webbrowser.open(url)
    print("Waiting for page to load...")

    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            is_image_detected = detect_image_in_region(image_path, region)
            if is_image_detected is not None:
                print("Image found!")
                return True
            print("Looking for image...")
            time.sleep(1)  # Adjust sleep time for faster detection
        except pyautogui.ImageNotFoundException:
            print("Image not found!")

    print("Timeout reached. Image not found.")
    return False


def detect_image_in_region(image_path, region, confidence=0.9):
    """
       Detects an image on the screen within a specified region.

       Args:
           image_path (str): Path to the image file to detect.
           region (tuple): The region (left, top, width, height) to search for the image.
           confidence (float): Confidence level for image matching (0 to 1). Default is 0.9.

       Returns:
           Coordinates of the center of the detected image, or None if not found.
       """
    try:
        image_location = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
        return image_location
    except Exception as e:
        print(f"Error detecting image: {e}")
        return None


def click_found_image(image_location, num_clicks=0):
    """
    Clicks on a found image location on the screen.

    Args:
        image_location (Optional[Tuple[int, int]]): The (x, y) coordinates of the image location.
        num_clicks (int): Number of times to click. Default is 1.

    Returns:
        None
    """
    if image_location is None:
        print("No image location provided, skipping clicks.")
        return

    for i in range(num_clicks):
        # Move the mouse to the location with a random duration
        pyautogui.moveTo(image_location.x, image_location.y, duration=random.uniform(0.3, 1.0))
        time.sleep(0.2)

        # Click the location
        pyautogui.click()
        print(f"Clicked on the found image (click {i + 1}/{num_clicks})")

        # Pause to simulate human behavior
        time.sleep(random.uniform(2, 5))


def debugging_capture_region(region, save_dir="./debug_logs"):
    """
    Captures a specified region of the screen and saves it as an image.

    Args:
        region (Tuple[int, int, int, int]): The region to capture (left, top, width, height).
        save_dir (str): Directory where the captured image will be saved. Default is './debug_logs'.

    Returns:
        Optional[str]: The file path of the saved image, or None if an error occurred.
    """
    # Validate the region
    if not isinstance(region, tuple) or len(region) != 4:
        print("Invalid region specified.")
        return None

    try:
        # Ensure the save directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_dir, f"captured_region_{timestamp}.png")

        left, top, width, height = region

        # Capture the region using PIL
        screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))

        # Convert the screenshot to a NumPy array
        screenshot_np = np.array(screenshot)

        # Convert from RGB (Pillow) to BGR (OpenCV)
        screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Save the image using OpenCV
        cv2.imwrite(file_path, screenshot_cv)

        print(f"Captured region saved to: {file_path}")
        return file_path

    except Exception as e:
        print(f"Error capturing region: {e}")
        return None
