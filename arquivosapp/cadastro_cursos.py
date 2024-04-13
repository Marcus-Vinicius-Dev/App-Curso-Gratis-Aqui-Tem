import flet as ft
import requests

def get_instituicao():
    response=requests.get("http://127.0.0.1:8000/cursos/instituicao/")
    return response.json()

def get_categoria():
    response=requests.get("http://127.0.0.1:8000/cursos/categoria/")
    return response.json()

def get_id_categoria(nome):
    for i in get_categoria():
        if i['nome'] == nome:
            return i['id']

def get_id_instituicao(nome):
    for i in get_instituicao():
        if i['nome'] == nome:
            return i['id']

def  main(page: ft.Page):
    page.title="Cadastrar Cursos"
    
    lista_cursos=ft.ListView()
    
    def cadastrar(e):
        data = {
            'nome_curso': nome.value,
            'descr_curso': descricao.value,
            'inscricao': inscricao.value,
            'categoria': get_id_categoria(categoria.value),
            'instituição': get_id_instituicao(instituicao.value)
        }
        
        response=requests.post("http://127.0.0.1:8000/cursos/cursos/", json=data)
        
        if response.status_code == 200:
            lista_cursos.controls.append(
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
    
    txt_erro=ft.Container(ft.Text('Erro ao cadastrar Curso!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_exito=ft.Container(ft.Text('Curso cadastrado com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    
    page.add(
        txt_erro,
        txt_exito,
        lista_cursos,
    )
    
    '''Menus Dropdow'''
    ft.Container()
    txt_categoria=ft.Text('Categoria:',color=ft.colors.AMBER)
    categoria=ft.Dropdown(
        options=[
            ft.dropdown.Option(i['nome']) for i in get_categoria()
        ]
    )
    
    txt_instituicao=ft.Text('Instituição:',color=ft.colors.AMBER)
    instituicao=ft.Dropdown(
        options=[
            ft.dropdown.Option(i['nome']) for i in get_instituicao()
        ]
    )
    
    txt_titulo=ft.Text('Título Curso:',color=ft.colors.AMBER)
    nome=ft.TextField(    
        label="Digite o título do Curso...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
        
    txt_descricao=ft.Text('Descrição do Curso:', color=ft.colors.AMBER)
    descricao=ft.TextField(
        label="Digite uma breve descrição do Curso...", 
        text_align=ft.TextAlign.LEFT,   
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.AMBER)
        
    txt_datainscricao=ft.Text('Data para inscrição:',color=ft.colors.AMBER)
    inscricao=ft.TextField(
        label="Selecione a data para inscrição...", 
        text_align=ft.TextAlign.LEFT,    
        border_color=ft.colors.AMBER)
    
    btn_curso=ft.ElevatedButton('CADASTRAR', on_click=cadastrar)
    
    page.add(
        txt_categoria,
        categoria,
        txt_instituicao,
        instituicao,
        txt_titulo,
        nome,
        txt_descricao,
        descricao,
        txt_datainscricao,        
        inscricao,
        btn_curso,
        lista_cursos
    )
    
    page.add(
        lista_cursos,
    )
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER)