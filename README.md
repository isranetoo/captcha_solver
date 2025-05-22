"""
# captcha_solver

Este projeto é uma solução completa para reconhecimento de CAPTCHAs usando redes neurais convolucionais (CNN e CRNN) com Keras/TensorFlow.

## Estrutura do Projeto
- `dataset/`: imagens de treino e teste rotuladas
- `src/`: scripts para coleta, preprocessamento, treinamento, predição, avaliação, augmentação e exportação
- `notebooks/`: notebooks para análise exploratória e análise de erros
- `gui_app.py`: aplicação com interface gráfica

## Passos
1. Colete CAPTCHAs com `collector.py`
2. Preprocessamento com `preprocess.py`
3. (Opcional) Augmente os dados com `augment.py`
4. Treinamento:
   - CNN com `train.py`
   - CRNN com `train_ctc.py`
5. Avaliação com `evaluate.py`
6. Predição individual com `predict.py`
7. Interface Gráfica com `gui_app.py`
8. Exportação para TFLite com `export.py`

## Requisitos
```bash
pip install tensorflow keras opencv-python numpy matplotlib albumentations pillow
```

## Execução
```bash
python src/train.py
python src/train_ctc.py
python src/evaluate.py
python src/gui_app.py
python src/export.py
```
"""