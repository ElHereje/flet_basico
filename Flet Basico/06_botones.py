import flet as ft

def main(page:ft.Page):
    #------ Configuracion de la aplicación---------
    page.title = "Ventana"
    page.window.height = 500
    page.window.width = 500
    page.window.resizable = False
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'dark'
    #----------------------------------------
    
    def funcion_ejemplo(e):
        print("Texto")
    
    page.add(
        # Se añaden botones por jerarquia----
        ft.ElevatedButton("ElevatedButton",
                          on_click=funcion_ejemplo),
        ft.Button("Button", bgcolor='red',
                  on_click=lambda e: print("Texto")),
        ft.FilledButton("FilledButton"),
        ft.FilledTonalButton("FilledTonalButton"),
        ft.OutlinedButton("OutlinedButton"),
        ft.TextButton("TextButton"),
        ft.FloatingActionButton("FloatingActionButton", icon=ft.Icons.ADD),
        ft.IconButton(icon=ft.Icons.HOME), #solo iconos
        ft.PopupMenuButton(
            icon=ft.Icons.DO_NOT_TOUCH,
            items=[
                ft.PopupMenuItem("boton 1"),
                ft.PopupMenuItem("boton 2")
            ]
        )
    )
    
#ejecuta la aplicación
ft.app(main)