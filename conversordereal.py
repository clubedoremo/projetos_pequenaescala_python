import requests

class usuario:
    def __init__(self, escolher):
        self.escolha = escolher
        self.taxa_dolar = 0
        self.taxa_euro = 0
        self.taxa_real = 0 

    def escolher(self):
        

      while True: 

        if self.escolha == "dolar":
               self.buscar_taxaDOLAR()
               self.converterDOLAR()
               break

        elif self.escolha == "euro":
            self.buscar_taxaEURO()
            self.converterEURO()
            break

        elif self.escolha == "real":
            self.buscar_taxaBR()
            self.converterREAL()
            break


        elif self.escolha == ".":
           print("OBRIGADO POR USAR NOSSA CALCULADORA")
           break


    def buscar_taxaBR(self):
        url = "https://api.fastforex.io/fetch-multi"

        params = {

            "from" : "BRL",
            "to" : "USD, EUR",
            "api_key": "0e2a141fd5-d9352684cf-swk8x1" 
           }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            dados = response.json()
            self.taxa_dolar = dados['results']['USD'] 
            self.taxa_euro = dados['results']['EUR'] 
        else:
            print("Erro ao buscar taxas da API.")

    def buscar_taxaDOLAR(self):
        url = "https://api.fastforex.io/fetch-multi"

        params = {

            "from" : "USD",
            "to" : "BRL, EUR",
            "api_key": "0e2a141fd5-d9352684cf-swk8x1" 
           }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            dados = response.json()
            self.taxa_real = dados['results']['BRL'] 
            self.taxa_euro = dados['results']['EUR'] 
        else:
            print("Erro ao buscar taxas da API.")
             
    def buscar_taxaEURO(self):
        url = "https://api.fastforex.io/fetch-multi"

        params = {

            "from" : "EUR",
            "to" : "USD, BRL",
            "api_key": "0e2a141fd5-d9352684cf-swk8x1" 
           }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            dados = response.json()
            self.taxa_dolar = dados['results']['USD'] 
            self.taxa_real = dados['results']['BRL'] 
        else:
            print("Erro ao buscar taxas da API.")             

    def converterREAL(self):
          valor = int(input("Insira um valor: "))
          dolar = valor * self.taxa_dolar
          euro = valor * self.taxa_euro
          print(f'o valor em dolar é: {dolar}')
          print(f'o valor em euro é: {euro}')
          print(f'o valor em real que você inseriu é: {valor}')
    
    def converterDOLAR(self):
          valor = int(input("Insira um valor: "))
          real = valor * self.taxa_real
          euro = valor * self.taxa_euro
          print(f'o valor em real é: {real}')
          print(f'o valor em euro é: {euro}')
          print(f'o valor em dolár que você inseriu é: {valor}')

    def converterEURO(self):
          valor = int(input("Insira um valor: "))
          real = valor * self.taxa_real
          dolar = valor * self.taxa_dolar
          print(f'o valor em real é: {real}')
          print(f'o valor em dolar é: {dolar}')
          print(f'o valor em euro que você inseriu é: {valor}')


teste = usuario((input('Selecione uma moeda (dolar, euro, real): ')))

teste.escolher()
