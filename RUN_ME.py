import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def wait_random(min_time=1, max_time=3):
    """Simulate human-like random wait time."""
    time.sleep(random.uniform(min_time, max_time))

def main():
    # Use undetected-chromedriver to avoid detection
    options = uc.ChromeOptions()
    
    # Disable features that reveal automation
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--disable-automation")
    options.add_argument("--disable-features=CDP")
    options.add_argument("--start-maximized")
    options.add_argument("--log-level=3")  # Disable console logs
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-component-extensions-with-background-pages")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-breakpad")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-component-update")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-devtools-experiments")
    options.add_argument("--disable-domain-reliability")
    options.add_argument("--disable-features=IsolateOrigins, site-per-process")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-ipc-flooding-protection")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-offline-auto-reload")
    options.add_argument("--disable-offline-auto-reload-visible-only")
    options.add_argument("--disable-password-generation")
    options.add_argument("--disable-payments-api")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-renderer-accessibility")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-search-geolocation-disclosure")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-speech-api")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-tab-groups")
    options.add_argument("--disable-usbguard")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=IsolateOrigins")
    options.add_argument("--disable-features=site-per-process")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-features=Oopif")
    options.add_argument("--disable-features=OopifIsolation")
    options.add_argument("--disable-features=OverlayScrollbar")
    options.add_argument("--disable-features=PaintHolding")
    options.add_argument("--disable-features=PartitionAlloc")
    options.add_argument("--disable-features=PartitionAllocForTesting")
    options.add_argument("--disable-features=ProcessPerTab")
    options.add_argument("--disable-features=ProcessPerTabForTesting")
    options.add_argument("--disable-features=SitePerProcess")
    options.add_argument("--disable-features=SubresourceFilter")
    options.add_argument("--disable-features=V8PerIsolateCodeCache")
    options.add_argument("--disable-features=V8PerIsolateCodeCacheForTesting")

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://hmaker.github.io/selenium-detector/")

        # Wait for the page to load
        wait_random(2, 5)

        # Locate the input fields
        token_input = driver.find_element(By.ID, "tokenInput")
        async_token_input = driver.find_element(By.ID, "asyncTokenInput")

        # Simulate human typing behavior using ActionChains
        actions = ActionChains(driver)

        # Retrieve the value of window.token
        token_value = driver.execute_script("return window.token")
        print(f"Token value: {token_value}")

        # Simulate human typing for token value
        for char in token_value:
            actions.send_keys(char)
            wait_random(0.1, 0.3)
        actions.perform()

        # Wait a bit before entering the second value
        wait_random(1, 3)

        # Retrieve the value of window.getAsyncToken()
        async_token_value = driver.execute_script("return window.getAsyncToken()")
        print(f"Async Token value: {async_token_value}")

        # Simulate human typing for async token value
        for char in async_token_value:
            actions.send_keys(char)
            wait_random(0.1, 0.3)
        actions.perform()

        # Wait a bit before clicking the button
        wait_random(2, 5)

        # Locate and click the "Interaction Test" button
        test_button = driver.find_element(By.ID, "interactionTest")
        actions.move_to_element(test_button).perform()
        wait_random(0.5, 1)
        test_button.click()

        # Wait for the result
        wait_random(3, 5)

        # Retrieve and print the detection result
        result = driver.find_element(By.ID, "result").text
        print(f"Detection result: {result}")

    finally:
        # Wait a while before closing the browser
        time.sleep(90)
        driver.quit()

if __name__ == "__main__":
    main()

