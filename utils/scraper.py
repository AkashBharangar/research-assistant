import requests
from bs4 import BeautifulSoup

def read_webpage(url: str) -> str:
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style","nav","footer","header","aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text


    except Exception as e:
        return f"Error: {e}"