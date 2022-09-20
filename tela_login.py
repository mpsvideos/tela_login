# Praticando Python - Tela Login
# Marley Paranhos - Iniciante na programaçao
# Precisando de ajuda pra entender validaçao de dados

from tkinter import *
from tkinter import messagebox


def cadastro():
    lista_cadastro = []
    usuario = e_usuario.get()
    senha = e_senha.get()
    lista_cadastro.append(usuario)
    lista_cadastro.append(senha)

    if usuario == '' or senha == '':
        messagebox.showerror('Erro', 'Preencha todos os campos.')
        return
    messagebox.showinfo('Sucesso!', 'Login salvo com sucesso!')
    print(lista_cadastro)


def login():
    lista = []
    usuario = e_usuario.get()
    senha = e_senha.get()
    lista.append(usuario)
    lista.append(senha)
    if usuario == '' and senha == '':
        messagebox.showerror('Erro', 'Preencha todos os campos.')
        return
    if usuario == lista[0] and senha == lista[1]:
        messagebox.showinfo('Acesso', 'Acesso concedido!')
        return
    messagebox.showerror('Erro', 'Dados incorretos.')
    print(lista)


janela = Tk()
janela.title('Tela Login - V-1.0')
janela.geometry('450x200')
janela.iconbitmap('icone.ico')

logo = PhotoImage(file='login.png')

f_frame_esquerdo = Frame(janela, width=200, height=200)
f_frame_esquerdo.grid(row=0, column=0)
l_frame_esquerdo = Label(f_frame_esquerdo, image=logo)
l_frame_esquerdo.place(x=40, y=30)

f_frame_direito = Frame(janela, width=400, height=200)
f_frame_direito.grid(row=0, column=1)
l_frame_direito = Label(f_frame_direito, text='LOGIN DE ACESSO', font=('Ivy 13 bold'), justify=CENTER, compound=CENTER)
l_frame_direito.place(x=10, y=10)

l_usuario = Label(f_frame_direito, text='Usuário', font=('Ivy 12'))
l_usuario.place(x=10, y=70)
e_usuario = Entry(f_frame_direito)
e_usuario.place(x=80, y=70)

l_senha = Label(f_frame_direito, text='Senha', font=('Ivy 12'))
l_senha.place(x=10, y=110)
e_senha = Entry(f_frame_direito, show='*')
e_senha.place(x=80, y=110)

b_login = Button(f_frame_direito, text='LOGIN', font=('Ivy 10 bold'), anchor=CENTER, compound=CENTER,
               width=10, overrelief=RIDGE, justify=LEFT, relief=SOLID, command=login)
b_login.place(x=30, y=150)

b_cadastrar = Button(f_frame_direito, text='SALVAR', font=('Ivy 10 bold'), anchor=CENTER, compound=CENTER,
               width=10, overrelief=RIDGE, justify=LEFT, relief=SOLID, command=cadastro)
b_cadastrar.place(x=130, y=150)

janela.mainloop()
