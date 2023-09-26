class pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade= idade
        self.comendo  = comendo
        self.falando = falando


    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} nao pode falar pois esta COMENDO!")
            return
        
        if self.falando:
            print(f"{self.nome} ja esta FALANDO!")
            return
        
        print(f"{self.nome} esta falando sobre {assunto}!")
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} nao esta falando!")
            return
        
        print(f"{self.nome} parou de falar!")
        self.falando = False


    
    def comer(self, alimento): #Aqui agente vai pedir para a pessoa comer
        if self.comendo:
            print(f"Desculpe, mas {self.nome} ja esta comendo!")
            return 
        #Nesse caso como o atributo la em cima  esta como "False" o Python ira ler o proximo comando aqui de baixo, se caso eu pedir novamente para ele comer ele vai ver que o estatus desse atributo agora estara como "True", entao e;ele printara essa mensagem "que ja esta comendo..."  

        if self.falando:
            print(f"{self.nome} nao pode comer falando!")
            return 

        print(f"{self.nome} esta comendo {alimento}")
        self.comendo = True #Como eu disse que ele esta comendo eu irei mudar o status "comendo"

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} nao esta mais comendo!")
            return
    
        print(f"{self.nome} Ja parou de comer!")
        self.comendo = False

        
