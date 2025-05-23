import os
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Caminhos
BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "fonts", "DejaVuSans.ttf")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Geração de texto aleatório com 5 caracteres
def gerar_texto(tamanho=5):
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choices(caracteres, k=tamanho))

# Geração de uma imagem CAPTCHA
def gerar_captcha(texto, nome_arquivo):
    largura = 120
    altura = 40
    imagem = Image.new("L", (largura, altura), color=255)
    draw = ImageDraw.Draw(imagem)

    fonte = ImageFont.truetype(FONT_PATH, 26)

    # Posição inicial ajustada para 5 caracteres
    x = 10
    for char in texto:
        y = random.randint(0, 10)
        draw.text((x, y), char, font=fonte, fill=0)
        x += 20  # espaçamento horizontal ajustado

    # Círculos de interferência
    for _ in range(8):
        x0 = random.randint(0, largura)
        y0 = random.randint(0, altura)
        d = random.randint(12, 35)
        draw.ellipse((x0, y0, x0 + d, y0 + d), outline=0)

    # Suavização leve
    imagem = imagem.filter(ImageFilter.GaussianBlur(0.3))

    # Salvar
    caminho_completo = os.path.join(OUTPUT_DIR, nome_arquivo)
    imagem.save(caminho_completo)
    print(f"CAPTCHA gerado: {caminho_completo}")

# Gera múltiplos CAPTCHAs
def gerar_lote(qtd=10):
    for i in range(qtd):
        texto = gerar_texto()
        gerar_captcha(texto, f"{texto}.png")

if __name__ == "__main__":
    gerar_lote(10000)
