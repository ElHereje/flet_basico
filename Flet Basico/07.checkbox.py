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
        t1.value=f"El valor del CheckBox es: {c1.value}"
        page.update

    c1 = ft.Checkbox(
            label="Motor",
            value=None, # valor inicial True, False o None
            tristate=True, # 3 estados
            on_change=check_test,
            
            #diferenciacion con colores
            check_color='white',
            active_color='green',
            hover_color=ft.Colors.AMBER
        )
    
    t1 = ft.Text(f"El valor del CheckBox es: {c1.value}")
    
    page.add(
        ft.Row( # añadimos una fila
            #organizamos la pila de forma horiz.
            alignment=ft.MainAxisAlignment.CENTER,
            #lo que hace
            controls=c1
        ),
        t1
    )
    
#ejecuta la aplicación
ft.app(main)