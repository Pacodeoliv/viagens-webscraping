import requests
from bs4 import BeautifulSoup 
import time

def fetch_page():
        url = "https://www.mercadolivre.com.br/creatina-monohidratada-100-300g-integralmedica-sabor-neutro/p/MLB6204289#polycard_client=search-nordic&searchVariation=MLB6204289&wid=MLB3582503463&position=5&search_layout=stack&type=product&tracking_id=669de623-ad9e-4fa7-a646-3d60887bf208&sid=search"
        response = requests.get(url)
        return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_ = 'ui-pdp-title').get_text()
    prices: list =soup.find_all('span', class_='andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', ' '))
    new_price: int = int(prices[1].get_text().replace('.', ' '))
    installment_price: int = int(prices[2].get_text().replace('.', ' '))
    

    
    return {
         'product_name': product_name,
         'old_price': old_price,
         'new_price': new_price,
         'installment_price': installment_price

    }
    
    

if __name__ == "__main__":
    while True:
         
        page_content = fetch_page()
        produto_info = parse_page(page_content)
        print(produto_info)
        time.sleep(10)
    