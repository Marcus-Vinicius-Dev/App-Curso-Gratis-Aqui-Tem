import flet as ft

def main(page: ft.Page):
    page.title="Cursos Grátis Aqui Tem APP"
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
        padding=ft.padding.all(10),
        aspect_ratio=9/16,
        content=ft.Column(
            
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
        padding=ft.padding.all(14),
        aspect_ratio=9/16,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value='CURSOS GRÁTIS AQUI TEM!',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                    size=22,
                ),
                ft.Text(
                    value='Selecione a opção para Visualizar',
                    color=ft.colors.WHITE,
                    size=20,
                ),
                
                ft.Container(
                    margin=ft.margin.Margin(top=30,left=0, right=0, bottom=0)),
                
                ft.ResponsiveRow(
                    columns=12,
                    controls=[ 
                        ft.Dropdown(
                            col=6,
                            label='Cursos',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=20),
                            border_color=ft.colors.AMBER_300,
                            border_width=0.5,
                            text_size=16,
                            height=80,
                            options=[
                                ft.dropdown.Option(text='CULINÁRIA'),
                                ft.dropdown.Option(text='TECNOLOGIA'),
                                ft.dropdown.Option(text='ARTES'),
                                ft.dropdown.Option(text='DANÇA'),
                                ft.dropdown.Option(text='DIREITO'),
                                ft.dropdown.Option(text='ADMINISTRAÇÃO'),
                            ]
                        ),
                        ft.Dropdown(
                            col=6,
                            label='Instituição',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=20),
                            border_color=ft.colors.AMBER_300,
                            border_width=0.5,
                            text_size=16,
                            height=80,
                            options=[
                                ft.dropdown.Option(text='UNIVESP'),
                                ft.dropdown.Option(text='UNIFESP'),
                                ft.dropdown.Option(text='CEU Curuçá'),
                                ft.dropdown.Option(text='USP'),
                                ft.dropdown.Option(text='UNICAMP'),
                                ft.dropdown.Option(text='UNESP'),
                            ]
                        )
                    ]
                ),
                
                ft.Container(
                    margin=ft.margin.Margin(top=30,left=0, right=0, bottom=0)),
                
                ft.Text(
                    value='Avalie o curso',
                    color=ft.colors.WHITE,
                    italic=True,
                    size=20,
                ), 
                
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
                
                ft.Container(
                    margin=ft.margin.Margin(top=0,left=0, right=0, bottom=30)),
                
                ft.Tabs(
                    selected_index=0,
                    height=200,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(20),
                                content=ft.Text(
                                    value='Bacharel em Tecnologia da Informação',
                                    color=ft.colors.WHITE,
                                    size=20,
                                )
                            ),
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(20),
                                content=ft.Text(
                                    value='Curso de TIC com ênfase em Django e Python além de lógica de programação',
                                    color=ft.colors.WHITE,
                                    size=20,
                                )
                            ),
                        ),
                        
                    ]
                ),
                
                ft.Container(
                    margin=ft.margin.Margin(top=0,left=0, right=0, bottom=10)),
                
                ft.ElevatedButton(
                    width=300,
                    content=ft.Text(
                        value='CADASTRAR',
                        #color=ft.colors.WHITE,
                        size=20,
                    ),
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(16),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE),
                            ft.MaterialState.HOVERED: ft.BorderSide(width=2, color=ft.colors.AMBER),
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.CYAN_900,
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.AMBER,
                            ft.MaterialState.HOVERED: ft.colors.WHITE,
                        }
                    )
                )
            ]
        )
    )
    
    layout = ft.Container(
        #width=900,
        margin=ft.margin.Margin(top=30,left=0, right=0, bottom=0),
        
        shadow=ft.BoxShadow(blur_radius=990, color=ft.colors.CYAN_900),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                #product_images,
                product_details
            ]
        )
    )
    
    page.add(layout)
    
if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)