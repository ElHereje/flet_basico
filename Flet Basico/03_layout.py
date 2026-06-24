import flet as ft

def main(page:ft.Page):
    # caracterist. de la pag
    page.title = "Ventana"
    page.window.height = 500
    page.window.width = 500
    page.window.resizable = False
    page.bgcolor = 'white'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    
    #---------------------------------
    
    page.add( # de arriba a abajo
        ft.Row( #añado componentes en fila
            expand=True,
            controls=[
                # añadimos un contenedor independiente
                ft.Container(
                    expand = True,
                    alignment=ft.Alignment(0,0),
                    bgcolor=ft.Colors.RED,
                    content=ft.Text("Etiqueta 1", color = 'black')
                ),
                ft.Container(
                    alignment=ft.Alignment(0,0),
                    bgcolor=ft.Colors.RED,
                    content=ft.Text("Etiqueta 1", color = 'black')
                )
            ]   
        ),
        ft.Column( # añado componentes en columnas
            expand=True,
            controls=[
                # añadimos un contenedor independiente
                ft.Container(
                    expand = True,
                    alignment=ft.Alignment(0,0),
                    bgcolor=ft.Colors.AMBER,
                    content=ft.Text("Etiqueta 1", color = 'black')
                ),
                ft.Container(
                    alignment=ft.Alignment(0,0),
                    bgcolor=ft.Colors.AMBER,
                    content=ft.Text("Etiqueta 1", color = 'black')
                )
            ]   
        )
    )

# inicio de la aplicación
ft.app(main)