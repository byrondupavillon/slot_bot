from functions import open_url_and_wait_for_image, detect_image_in_region, click_found_image


def open_coral_and_check_logo():
    """Open the Coral site and check for the logo."""
    url = "https://promo.coral.co.uk/en/promo/p/smart-rewards"
    coral_logo_path = './coral_wager_20_get_10_free_spins/images/coral_logo.jpg'
    coral_logo_region = (1728, 159, 130, 32)
    print("Opening Coral website...")
    if not open_url_and_wait_for_image(url, coral_logo_path, coral_logo_region):
        print("Failed to load the Coral website.")
        return False
    return True


def attempt_login():
    """Attempt to detect and click the login button."""
    login_image_path = './coral_wager_20_get_10_free_spins/images/login_btn.jpg'
    login_region = (3293, 152, 142, 43)
    print("Attempting to detect login button...")
    login_btn_detection = detect_image_in_region(login_image_path, login_region)
    if login_btn_detection:
        print("Found login button...")
        click_found_image(login_btn_detection, num_clicks=1)
        return True
    return False


def attempt_login_prompt_button():
    """Attempt to detect and click the login prompt button."""
    login_image_path = './coral_wager_20_get_10_free_spins/images/login_prompt_btn.jpg'
    login_region = (2406, 818, 349, 54)
    print("Attempting to detect login prompt button...")
    login_prompt_btn_detection = detect_image_in_region(login_image_path, login_region, confidence=1)
    if login_prompt_btn_detection:
        print("Found login button...")
        click_found_image(login_prompt_btn_detection, num_clicks=1)
        return True
    return False


def check_for_deposit_button():
    """Check for the deposit button and navigate to a new site if found."""
    deposit_image_path = './coral_wager_20_get_10_free_spins/images/deposit_btn.jpg'
    deposit_region = (3294, 153, 61, 43)
    print("Checking for deposit button...")
    if detect_image_in_region(deposit_image_path, deposit_region, confidence=0.7):
        print("Deposit button found. Navigating to Codeo site...")
        return True
    return False


def run_coral_task():
    """Main function to run the Coral task."""
    # Step 1: Open Coral site and check for the logo
    if not open_coral_and_check_logo():
        return

    # Step 2: Attempt to log in or check for the deposit button
    if attempt_login():
        attempt_login_prompt_button()
        print("Successfully logged in.")
    elif check_for_deposit_button():
        print("Already logged in.")
    else:
        print("Neither login nor deposit button found.")
        return

    # Step 3: Check for Opt into Offer
    # Step 4: Go to Wager Page - https://www.coral.co.uk/en/games/launchng/playtechgoldentour
