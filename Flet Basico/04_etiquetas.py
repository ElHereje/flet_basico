import flet as ft

def main(page:ft.Page):
    #------ Configuracion de ventana---------
    page.title = "Ventana"
    page.window.height = 500
    page.window.width = 500
    page.window.resizable = False
    page.bgcolor = 'white'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    #----------------------------------------
    
    estilo_text = ft.TextStyle(
            color='#000000',# 'black'
            font_family='Times new Roman',
            bgcolor='red',
            size=24,
            italic= False,
            weight=ft.FontWeight.BOLD
    )
    page.add(
        ft.Text(
            value = "IMAD con stile_text",
            style=estilo_text
        ),
        ft.Text("Imad", italic=True, size=40),
        ft.Text(
            "HOLA", 
            italic=True, 
            size=40, 
            selectable=True, 
            color='blue')
    )

# inicio de la aplicación
ft.app(main)