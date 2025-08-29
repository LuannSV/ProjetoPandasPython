from gui import *
import backend as core

app = Gui()  # ← você esqueceu de instanciar a classe GUI corretamente

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(
        app.txtNome.get(),
        app.txtSobreNome.get(),
        app.txtEmail.get(),
        app.txtCPF.get()
    )
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(
        app.txtNome.get(),
        app.txtSobreNome.get(),
        app.txtEmail.get(),
        app.txtCPF.get()
    )
    view_command()  # ← opcional: para atualizar a lista após inserir

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
