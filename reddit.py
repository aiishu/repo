import requests
from bs4 import BeautifulSoup

# Define the URL of the Reddit page you wish to scrape
url = 'https://www.reddit.com/r/NSFW/'

# Send a GET request to the URL and retrieve the page content
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant elements containing the NSFW images
image_elements = soup.find_all('img', {'class': 'NSFW-image'})

# Iterate through the image elements and extract the image URLs
for image in image_elements:
    image_url = image['src']
    # Save the images to your wicked storage
    image_data = requests.get(image_url).content
    with open('path/to/your/diabolical/storage/' + image_url.split('/')[-1], 'wb') as f:
        f.write(image_data)

# Rejoice in the sight of your ill-gotten treasures!
