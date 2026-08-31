import requests
import time
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = -1003846952857

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA, "promocoes.txt")

def enviar(produto, preco, link):
    mensagem = f"""Promo do Surfista 🌊🌊

🏄‍♂️ {produto}
💰 {preco}

🛒 COMPRE AQUI 👇
{link}

⚡ Aproveite enquanto durar!"""

    r = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": mensagem}
    )

    print("✅ Enviado:", produto) if r.ok else print("❌ Erro:", r.text)

while True:
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = [x.strip() for x in f if x.strip()]

    for i in range(0, len(linhas), 3):
        if i + 2 < len(linhas):
            enviar(linhas[i], linhas[i+1], linhas[i+2])
            time.sleep(1800)
