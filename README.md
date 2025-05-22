# captcha_solver

Este projeto é uma solução completa para automação e resolução de CAPTCHAs utilizando inteligência artificial. Ele abrange desde a coleta de dados, preprocessamento, aumento de dados (augmentation), treinamento de modelos (CNN e CRNN), avaliação, exportação para uso em dispositivos móveis e interface gráfica para uso prático.

---

## 📁 Estrutura do Projeto
```
captcha_solver/
├── dataset/                # Imagens rotuladas para treino e teste
│   ├── train/
│   └── test/
├── notebooks/             # Análises e visualizações em Jupyter
│   ├── exploratory_analysis.ipynb
│   └── error_analysis.ipynb
├── src/                   # Código-fonte do projeto
│   ├── augment.py         # Geração de dados aumentados
│   ├── collector.py       # Coletor de CAPTCHAs via URL
│   ├── evaluate.py        # Avaliação da acurácia do modelo
│   ├── export.py          # Exportação do modelo para TFLite
│   ├── gui_app.py         # Aplicação com interface gráfica (Tkinter)
│   ├── model.py           # Modelo CNN
│   ├── model_crnn.py      # Modelo CRNN (para CTC)
│   ├── predict.py         # Predição de novos CAPTCHAs
│   ├── preprocess.py      # Preprocessamento das imagens
│   ├── train.py           # Treinamento CNN
│   └── train_ctc.py       # Treinamento CRNN (CTC Loss)
```

---

## ⚙️ Requisitos
```bash
pip install tensorflow keras opencv-python numpy matplotlib albumentations pillow
```

---

## Como funciona?
O fluxo principal do projeto é:
1. **Coleta de dados**: Captura manual de CAPTCHAs rotulados para criar o dataset.
2. **Preprocessamento**: As imagens são convertidas para tons de cinza, redimensionadas, binarizadas e suavizadas para facilitar o reconhecimento.
3. **Aumento de dados (Augmentation)**: Aplica distorções e filtros para simular variações e aumentar a base de dados.
4. **Treinamento dos modelos**: Dois modelos são treinados:
   - **CNN**: Para CAPTCHAs de tamanho fixo (5 caracteres).
   - **CRNN + CTC Loss**: Para CAPTCHAs de tamanho variável.
5. **Avaliação**: Mede a acurácia dos modelos comparando as predições com os rótulos reais.
6. **Exportação**: Converte o modelo treinado para o formato `.tflite` para uso em dispositivos móveis.
7. **Interface gráfica**: Permite ao usuário selecionar uma imagem e ver o resultado da predição.
8. **Análise de dados e erros**: Notebooks Jupyter para explorar o dataset e analisar o desempenho dos modelos.

## How to use

### 1. Data Collection
Run the script to collect CAPTCHA images and label them manually:
```bash
python src/collector.py
```
The images will be saved in `dataset/train/` with the filename equal to the CAPTCHA text.

### 2. Preprocessing
Preprocessing is done automatically during data loading for training and prediction.

### 3. Augmentation (optional)
Implement or adapt the script `src/augment.py` to increase the dataset with variations of the original images.

### 4. Model Training
To train the CNN model (fixed at 5 characters):
```bash
python src/train.py
```
Output: `captcha_model.h5`

To train the CRNN model (variable length):
```bash
python src/train_ctc.py
```
Output: `captcha_crnn.h5`

### 5. Avaliação
Avalie o desempenho do modelo CNN:
```bash
python src/evaluate.py
```

### 6. Predição
Faça a predição do texto de um CAPTCHA a partir de uma imagem:
```bash
python src/predict.py caminho/da/imagem.png
```

### 7. Interface Gráfica
Abra a interface gráfica para selecionar uma imagem e ver o resultado da IA:
```bash
python src/gui_app.py
```

### 8. Exportação para TFLite
Converta o modelo `.h5` para `.tflite` para uso em apps móveis:
```bash
python src/export.py
```

### 9. Análises (Jupyter)
Utilize os notebooks para:
- Explorar os dados: `notebooks/exploratory_analysis.ipynb`
- Analisar erros e acurácia: `notebooks/error_analysis.ipynb`

### 10. Workflow automatizado
Para executar todas as etapas (exceto coleta manual) em sequência:
```bash
python run_all.py
```

---

## ✨ Possíveis Melhorias
- Uso de OCR + aprendizado semi-supervisionado
- Treinamento com mais dados rotulados via serviço externo (2Captcha, AntiCaptcha)
- Adição de quantização na exportação `.tflite`
- Versão com FastAPI para inferência web

---

## 👨‍💻 Autor
Este projeto foi estruturado para aprendizado e automação de CAPTCHAs com inteligência artificial e é mantido por [Israel Neto].

---

Pronto para usar ou expandir com base nas suas necessidades!