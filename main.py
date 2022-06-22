#Calculadora para a matéria de LPAR I--------------
from tkinter import * #O '*' significa que importará TODA a bibioteca
import math

root = Tk()
root.title("Calculadora")

#FUNÇÕES
def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))

def click_ponto():
    visor.insert(END, ".")

def click_delete():
    visor.delete(0, END)

def click_soma():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(numero1)
    visor.delete(0, END)

def click_sub():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "subtracao"
    p_numero = float(numero1)
    visor.delete(0, END)

def click_mult():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "multiplicacao"
    p_numero = float(numero1)
    visor.delete(0, END)

def click_div():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "divisao"
    p_numero = float(numero1)
    visor.delete(0, END)

def click_porc():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "porcentagem"
    p_numero = float(numero1)
    visor.delete(0, END)

def click_fatorial():
    numero1 = visor.get()
    global p_numero
    global fatcont
    global matematica
    matematica = "fatorial"
    p_numero = int(numero1)
    fatcont = 1
    while (p_numero>1):
        fatcont = fatcont * p_numero
        p_numero = p_numero - 1
    visor.delete(0, END)

def click_elev2():
    numero1 = visor.get()
    global p_numero
    global resultado
    global matematica
    matematica = "elevado2"
    p_numero = float(numero1)
    resultado = (p_numero**2)
    visor.delete(0, END)

def click_raiz():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "raiz2"
    p_numero = float(numero1)
    visor.delete(0, END)

def click_salvar():
    numero1 = visor.get()
    global p_numero
    global valor
    global matematica
    matematica = "salvar"
    p_numero = float(numero1)
    valor = []
    visor.delete(0, END)

def click_ler():
    numero1 = visor.get()
    global p_numero
    global matematica
    matematica = "ler"
    p_numero = float(numero1)
    visor.delete(0, END)

def igual():
    numero2 = visor.get()
    visor.delete(0, END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(numero2))
    elif matematica == "subtracao":
        visor.insert(0, p_numero - float(numero2))
    elif matematica == "multiplicacao":
        visor.insert(0, p_numero * float(numero2))
    elif matematica == "divisao":
        visor.insert(0, p_numero / float(numero2))
    elif matematica == "porcentagem":
        visor.insert(0, (p_numero*float(numero2)/100))
    elif matematica == "fatorial":
        visor.insert (0, fatcont)
    elif matematica == "elevado2":
        visor.insert(0, resultado)
    elif matematica == "raiz2":
        visor.insert(0, p_numero **(1/2))
    elif matematica == "salvar":
        visor.insert(0, END)
        valor.append = [visor.get()]
    elif matematica == "ler" and click_button == "=":
        visor.insert (0, valor[-1])


#VISOR
visor = Entry(root, background="mistyrose", font= ("arial", 16))
visor.pack(ipadx= 20, ipady=35, fill="both")

#----FILEIRAS DE BOTÕES---------
#fileira 1:
bt7 = Button(root, text= "7", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(7))
bt7.place(x=10, y=100)

bt4 = Button(root, text= "4", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(4))
bt4.place(x=10, y=155)

bt1 = Button(root, text= "1", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(1))
bt1.place(x=10, y=210)

btclear = Button(root, text= "CE", bg="peachpuff", pady=14, padx=10, bd=4, command=click_delete)
btclear.place(x=10, y=265)

btsalvar = Button(root, text= "S", bg="peachpuff", pady=14, padx=14, bd=4, command=click_salvar)
btsalvar.place(x=10, y=320)

#fileira 2:
bt8 = Button(root, text= "8", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(8))
bt8.place(x=60, y=100)

bt5 = Button(root, text= "5", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(5))
bt5.place(x=60, y=155)

bt2 = Button(root, text= "2", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(2))
bt2.place(x=60, y=210)

bt0 = Button(root, text= "0", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(0))
bt0.place(x=60, y=265)

btler = Button(root, text= "L", bg="peachpuff", pady=14, padx=14, bd=4, command=click_ler)
btler.place(x=60, y=320)

#fileira 3:
bt9 = Button(root, text= "9", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(9))
bt9.place(x=110, y=100)

bt6 = Button(root, text= "6", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(6))
bt6.place(x=110, y=155)

bt3 = Button(root, text= "3", bg="lightpink", pady=14, padx=14, bd=4, command= lambda:click_button(3))
bt3.place(x=110, y=210)

btponto = Button(root, text= ".", bg="lightpink", pady=14, padx=16, bd=4, command=click_ponto)
btponto.place(x=110, y=265)

btigual = Button(root, text= "=", bg="tan1", pady=14, padx=14, bd=4, command=igual)
btigual.place(x=110, y=320)

#fileira 4:
btsubtracao = Button(root, text= "-", bg="lightblue", pady=14, padx=14, bd=4, command=click_sub)
btsubtracao.place(x=160, y=100)

btdivisao = Button(root, text= "/", bg="lightblue", pady=14, padx=14, bd=4, command=click_div)
btdivisao.place(x=160, y=155)

btsoma = Button(root, text= "+", bg="lightblue", pady=14, padx=13, bd=4, command=click_soma)
btsoma.place(x=160, y=210)

btmultiplicacao = Button(root, text= "x", bg="lightblue", pady=14, padx=14, bd=4, command=click_mult)
btmultiplicacao.place(x=160, y=265)

btdesligar = Button(root, text= "OFF", bg="lightgreen", pady=14, padx=34, bd=4, command=root.destroy)
btdesligar.place(x=160, y=320)

#fileira 5:
btporcentagem = Button(root, text= "%", bg="lightblue", pady=14, padx=14, bd=4, command=click_porc) #tem que apertar primeiro o botao e depois o numero
btporcentagem.place(x=210, y=100)

btelevadodois = Button(root, text="x²", bg="lightblue", pady=14, padx=14, bd=4, command=click_elev2)
btelevadodois.place(x=210, y=155)

btraiz = Button(root, text= "√", bg="lightblue", pady=14, padx=15, bd=4, command=click_raiz)
btraiz.place(x=210, y=210)

btfatoracao = Button(root, text= "n!", bg="lightblue", pady=14, padx=14, bd=4, command=click_fatorial)
btfatoracao.place(x=210, y=265)

#Dimensões
root.resizable(False, False) #Usuario não poderá redimensionar a tela
root.geometry("280x380")
root.mainloop() #para funcionar