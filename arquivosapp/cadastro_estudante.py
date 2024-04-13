import flet as ft
import requests

def get_estudante():
    response = requests.get("http://127.0.0.1:8000/cursos/estudante/")
    return response.json()

def main(page: ft.Page):    
    page.title="Cadastrar Estudante"
    
    lista_estudantes = ft.ListView()
    
    def cadastrar(e):
        data = {
            'nome': nome.value,
            'sobrenome': sobrenome.value,
            #'nascimento': data_nascimento.value,
            'telefone': telefone.value,
            'email': email.value,
            'sexo': sexo.value
        }
        
        response = requests.post("http://127.0.0.1:8000/cursos/estudante/", json=data)
        
        if response.status_code == 200:
            lista_estudantes.controls.append(
                ft.Container(
                    ft.Text(nome.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                )
            )
            
            page.update()
    
    txt_erro = ft.Container(ft.Text('Erro ao cadastrar Estudante!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_exito =  ft.Container(ft.Text('Estudante cadastrado com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    
    page.add(
        txt_erro,
        txt_exito,
        lista_estudantes,
    )
    
    ft.Container()
    txt_nome=ft.Text('Nome:', color=ft.colors.AMBER)
    nome=ft.TextField(    
        #label="Digite o Nome...", 
        text_align=ft.TextAlign.LEFT,    
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.AMBER)
        
    txt_sobrenome=ft.Text('Sobrenome:', color=ft.colors.AMBER)
    sobrenome=ft.TextField(
        #label="Digite o Sobrenome...", 
        text_align=ft.TextAlign.LEFT,    
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.AMBER)
        
    #txt_datanasc=ft.Text('Data nascimento:', color=ft.colors.AMBER)
    #data_nascimento=ft.TextField(
        #label="Selecione a data de Nascimento...", 
        #text_align=ft.TextAlign.LEFT,
        #border=ft.InputBorder.UNDERLINE,
        #border_color=ft.colors.AMBER,
        #)    
    
    txt_telefone=ft.Text('Telefone:', color=ft.colors.AMBER)
    telefone=ft.TextField(
        #label="Digite o Telefone...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.AMBER)
    
    txt_email=ft.Text('E-mail:', color=ft.colors.AMBER)
    email=ft.TextField(
        #label="Digito o E-mail...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.AMBER)
    
    txt_sexo=ft.Text('Sexo:',color=ft.colors.AMBER)
    sexo=ft.TextField(
        #label="Sexo...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.AMBER)
    
    btn_estudante=ft.ElevatedButton('CADASTRAR', on_click=cadastrar)
    
    page.add(
        txt_nome,
        nome,
        txt_sobrenome,
        sobrenome,
        #txt_datanasc,
        #data_nascimento,
        txt_telefone,
        telefone,
        txt_email,
        email,
        txt_sexo,
        sexo,
        btn_estudante
    )
        
    page.add(
        lista_estudantes,
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)