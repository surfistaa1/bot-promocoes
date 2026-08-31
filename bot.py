import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = -1003846952857

with open("promocoes.txt", "r", encoding="utf-8") as arquivo:
    linhas = [x.strip() for x in arquivo if x.strip()]

if len(linhas) >= 3:
    produto = linhas[0]
    preco = linhas[1]
    link = linhas[2]

    mensagem = f"""🌊 PROMO DO SURFISTA 🏄

🛍️ {produto}
💰 {preco}

🛒 COMPRE AQUI 👇
{link}

🏄‍♂️ Aproveita essa onda antes que ela passe! 🌊"""

    resposta = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensagem
        }
    )

    if resposta.ok:
        print("Promoção enviada!")

        with open("promocoes.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("\n".join(linhas[3:]))
    else:
        print("Erro ao enviar:", resposta.text)
else:
    print("Não há promoções suficientes.")
