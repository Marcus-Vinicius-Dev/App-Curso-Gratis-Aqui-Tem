import flet as ft
import requests

def get_instituicao():
    response = requests.get('http://127.0.0.1:8000/cursos/instituicao/')
    return response.json()

def  main(page: ft.Page):
    
    page.title="Cadastrar Instituição"
    
    lista_instituicao = ft.ListView()
    
    def cadastrar(e):
        data = {
            'nome': nome.value,
            'cep': cep.value,
            'endereco': endereco.value,
            'cidade': cidade.value,
            'uf': uf.value,
            'telefone': telefone.value,
            'email': email.value,
            'site': site.value,
        }
        
        response = requests.post('http://127.0.0.1:8000/cursos/instituicao/', json=data)
        
        if response.status_code == 200:
            lista_instituicao.controls.append(
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
    
    txt_erro = ft.Container(ft.Text('Erro ao cadastrar Instituição!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_exito =  ft.Container(ft.Text('Instituição cadastrada com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    
    page.add(
        txt_erro,
        txt_exito,
        lista_instituicao,
    )
    
    ft.Container()
    txt_nome=ft.Text('Nome:',color=ft.colors.AMBER)
    nome=ft.TextField(    
        label="Digite o nome da instituição...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
        
    txt_cep=ft.Text('CEP:',color=ft.colors.AMBER)
    cep=ft.TextField(
        label="CEP...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    txt_endereco=ft.Text('Endereço:',color=ft.colors.AMBER)
    endereco=ft.TextField(
        label="Rua, Av, Logradouro...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    txt_cidade=ft.Text('Cidade:',color=ft.colors.AMBER)
    cidade=ft.TextField(
        label="Cidade...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    txt_uf=ft.Text('UF:',color=ft.colors.AMBER)
    uf=ft.TextField(
        label="UF...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    txt_telefone=ft.Text('Telefone:',color=ft.colors.AMBER)
    telefone=ft.TextField(
        label="Telefone...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    txt_email=ft.Text('E-mail:',color=ft.colors.AMBER)
    email=ft.TextField(
        label="E-mail...", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    txt_site=ft.Text('Site:',color=ft.colors.AMBER)
    site=ft.TextField(
        prefix_text="https://",
        label="Digite o Site..", 
        text_align=ft.TextAlign.LEFT,
        border=ft.InputBorder.UNDERLINE,    
        border_color=ft.colors.AMBER)
    
    btn_instituicao=ft.ElevatedButton('CADASTRAR', on_click=cadastrar)
    
    page.add(
        txt_nome,
        nome,
        txt_cep,
        cep,
        txt_endereco,
        endereco,
        txt_cidade,
        cidade,
        txt_uf,
        uf,
        txt_telefone,
        telefone,
        txt_email,
        email,
        txt_site,
        site,
        btn_instituicao
    )
        
    page.add(
        lista_instituicao,
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)