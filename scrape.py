import requests
from bs4 import BeautifulSoup
import os
import re
import time
from random import uniform

# URL of the website to scrape
url = 'https://www.my-website-example.com'

# Set a User-Agent header to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Create a session
session = requests.Session()

# Function to add a random delay between requests
def random_delay(min_delay=1, max_delay=3):
    time.sleep(uniform(min_delay, max_delay))

# Send a GET request to fetch the HTML content
print("Fetching webpage...")
response = session.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Webpage fetched successfully.")

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create a directory to save images
    os.makedirs('images', exist_ok=True)
    print("Created 'images' directory.")

    # Find all image tags
    img_tags = soup.find_all('img')
    print(f"Found {len(img_tags)} image(s) on the webpage.")

    # Track downloaded URLs to avoid duplicates
    downloaded_urls = set()

    # Loop through the image tags and download the images
    for img in img_tags:
        img_url = img.get('src')
        if img_url and img_url not in downloaded_urls:  # Skip if already downloaded
            print(f"Processing image URL: {img_url}")

            # Handle relative URLs
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif img_url.startswith('/'):
                img_url = 'https://recovery.lacounty.gov' + img_url
            elif not img_url.startswith('http'):
                img_url = url + img_url

            # Skip non-image URLs (e.g., tracking pixels)
            if not any(img_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
                print(f"Skipping non-image URL: {img_url}")
                continue

            # Sanitize the image name
            img_name = img_url.split('/')[-1]  # Get the last part of the URL
            img_name = img_name.split('?')[0]  # Remove query parameters
            img_name = re.sub(r'[^\w\-_.]', '_', img_name)  # Replace invalid characters
            img_name = os.path.join('images', img_name)  # Add the 'images' directory

            # Download the image
            try:
                print(f"Downloading {img_url}...")
                img_data = session.get(img_url, headers=headers)
                img_data.raise_for_status()  # Raise an error for bad responses
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data.content)
                print(f"Downloaded: {img_name}")
                downloaded_urls.add(img_url)  # Add URL to the set of downloaded URLs
                
                # Add a random delay between requests
                random_delay()
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {img_url}: {e}")

    print("Images have been downloaded successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
