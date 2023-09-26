class pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade= idade
        self.comendo  = comendo
        self.falando = falando

    
    def comer(self, alimento): #Aqui agente vai pedir para a pessoa comer
        if self.comendo:
            print(f"Desculpe, mas {self.nome} ja esta comendo!")
            return 
        #Nesse caso como o atributo la em cima  esta como "False" o Python ira ler o proximo comando aqui de baixo, se caso eu pedir novamente para ele comer ele vai ver que o estatus desse atributo agora estara como "True", entao e;ele printara essa mensagem "que ja esta comendo..."   

        print(f"{self.nome} esta comendo {alimento}")
        self.comendo = True #Como eu disse que ele esta comendo eu irei mudar o status "comendo"

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} nao esta mais comendo!")
            return
    
        print(f"{self.nome} Ja parou de comer!")
        self.comendo = False

        
