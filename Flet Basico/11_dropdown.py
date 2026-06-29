import flet as ft

def main(page:ft.Page):
    #------ Configuracion de la aplicación---------
    page.title = "Dropdown"
    page.window.height = 500
    page.window.width = 500
    page.window.resizable = False
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'light'
    #----------------------------------------
    
    def changeColor(e):
        t1.value = f"El valor del Dropdown es {d1.value}"
        page.update()

    d1 = ft.Dropdown(
            label="Colores",
            hint_text="Selecciona color",
            options=[
                ft.dropdown.Option("Azul"),
                ft.dropdown.Option("Rojo"),
                ft.dropdown.Option("Verde"),
                ft.dropdown.Option("Amarillo")
            ],
            on_text_change=changeColor,
            border=ft.InputBorder.UNDERLINE,
            border_color='orange',
            label_style=ft.TextStyle(color='red')
        )
    
    t1 = ft.Text(f"El valor del Dropdown es {d1.value}")

    page.add(
        d1,
        t1
    )
    
#ejecuta la aplicación
ft.app(main)