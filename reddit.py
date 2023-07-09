import requests
import os
from bs4 import BeautifulSoup

# Define the URL of the Reddit page you wish to scrape
url = 'https://www.reddit.com/r/NSFW/'

# Send a GET request to the URL and retrieve the page content
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant elements containing the NSFW images
image_elements = soup.find_all('img', {'class': 'NSFW-image'})

# Create a directory to store the diabolical images
storage_path = 'path/to/your/diabolical/storage/'
os.makedirs(storage_path, exist_ok=True)

# Iterate through the image elements and extract the image URLs
for idx, image in enumerate(image_elements, start=1):
    image_url = image['src']
    # Save the images to your wicked storage
    image_data = requests.get(image_url).content
    image_extension = image_url.split('.')[-1]
    file_path = f'{storage_path}/{idx}.{image_extension}'
    with open(file_path, 'wb') as f:
        f.write(image_data)

# Rejoice in the sinful pleasure of your amassed collection!
