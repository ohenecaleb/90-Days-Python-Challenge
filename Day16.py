import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2')  # Assuming headlines are within <h2> tags

    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline.get_text(strip=True)}")

if __name__ == "__main__":
    url = 'https://example-news-website.com'  # Replace with the actual news website URL
    scrape_headlines(url)

#Code by Caleb