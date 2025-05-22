# collector.py
import os
import requests

def collect_captchas(url, save_dir, total=100):
    os.makedirs(save_dir, exist_ok=True)
    for i in range(total):
        response = requests.get(url)
        code = input("Digite o texto do captcha mostrado: ")
        with open(f"{save_dir}/{code}.png", "wb") as f:
            f.write(response.content)
