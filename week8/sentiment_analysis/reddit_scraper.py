import requests
from bs4 import BeautifulSoup
import time

# URL of the website to scrape
url = 'https://www.reddit.com/r/technology/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with an id that starts with "post-title"
    posts = soup.select('shreddit-post')

    for post in posts:
        print(f"Title: {post['post-title']}")
        print(f"Author: {post['author']}")
        print(f"Creation Date & Time: {post['created-timestamp']}")
        print(f"Score: {post['score']}")
        print(f"Number of Comments: {post['comment-count']}")
        print(f"Permalink: {post['permalink']}")
        print("\n" + "=" * 40 + "\n")
        time.sleep(1)


else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")