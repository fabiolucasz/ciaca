import requests
import json
import re
from bs4 import BeautifulSoup


def get_fii():
    url_fii = "https://investidor10.com.br/fiis/gare11/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url_fii, headers=headers)
    print(response.status_code)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        header = soup.select('div._card-header div span')
        cotacao = header[0].text if header else "Não encontrado"
        print(cotacao)
        
        
        # Exemplo 1: Extrair valor usando regex por classe
        # cotacao_match = re.search(r'<span class="nome-da-classe">([^<]+)</span>', html)
        # cotacao = cotacao_match.group(1) if cotacao_match else "Não encontrado"
        
        # Exemplo 2: Extrair valor por atributo data
        # cotacao_match = re.search(r'data-valor="([^"]+)"', html)
        # cotacao = cotacao_match.group(1) if cotacao_match else "Não encontrado"
        
        # Exemplo 3: Extrair valor entre tags específicas
        # cotacao_match = re.search(r'<div class="card-body">\s*<span>([^<]+)</span>', html)
        # cotacao = cotacao_match.group(1) if cotacao_match else "Não encontrado"
        
        
        
        json_data = {
            "name": "GARE11",
            "cotacao": cotacao,
        }
        
        with open("fii_data.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)


    else:
        print("Erro ao acessar a página")

if __name__ == "__main__":
    get_fii()
