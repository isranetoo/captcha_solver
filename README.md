# captcha_solver

<p align="center">
  <img src="https://i.ibb.co/ymKKZ3q8/logo-ia.png" alt="captcha_solver logo" width="220"/>
</p>

Este projeto é uma solução completa para automação e resolução de CAPTCHAs utilizando inteligência artificial. Agora, o sistema suporta tanto CAPTCHAs de tamanho fixo (usando CNN) quanto de tamanho variável (usando CRNN com CTC Loss). O fluxo cobre desde a coleta de dados, preprocessamento automático, aumento de dados, treinamento, avaliação, exportação para dispositivos móveis e interface gráfica para uso prático.

---

## 📁 Estrutura do Projeto
```
├── analysis/
│   └── plot_training.py
├── captcha_generator/
│   ├── generate_captcha.py
│   ├── fonts/
│   │   └── DejaVuSans.ttf
│   └── output/
├── dataset/
│   ├── test/
│   └── train/
├── notebooks/
│   ├── error_analysis.ipynb
│   └── exploratory_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── augment.py
│   ├── collector.py
│   ├── evaluate.py
│   ├── export.py
│   ├── gui_app.py
│   ├── model_crnn.py
│   ├── model.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── train_ctc.py
│   └── train.py
├── captcha_model.h5
├── captcha_model.tflite
├── LICENSE
├── README.md
├── run_all.py
├── training_history.npy
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

## Como usar

### 1. Coleta de Dados
Execute o script para coletar imagens de CAPTCHA e rotulá-las manualmente:
```bash
python src/collector.py
```
As imagens serão salvas em `dataset/train/` com o nome do arquivo igual ao texto do CAPTCHA.

### 2. Preprocessamento
O preprocessamento é feito automaticamente durante o carregamento dos dados para treinamento e predição.

### 3. Aumento de Dados (opcional)
Implemente ou adapte o script `src/augment.py` para aumentar o conjunto de dados com variações das imagens originais.

### 4. Treinamento do Modelo
Para treinar o modelo CNN (fixo em 5 caracteres):
```bash
python src/train.py
```
Saída: `captcha_model.h5`

Para treinar o modelo CRNN (comprimento variável):
```bash
python src/train_ctc.py
```
Saída: `captcha_crnn.h5`

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