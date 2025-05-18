import tkinter as tk
from tkinter import messagebox, simpledialog

class Usuario:
    def __init__(self, escolha):
        self.escolha = escolha
        self.valor_mutante = 0

    def escolher(self):
        root = tk.Tk()
        root.withdraw()  

        while True:
            if self.escolha == "+":
                if self.valor_mutante == 0:
                    self.adicionar()
                else:
                    self.adicionarmutante()
            elif self.escolha == "-":
                if self.valor_mutante == 0:
                    self.subtrair()
                else:
                    self.subtrairmutante()
            elif self.escolha == "*":
                if self.valor_mutante == 0:
                    self.multiplicar()
                else:
                    self.multiplicarmutante()
            elif self.escolha == "/":
                if self.valor_mutante == 0:
                    self.dividir()
                else:
                    self.dividirmutante()
            elif self.escolha == ".":
                messagebox.showinfo("Fim", "Obrigado por usar a calculadora!")
                break
            else:
                messagebox.showwarning("Operação inválida", "Digite uma operação válida.")

            self.escolha = simpledialog.askstring("Operação", "Digite a operação (+, -, *, /, . para sair):")

    def adicionar(self):
        try:
            valor1 = int(simpledialog.askstring("Adição", "Digite o primeiro número:"))
            valor2 = int(simpledialog.askstring("Adição", "Digite o segundo número:"))
            self.valor_mutante = valor1 + valor2
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except:
            messagebox.showerror("Erro", "Insira números válidos.")
            self.adicionar()

    def adicionarmutante(self):
        try:
            valor = int(simpledialog.askstring("Adição", "Digite o número para somar:"))
            self.valor_mutante += valor
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except:
            messagebox.showerror("Erro", "Número inválido.")
            self.adicionarmutante()

    def subtrair(self):
        try:
            valor1 = int(simpledialog.askstring("Subtração", "Digite o primeiro número:"))
            valor2 = int(simpledialog.askstring("Subtração", "Digite o segundo número:"))
            self.valor_mutante = valor1 - valor2
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except:
            messagebox.showerror("Erro", "Insira números válidos.")
            self.subtrair()

    def subtrairmutante(self):
        try:
            valor = int(simpledialog.askstring("Subtração", "Digite o número para subtrair:"))
            self.valor_mutante -= valor
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except:
            messagebox.showerror("Erro", "Número inválido.")
            self.subtrairmutante()

    def multiplicar(self):
        try:
            valor1 = int(simpledialog.askstring("Multiplicação", "Digite o primeiro número:"))
            valor2 = int(simpledialog.askstring("Multiplicação", "Digite o segundo número:"))
            self.valor_mutante = valor1 * valor2
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except:
            messagebox.showerror("Erro", "Número inválido.")
            self.multiplicar()

    def multiplicarmutante(self):
        try:
            valor = int(simpledialog.askstring("Multiplicação", "Digite o número para multiplicar:"))
            self.valor_mutante *= valor
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except:
            messagebox.showerror("Erro", "Número inválido.")
            self.multiplicarmutante()

    def dividir(self):
        try:
            valor1 = int(simpledialog.askstring("Divisão", "Digite o dividendo:"))
            valor2 = int(simpledialog.askstring("Divisão", "Digite o divisor:"))
            self.valor_mutante = valor1 / valor2
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
            self.dividir()
        except:
            messagebox.showerror("Erro", "Número inválido.")
            self.dividir()

    def dividirmutante(self):
        try:
            valor = int(simpledialog.askstring("Divisão", "Digite o número para dividir:"))
            self.valor_mutante /= valor
            messagebox.showinfo("Resultado", f"Resultado: {self.valor_mutante}")
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
            self.dividirmutante()
        except:
            messagebox.showerror("Erro", "Número inválido.")
            self.dividirmutante()


# Início da calculadora
escolha_inicial = simpledialog.askstring("Operação", "Digite a operação (+, -, *, /, . para sair):")
usuario = Usuario(escolha_inicial)
usuario.escolher()
