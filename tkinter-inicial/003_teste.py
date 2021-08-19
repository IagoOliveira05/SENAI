from tkinter import *

class Tela:
    def __init__(self):
        self.root = root
        self.configura_tela()
        self.widgets()
        root.mainloop()


    def configura_tela(self):
        self.root.configure(bg='#2A2A72')
        self.root.geometry('375x667+600+15')        # dimensão, posição em Y, distância do topo da tela
        

    def widgets(self):
        ola = Label(
            self.root,
            text='Hello World!',
            font=('times', 30, 'bold'),
            bg='#2A2A72',
            fg='#FFA400'
            )
        ola.place(x=50, y=100, height=50, width=300)      #.pack()→ Centraliza no meio    .grid()→ Divide a tela em coluna e linhas     .place()→ Você passa as coordenas

        self.btn_confirma = Button(
            self.root,
            text='CLIQUE',
            bg='#FFA400',
            command=self.clica
        )
        self.btn_confirma.place(x=130, y=150, height=30, width=150)

        self.btn_fecha = Button(
            self.root,
            text='X',
            bg='red',
            command=self.fechar
        )
        self.btn_fecha.place(x=10, y=10, height=30, width=30)


    def clica(self):
        texto = Label(
            self.root,
            text='Eu amo ester e ana!',
            font=('times', 25, 'bold'),
            bg='#2A2A72',
            fg='#FFA400'
            )
        texto.place(x=50, y=250, height=50, width=300)
    
    
    def fechar(self):
        self.root.destroy()

root = Tk()
Tela()
