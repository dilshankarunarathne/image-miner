import os
import requests
from bs4 import BeautifulSoup


def download_images(search_query, num_images):
    # Create a new folder for the search query if it doesn't exist
    if not os.path.exists(search_query):
        os.makedirs(search_query)

    # Perform a Google image search
    search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    response = requests.get(search_url)

    # Parse the HTML content of the search results page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract image URLs
    img_tags = soup.find_all('img', class_='rg_i')
    img_urls = [img['data-src'] for img in img_tags if 'data-src' in img.attrs]

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


# Example usage
if __name__ == "__main__":
    search_query = input("Enter search query: ")
    num_images = int(input("Enter number of images to download: "))
    download_images(search_query, num_images)
    print(f"{num_images} images downloaded and stored in the '{search_query}' folder.")
