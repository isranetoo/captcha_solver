# gui_app.py
import tkinter as tk
from tkinter import filedialog
from src.predict import predict
from PIL import ImageTk, Image

class CaptchaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Captcha Solver")
        self.label = tk.Label(root, text="Escolha uma imagem")
        self.label.pack()
        self.btn = tk.Button(root, text="Abrir", command=self.load_img)
        self.btn.pack()
        self.img_label = tk.Label(root)
        self.img_label.pack()
        self.result = tk.Label(root, text="Resultado: ")
        self.result.pack()

    def load_img(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((200, 60))
            self.img = ImageTk.PhotoImage(img)
            self.img_label.configure(image=self.img)
            pred = predict(file_path)
            # Mostra apenas os 5 primeiros caracteres
            self.result.config(text=f"Resultado: {pred[:5]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptchaGUI(root)
    root.mainloop()
