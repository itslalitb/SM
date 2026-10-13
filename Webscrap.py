
import requests
from bs4 import BeautifulSoup

url = "https://www.paruluniversity.ac.in/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Title:", soup.title.string if soup.title else "No Title")

h1_tags = soup.find_all("h1")
print("H1 Count:", len(h1_tags))

for h1 in h1_tags:
    print("H1:", h1.get_text(strip=True))

meta_tags = soup.find_all("meta")
print("Meta Tags Count:", len(meta_tags))



# pip install requests beautifulsoup4
# python -m pip install requests beautifulsoup4