import requests
from bs4 import BeautifulSoup
import json

def get_stats():
    url = "https://proclubshead.com/24/club/ps5-2158921/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    jogadores = []
    # O script procura as linhas da tabela no Pro Clubs Head
    rows = soup.find_all('tr')[1:] # Pula o cabeçalho
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 5:
            nome = cols[1].text.strip()
            # Filtra apenas os 3 principais se quiser, ou pega todos
            if nome in ["Walison", "Luigi", "Nicolas"]:
                jogadores.append({
                    "nome": nome,
                    "pj": cols[2].text.strip(),
                    "gols": cols[3].text.strip(),
                    "ast": cols[4].text.strip()
                })
    
    with open('stats.json', 'w') as f:
        json.dump({"jogadores": jogadores}, f)

if __name__ == "__main__":
    get_stats()
