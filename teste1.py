import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Algoritmo de Upscale (Vizinho Mais Próximo)
def upscale_vizinho_proximo(img_orig, fator):
    largura_orig, altura_orig = img_orig.size
    pixels_orig = img_orig.load()
    
    largura_nova = largura_orig * fator
    altura_nova = altura_orig * fator
    
    img_nova = Image.new("RGB", (largura_nova, altura_nova))
    pixels_novos = img_nova.load()
    
    for y_novo in range(altura_nova):
        for x_novo in range(largura_nova):
            x_orig = int(x_novo / fator)
            y_orig = int(y_novo / fator)
            pixels_novos[x_novo, y_novo] = pixels_orig[x_orig, y_orig]
            
    return img_nova

class AplicacaoUpscale:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Pixel Art Upscaler - Interface")
        self.janela.geometry("1280x720")

        self.img_original = None
        self.img_processada = None

        # --- Painel de Controles Superior ---
        frame_controles = tk.Frame(janela)
        frame_controles.pack(pady=10)

        tk.Button(frame_controles, text="Carregar Imagem", command=self.carregar_imagem).pack(side=tk.LEFT, padx=5)
        
        tk.Label(frame_controles, text="Escala:").pack(side=tk.LEFT, padx=5)
        self.fator_var = tk.IntVar(value=2)
        
        # Menu para escolher o fator de escala
        menu_escala = tk.OptionMenu(frame_controles, self.fator_var, 2, 3, 4, 6, command=lambda _: self.gerar_preview())
        menu_escala.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_controles, text="Salvar Imagem", command=self.salvar_imagem).pack(side=tk.LEFT, padx=5)

        # --- Área de Exibição do Preview ---
        self.area_preview = tk.Label(janela, text="Selecione uma imagem para começar", bg="#e0e0e0")
        self.area_preview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def carregar_imagem(self):
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
        if caminho:
            self.img_original = Image.open(caminho).convert("RGB")
            self.gerar_preview()

    def gerar_preview(self):
        if self.img_original is None:
            return

        fator = self.fator_var.get()
        # Processa o upscale
        self.img_processada = upscale_vizinho_proximo(self.img_original, fator)

        # Ajusta a imagem do preview apenas para caber na janela sem distorcer
        preview_display = self.img_processada.copy()
        preview_display.thumbnail((500, 400), Image.Resampling.NEAREST)

        # Converte para exibição no Tkinter
        self.imagem_tk = ImageTk.PhotoImage(preview_display)
        self.area_preview.config(image=self.imagem_tk, text="")

    def salvar_imagem(self):
        if self.img_processada is None:
            messagebox.showwarning("Aviso", "Por favor, carregue uma imagem primeiro.")
            return
        
        caminho_salvar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imagem PNG", "*.png")])
        if caminho_salvar:
            self.img_processada.save(caminho_salvar)
            messagebox.showinfo("Sucesso", f"Imagem salva com sucesso!")

# Inicia o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoUpscale(root)
    root.mainloop()
