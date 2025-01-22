import requests
from bs4 import BeautifulSoup 
import time
import pandas as pd
import sqlite3

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
    
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price,
        'timestamp': timestamp
    }
    
def create_connection(db_name = 'creatina_prices.db'):
    """Cria uma conexão com o banco de dados SQLite"""
    conn = sqlite3.connect(db_name)
    return conn


def setup_database(conn):
    """Cria a tabela de preços se ela não existir"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        old_price INTEGER,
        new_price INTEGER,
        installment_price INTEGER,
        timestamp TEXT
        )
    ''')
    conn.commit()


def save_to_dataframe(product_info, df):
    new_row = pd.DataFrame([product_info])
    df = pd.concat([df, new_row], ignore_index = True)
    return df




if __name__ == "__main__":


    conn = 

    df = pd.DataFrame()
    
    while True:
         
        page_content = fetch_page()
        produto_info = parse_page(page_content)
        df = save_to_dataframe(produto_info, df)
        print(df)
        time.sleep(10)
    