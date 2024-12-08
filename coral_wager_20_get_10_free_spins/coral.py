import time
import random
from functions import open_url_and_wait_for_image, detect_image_in_region, click_found_image


def open_coral_and_check_logo():
    """Open the Coral site and check for the logo."""
    url = "https://promo.coral.co.uk/en/promo/p/smart-rewards"
    coral_logo_path = './coral_wager_20_get_10_free_spins/images/coral_logo.jpg'
    coral_logo_region = (8, 14, 129, 28)
    print("Opening Coral website...")
    if not open_url_and_wait_for_image(url, coral_logo_path, coral_logo_region):
        print("Failed to load the Coral website.")
        return False
    return True


def attempt_login():
    """Attempt to detect and click the login button."""
    login_image_path = './coral_wager_20_get_10_free_spins/images/login_btn.jpg'
    login_region = (1819, 6, 76, 43)
    print("Attempting to detect login button...")
    login_btn_detection = detect_image_in_region(login_image_path, login_region, timeout=5)
    if login_btn_detection:
        print("Found login button...")
        click_found_image(login_btn_detection, num_clicks=1)
        return True
    return False


def attempt_login_prompt_button():
    """Attempt to detect and click the login prompt button."""
    login_prompt_path = './coral_wager_20_get_10_free_spins/images/login_prompt_btn.jpg'
    login_prompt_region = (781, 558, 357, 68)
    print("Attempting to detect login prompt button...")
    login_prompt_btn_detection = detect_image_in_region(login_prompt_path, login_prompt_region, confidence=0.98, timeout=5)
    if login_prompt_btn_detection:
        print("Found login button...")
        click_found_image(login_prompt_btn_detection, num_clicks=1)
        return True
    return False


def check_for_deposit_button():
    """Check for the deposit button and navigate to a new site if found."""
    deposit_image_path = './coral_wager_20_get_10_free_spins/images/deposit_btn.jpg'
    deposit_region = (1679, 5, 100, 45)
    print("Checking for deposit button...")
    if detect_image_in_region(deposit_image_path, deposit_region, confidence=0.7, timeout=5):
        print("Deposit button found. Navigating to Slot...")
        return True
    return False


def open_coral_wager_and_check_spin_button():
    """Open the Coral wager site and check for spin button"""
    url = "https://www.coral.co.uk/en/games/launchng/playtechgoldentour"
    coral_logo_path = './coral_wager_20_get_10_free_spins/images/spin_btn.jpg'
    coral_logo_region = (1150, 824, 141, 60)
    print("Opening Coral Golden Tour Slot...")
    if not open_url_and_wait_for_image(url, coral_logo_path, coral_logo_region):
        print("Failed to load the Coral website.")
        return False
    return True

def check_correct_wager_amount():
    """Check to make sure that the correct bet amount is set."""
    wager_image_path = './coral_wager_20_get_10_free_spins/images/wager_amount.jpg'
    wager_region = (779, 972, 87, 30)
    print("Checking for correct wager amount...")
    if detect_image_in_region(wager_image_path, wager_region, confidence=0.7, timeout=5):
        print("Correct wager amount found. Starting spins...")
        return True
    return False

def run_coral_task():
    """Main function to run the Coral task."""
    # Step 1: Open Coral site and check for the logo
    if not open_coral_and_check_logo():
        return

    # Step 2: Attempt to log in or check for the deposit button
    time.sleep(random.uniform(2.0, 5.0))
    if attempt_login():
        time.sleep(random.uniform(2.0, 5.0))
        attempt_login_prompt_button()
        time.sleep(random.uniform(2.0, 5.0))
        check_for_deposit_button()
        time.sleep(random.uniform(2.0, 5.0))
        print("Successfully logged in.")
    elif check_for_deposit_button():
        print("Already logged in.")
    else:
        print("Neither login nor deposit button found.")
        return

    # Step 3: Check for Opt into Offer
    #open_coral_wager_and_check_spin_button()
    # Step 4: Go to Wager Page - https://www.coral.co.uk/en/games/launchng/playtechgoldentour
    print("Directing you to Golden Tour Slot")
    if not open_coral_wager_and_check_spin_button():
        return
    check_correct_wager_amount()