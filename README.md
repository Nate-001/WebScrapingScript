# Web Scraping Script for Image Downloading

This Python script scrapes images from a specified webpage and downloads them to a local directory. It uses the `requests` and `BeautifulSoup` libraries for web scraping and includes features such as random delays between requests to mimic human behavior.

---

## Features
- Fetches HTML content of a webpage.
- Parses the page to find all image tags (``).
- Handles relative and absolute URLs for images.
- Downloads images while avoiding duplicates.
- Skips non-image URLs (e.g., tracking pixels).
- Adds random delays between requests to avoid overloading the server.

---

## Requirements
- Python 3.x
- Libraries: `requests`, `BeautifulSoup4`

Install the required libraries using:
```
pip install requests beautifulsoup4
```

---

## Usage
1. **Set Up the Script**:
   - Replace the `url` variable in the script with the URL of the webpage you want to scrape.

2. **Run the Script**:
   Execute the script in your terminal or command prompt:
   ```
   python script_name.py
   ```

3. **Output**:
   - The script will create an `images` directory in the current working directory.
   - All downloaded images will be saved in this directory.

---

## Code Overview

### Key Functions:
1. **Random Delay**:
   Adds a random delay between requests to mimic human browsing behavior:
   ```
   def random_delay(min_delay=1, max_delay=3):
       time.sleep(uniform(min_delay, max_delay))
   ```

2. **Image Downloading**:
   - Handles relative URLs, appending the base URL where necessary.
   - Skips non-image URLs based on file extensions (`.jpg`, `.png`, etc.).
   - Sanitizes filenames to ensure compatibility with all filesystems.

---

## Example Output
- The script will log its progress in the terminal, including:
  - Number of images found on the webpage.
  - Status of each image download (success or failure).

Example log:
```
Fetching webpage...
Webpage fetched successfully.
Created 'images' directory.
Found 10 image(s) on the webpage.
Processing image URL: https://example.com/image1.jpg
Downloading https://example.com/image1.jpg...
Downloaded: images/image1.jpg
```

---

## Best Practices for Web Scraping
1. **Respect Robots.txt**: Always check if scraping is allowed on the target website.
2. **Avoid Overloading Servers**: Use delays between requests to reduce server load.
3. **Ethical Scraping**: Only scrape publicly available data and adhere to legal guidelines.

For more information on ethical scraping practices, refer to this [guide](https://www.scrapingbee.com/blog/web-scraping-101-with-python/).

---

## Disclaimer
This script is intended for educational purposes only. Ensure you have permission to scrape data from any website before using this tool.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
