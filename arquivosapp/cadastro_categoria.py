import flet as ft
import requests

def get_categoria():
    response = requests.get("http://127.0.0.1:8000/cursos/categoria/")
    return response.json()

def  main(page: ft.Page):
    
    page.title="Cadastrar Categoria"
    
    lista_categoria = ft.ListView()
    
    def cadastrar(e):
        data = {
            'nome': nome.value,
        }
        
        response = requests.post("http://127.0.0.1:8000/cursos/categoria/", json=data)
        
        if response.status_code == 200:
            lista_categoria.controls.append(
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
    
    txt_erro = ft.Container(ft.Text('Erro ao cadastrar Categoria!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_exito =  ft.Container(ft.Text('Categoria cadastrada com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    
    page.add(
        txt_erro,
        txt_exito,
        lista_categoria,
    )
    
    ft.Container()
    txt_nome=ft.Text('Nome:', color=ft.colors.AMBER)
    nome=ft.TextField(    
        label="Digite uma Categoria...", 
        text_align=ft.TextAlign.LEFT, 
        border=ft.InputBorder.UNDERLINE,   
        border_color=ft.colors.AMBER)
    
    btn_categoria=ft.ElevatedButton('CADASTRAR', on_click=cadastrar)
    
    page.add(
        txt_nome,
        nome,
        btn_categoria,
    )
        
    page.add(
        lista_categoria,
    )
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER)