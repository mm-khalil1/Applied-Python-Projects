"""
Web Scraper
This script scrapes book information from the website 'https://books.toscrape.com'. 
It retrieves the titles and star ratings of books listed on the site 
using BeautifulSoup and displays the results.

Author: Mahmoud Khalil
Date: 07-12-2023
"""

import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://books.toscrape.com"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <li> elements with the specified class
    list_items = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    # Create a list to store book information as dictionaries
    books = []

    # Extract and store title and star rating for each book
    for lst in list_items:
        # Extract title from <h3> element
        h3_element = str(lst.find('h3'))
        title_start_index = h3_element.find("title=") + 7
        title_end_index = h3_element.find('"')
        title = h3_element[title_start_index : title_end_index]
        
        # Extract star rating from <li> element
        rating_begin = str(lst).split("star-rating ")[1]
        rating = rating_begin[ : rating_begin.find('">')]
        
        # Store book information in a dictionary
        book = {'title': title, 'rating': rating}
        
        # Add the dictionary to the list
        books.append(book)
    
    # Print the stored book information
    for book in books:
        print(f"Book Title: {book['title']}. \nStar Rating: {book['rating']}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
