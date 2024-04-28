from django.shortcuts import render
from django.http import HttpResponse
import flet as ft

def home(request):
    # Aqui você pode chamar a função main do seu aplicativo Flet
    # e gerar o conteúdo HTML necessário para renderizar a página.
    # Por exemplo:
    page = ft.Page()
    main(page) # Supondo que main seja a função do seu aplicativo Flet
    html_content = page.render() # Supondo que page.render() retorne o HTML gerado

    return HttpResponse(html_content)

def main(page):
    # Exemplo de uso do Flet para adicionar conteúdo à página
    page.add_text("Bem-vindo à página inicial!")
    # Adicione mais conteúdo conforme necessário
