# run_all.py
"""
Script para executar o workflow completo do captcha_solver, exceto a coleta manual (collector.py).

Etapas:
1. Augmentação dos dados (opcional, se desejar aumentar dataset)
2. Treinamento dos modelos (CNN e CRNN)
3. Avaliação dos modelos
4. Exportação para TFLite
5. Interface gráfica (opcional)

Execute: python run_all.py
"""
import subprocess
import sys
import os

# Caminho base
SRC = os.path.join(os.path.dirname(__file__), 'src')

# 1. Augmentação (opcional, depende de implementação de script de augmentação em lote)
# subprocess.run([sys.executable, os.path.join(SRC, 'augment.py')])

# 2. Treinamento dos modelos
print('Treinando modelo CNN...')
subprocess.run([sys.executable, "-m", "src.train"], check=True, cwd=os.path.dirname(__file__))

print('Treinando modelo CRNN (CTC)...')
subprocess.run([sys.executable, "-m", "src.train_ctc"], check=True, cwd=os.path.dirname(__file__))

# 3. Avaliação dos modelos
print('Avaliando modelo CNN...')
subprocess.run([sys.executable, "-m", "src.evaluate"], check=True, cwd=os.path.dirname(__file__))

# 4. Exportação para TFLite
print('Exportando modelo CNN para TFLite...')
subprocess.run([sys.executable, "-m", "src.export"], check=True, cwd=os.path.dirname(__file__))

print('\nWorkflow finalizado!')
print('Para interface gráfica, execute: python -m src.gui_app')
print('Para predição individual: python -m src.predict caminho/da/imagem.png')
