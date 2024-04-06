from tkinter import *
import os 
from tkinter.filedialog import askdirectory

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Hello World!")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Selecionar Pastas"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.caixaSelec)
        self.sair.pack ()
  
    def caixaSelec(self, event):
        caminho = askdirectory(title="selecione uma pasta")
        listaArquivos = os.listdir(caminho)
        print(listaArquivos)

        locais = {
            "imagens": [".png",".jpg"],
            "planilhas": [".csv",".xlsx"],
            "PDFs": [".pdf"],
            "textos": [".txt",".doc"],            
        }

        for arquivo in listaArquivos: 
            nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
            for pasta in locais: 
                if extensao in locais[pasta]:
                    if not os.path.exists(f'{caminho}/{pasta}'):
                        os.mkdir(f'{caminho}/{pasta}')
                    os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')    

root = Tk()
Application(root)
root.mainloop()