from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
from datetime import datetime
import json

directory = os.path.join(os.path.dirname(os.getcwd()), 'exports')
os.makedirs(directory, exist_ok=True)

now = datetime.today().strftime('%Y-%m-%d')

file_path = os.path.join(directory, f"poem-{now}.json" )

class ScrapeWebsite: 
    text = ''
    def __init__(self, url):
        self.url = url

        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
        chrome_options.add_argument("--disable-infobars")
        # chrome_options.add_argument("--headless=new")

        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            driver.get(url)

            page_source = driver.page_source

            soup = BeautifulSoup(page_source,'html.parser')

            self.title = soup.title.string if soup.title else "No title found"
            
            if soup.body:
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                self.text = soup.body.get_text(separator="\n", strip=True)

            links = []
            anchor_links = soup.find_all('a')
            for link in anchor_links:
                href = link.get('href')
                if (href and 'http' not in href and link):
                    links.append(url + href)
            
            self.links = links


        finally:
            driver.close()

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"
        

def get_news_details(url):
    website = ScrapeWebsite(url)
    content = website.get_contents()
    result = "Landing page:\n"
    result += content
    # links = get_links(website.url, website.links)
    # for link in links["links"]:
    #     result += f"\n\n{link['type']}\n"
    #     result += ScrapeWebsite(link["url"]).get_contents()
        # time.sleep(1)

    data = {
        "date": now,
        "content": result,
        "url": website.url
    }
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return result




