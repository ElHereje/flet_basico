import flet as ft

def main(page:ft.Page):
    #------ Configuracion de la aplicación---------
    page.title = "Ventana"
    page.window.height = 500
    page.window.width = 500
    page.window.resizable = False
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'dark '
    #----------------------------------------

    def check_test(e):
        t1.value = f"El valor es {c1.value}"
        page.update()
        
    c1 = ft.Switch(
            label="Motor",
            value=False,
            on_change=check_test
        )
    
    t1 = ft.Text(f"El valor es {c1.value}")

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[c1]
        ),
        t1
    )
    
#ejecuta la aplicación
ft.app(main)