import flet as ft

def  main(page: ft.Page):
    page.title="Login"
    
    #main_image.update()

    ft.Container(margin=ft.margin.Margin(top=50,left=0, right=0, bottom=0),
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(10),
        aspect_ratio=9/16,
        content=ft.Column(
            width=500,
            height=500,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        
            #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            #controls=[
                #main_image := ft.Image(
                    #src='../app/img/artes.jpg',
                    #width=500,
                    #height=500,
                #),
                    
                #ft.Text(
                #    height=200,
                #    value="Login",
                #    color=ft.colors.AMBER,
                #    size=20,
                #),
            #]
        )
    )
        
    ft.Row(
        controls=[
            ft.Container(
                expand=1,
                content=ft.Text("Login"),
                bgcolor=ft.colors.GREEN_100,
            ),
            ft.Container(
                expand=2, content=ft.Text("Container 2"), bgcolor=ft.colors.RED_100
            ),
        ],
    ),
        
        
    layout = ft.Container(
        width=900,
        margin=ft.margin.Margin(top=30,left=0, right=0, bottom=0),
        
        shadow=ft.BoxShadow(blur_radius=900, color=ft.colors.CYAN_900),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            #controls=[
                #product_images,
                #product_details
            #]
        )
    )
    
    page.add(layout)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)