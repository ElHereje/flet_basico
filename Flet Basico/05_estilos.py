import flet as ft

def main(page:ft.Page):
    #------ Configuracion de la aplicación---------
    page.title = "Ventana"
    page.window.height = 500
    page.window.width = 500
    page.window.resizable = False
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'light'
    page.theme = ft.Theme(
        color_scheme_seed='#247f4c',
        font_family='Comic Sans Ms',
    )
    #----------------------------------------
    
#ejecuta la aplicación
ft.app(main)