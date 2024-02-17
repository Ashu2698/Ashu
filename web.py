import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data from the parsed HTML
        # Example: Extract all the text from <h1> tags
        headings = soup.find_all('h1')
        for heading in headings:
            print(heading.text)
    else:
        print("Failed to retrieve data from the website.")

def main():
    # URL of the website to scrape
    url = 'https://example.com'

    # Call the scrape_website function with the URL
    scrape_website(url)

if __name__ == "__main__":
    main()
