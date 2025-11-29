import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape():
    url = "https://books.toscrape.com/"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    items=[]
    for prod in soup.select(".product_pod"):
        title=prod.h3.a["title"]
        price=prod.select_one(".price_color").get_text(strip=True)
        items.append({"title":title, "price":price})
    df=pd.DataFrame(items)
    out=f"books_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(out, index=False)
    print("Saved", out)

if __name__=="__main__":
    scrape()
