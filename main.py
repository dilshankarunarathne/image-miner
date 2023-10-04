import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def download_images(search_query, num_images):
    # Create a new folder for the search query if it doesn't exist
    if not os.path.exists(search_query):
        os.makedirs(search_query)

    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Perform a Google image search
        search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"
        driver.get(search_url)

        # Scroll down to load more images (you might need to adjust this based on the number of images you want)
        for _ in range(num_images // 20):
            driver.find_element('body').send_keys(Keys.END)
            time.sleep(2)  # Wait for 2 seconds to load more images

        # Get the URLs of the top images
        from selenium.webdriver.common.by import By

    except Exception as e:
        print(f"Error: {e}")
        print(f"Current URL: {driver.current_url}")

    finally:
        # Quit the WebDriver
        driver.quit()


download_images("cats", 10)
