
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Garante que o pacote src seja encontrado ao importar
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Caminho para o modelo treinado e histórico (ajuste se necessário)
MODEL_PATH = os.path.abspath(os.path.join(ROOT, "captcha_model.h5"))

def plot_history(history):
    # history pode ser um dict ou um objeto History do Keras
    if hasattr(history, 'history'):
        history = history.history

    # Plota loss
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history['loss'], label='train loss')
    if 'val_loss' in history:
        plt.plot(history['val_loss'], label='val loss')
    plt.title('Loss')
    plt.legend()

    # Plota acurácia de cada caractere
    plt.subplot(1, 2, 2)
    for i in range(5):
        key = f'char_{i}_accuracy'
        if key in history:
            plt.plot(history[key], label=f'char_{i+1} acc')
    plt.title('Accuracy por caractere')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():

    # 1. Carrega histórico de treinamento, se existir
    history_path = os.path.join(ROOT, "training_history.npy")
    if os.path.exists(history_path):
        history = np.load(history_path, allow_pickle=True).item()
        plot_history(history)
    else:
        print("[AVISO] Arquivo de histórico de treinamento não encontrado.")

    # 2. Avaliação do modelo no conjunto de teste
    from src.train import load_dataset, CHARS
    model = tf.keras.models.load_model(MODEL_PATH)
    X_test, Y_test = load_dataset(os.path.join(ROOT, "dataset", "test"))
    results = model.evaluate(X_test, Y_test, verbose=1)
    print("Resultados do teste:", results)

    # 3. Predição em lote
    Y_pred = model.predict(X_test)

    # 4. Matrizes de confusão para cada caractere
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    for i in range(5):
        y_true = np.argmax(Y_test[i], axis=1)
        y_pred = np.argmax(Y_pred[i], axis=1)
        classes_presentes = np.unique(np.concatenate([y_true, y_pred]))
        labels_usados = [CHARS[j] for j in classes_presentes]
        cm = confusion_matrix(y_true, y_pred, labels=classes_presentes)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels_usados)
        disp.plot(ax=axes[i], xticks_rotation='vertical', colorbar=False)
        axes[i].set_title(f"Matriz confusão - char {i+1}")
    plt.tight_layout()
    plt.show()

    # 5. Histograma de acertos por caractere
    plt.figure(figsize=(8,4))
    accs = []
    for i in range(5):
        y_true = np.argmax(Y_test[i], axis=1)
        y_pred = np.argmax(Y_pred[i], axis=1)
        acc = np.mean(y_true == y_pred)
        accs.append(acc)
    plt.bar([f'char_{i+1}' for i in range(5)], accs)
    plt.ylim(0,1)
    plt.ylabel('Acurácia')
    plt.title('Acurácia por posição do caractere')
    plt.show()

    # 6. Acurácia total do captcha (todos os caracteres corretos)
    y_true_all = np.stack([np.argmax(Y_test[i], axis=1) for i in range(5)], axis=1)
    y_pred_all = np.stack([np.argmax(Y_pred[i], axis=1) for i in range(5)], axis=1)
    total_correct = np.all(y_true_all == y_pred_all, axis=1).sum()
    total_acc = total_correct / len(X_test)
    print(f"Acurácia total (captcha inteiro): {total_acc*100:.2f}%")

    # 7. Exemplos de predições corretas e incorretas
    print("Exemplos de predições incorretas:")
    for idx in range(len(X_test)):
        true_str = ''.join([CHARS[c] for c in y_true_all[idx]])
        pred_str = ''.join([CHARS[c] for c in y_pred_all[idx]])
        if true_str != pred_str:
            print(f"GT: {true_str} | Pred: {pred_str}")
        if idx > 10:
            break

if __name__ == "__main__":
    main()