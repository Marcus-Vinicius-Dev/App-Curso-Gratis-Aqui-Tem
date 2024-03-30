import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.AUTO
    
    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity=1
                main_image.src=elem.image_src
            else:
                elem.opacity=0.5
                
        main_image.update()
        options.update()
    
    product_images=ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='../app/img/artes.jpg',
                    width=500,
                    height=500,
                ),
                
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='../app/img/esportes.jpg',
                            width=90,
                            height=90,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='../app/img/negocios.jpg',
                            width=90,
                            height=90,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='../app/img/tecnologia.jpg',
                            width=90,
                            height=90,
                            opacity=1,
                            on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )
    product_details=ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value='CURSOS GRÁTIS AQUI TEM!',
                    color=ft.colors.AMBER,
                    #weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Selecione um Curso para Visualizar',
                    color=ft.colors.WHITE,
                    #weight=ft.FontWeight.BOLD,
                    size=14,
                ),
                
                ##########
                ft.Container(expand=True),
                
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Cursos',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Culinária'),
                                ft.dropdown.Option(text='Tecnologia'),
                                ft.dropdown.Option(text='Artes'),
                            ]
                        ),
                        ft.Dropdown(
                            col=6,
                            label='Instituição',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='UNIVESP'),
                                ft.dropdown.Option(text='UNIFESP'),
                                ft.dropdown.Option(text='CEU Curuçá'),
                            ]
                        )
                    ]
                ),
                
                ##########
                ft.Container(expand=True),
                
                ft.Text(
                    value='Avalie o curso',
                    color=ft.colors.GREY,
                    italic=True,
                ), 
                
                ##########
                #ft.Container(expand=True),
                
                ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.CENTER,
                    columns=12,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            col={'xs': 12, 'sm': 6},
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 2 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]  
                ),
                
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Bacharel em Tecnologia da Informação',
                                    color=ft.colors.GREY,
                                )
                            ),
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Curso de TIC com ênfase em Django e Python além de lógica de programação',
                                    color=ft.colors.GREY,
                                )
                            ),
                        ),
                        
                    ]
                ),
                ft.Container(expand=True),
                
                ft.ElevatedButton(
                    width=900,
                    text='Cadastrar',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE),
                            ft.MaterialState.HOVERED: ft.BorderSide(width=2, color=ft.colors.CYAN),
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.WHITE
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        }
                    )
                )
            ]
        )
    )
    
    layout = ft.Container(
        width=900,
        margin=ft.margin.all(0),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )
    
    page.add(layout)
    
if __name__ == '__main__':
    ft.app(target=main)