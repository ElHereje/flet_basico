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
    
ft.app(main)