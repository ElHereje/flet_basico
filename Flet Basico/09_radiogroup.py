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

    def checkRadio(e):
        t1.value = f"La opción seleccionada es {r1.value}"
        page.update()


    r1 = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Text("Elije una opción: "),
                    ft.Radio(label="Rojo", value=1, active_color='red'),
                    ft.Radio(label="Verde", value=2, active_color='green'),
                    ft.Radio(label="Morado", value=3, active_color='purple'),
                    ft.Radio(label="Amarillo", value=4, active_color='yellow')
                ]
            ),
            on_change=checkRadio,
        )
    
    t1 = ft.Text(f"La opción seleccionada es {r1.value}")

    page.add(
        ft.Row(
            alignment='center',
            controls=[r1]
        ),
        t1
    )
    
#ejecuta la aplicación
ft.app(main)