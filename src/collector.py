# collector.py
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

url = "https://certidao.trt3.jus.br/certidao/feitosTrabalhistas/aba1.emissao.htm"
output_dir = "dataset/train"
os.makedirs(output_dir, exist_ok=True)

driver = webdriver.Chrome()  # Certifique-se de que o chromedriver está no PATH

for i in range(500):
    # Abre uma nova aba e navega até a página do captcha
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    time.sleep(2)
    captcha_img = driver.find_element(By.XPATH, '//*[@id="form:imagemCaptcha"]')
    captcha_src = captcha_img.get_attribute("src")
    # Salva a imagem com um nome temporário
    temp_filename = f"{output_dir}/temp_{i}.png"
    with open(temp_filename, "wb") as f:
        f.write(requests.get(captcha_src).content)
    # Mostra o caminho da imagem para o usuário digitar o texto
    print(f"Imagem salva em: {temp_filename}")
    code = input("Qual o texto do captcha mostrado? ")
    # Renomeia o arquivo para o nome informado
    final_filename = f"{output_dir}/{code}.png"
    os.rename(temp_filename, final_filename)
    # Fecha a aba atual e volta para a anterior
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

driver.quit()

