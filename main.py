import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def download_images(search_query, num_images):
    # Create a new folder for the search query if it doesn't exist
    if not os.path.exists(search_query):
        os.makedirs(search_query)

    # Use Selenium to perform a Google image search and download the specified number of images
    driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed.
    search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"

    driver.get(search_url)

    # Scroll down to load more images (you might need to adjust this based on the number of images you want)
    for _ in range(num_images // 20):
        driver.find_element_by_css_selector('body').send_keys(Keys.END)

    # Get image URLs
    img_urls = [img.get_attribute('src') for img in driver.find_elements_by_css_selector('img.rg_i')]

    # Download the specified number of images
    for i, img_url in enumerate(img_urls[:num_images]):
        try:
            response = requests.get(img_url, stream=True)
            # Extract image name from URL
            img_name = os.path.join(search_query, f"{i + 1}.jpg")
            with open(img_name, 'wb') as img_file:
                for chunk in response.iter_content(1024):
                    img_file.write(chunk)
        except Exception as e:
            print(f"Failed to download {img_url}: {str(e)}")
            continue

    driver.quit()


# Example usage
if __name__ == "__main__":
    search_query = input("Enter search query: ")
    num_images = int(input("Enter number of images to download: "))
    download_images(search_query, num_images)
    print(f"{num_images} images downloaded and stored in the '{search_query}' folder.")
