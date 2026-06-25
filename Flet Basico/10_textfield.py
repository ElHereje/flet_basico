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
    
    def check_txt(e):
        t1.value = f"El valor del texto es : {tx1.value}"
        page.update()
        
    def borar_txt(e):
        tx1.value = ""
        t1.value = f"El valor del texto es : {tx1.value}"
        

    tx1 = ft.TextField(
            label="Nombre :",
            hint_text="Introduce tu nombre",
            #multiline=True, # se añaden renglones al escribir
            #min_lines=1,
            #max_lines=5, # min y max de lineas
            #password=True, # encripta los caracteres
            
            on_change=check_txt, #se ve la entrada en el resultado letra por letyra
            on_blur=check_txt, # habilita la funcion con el enter
            
            #personalizacion
            border=ft.InputBorder.UNDERLINE, # queda solo la linea inferior
            color='red', # color del texto de la caja
            label_style=ft.TextStyle(color='green'),
            focused_border_color='yellow',
            border_color='purple',
            selection_color='blue',
            cursor_color='pink'
                                    
        )
    
    t1 = ft.Text(f"El valor del texto es {tx1.value}")

    page.add(
        tx1,
        t1,
        ft.Button("Aceptar", on_click=check_txt),
        ft.Button("Borrar", on_click=borar_txt)
    )
    
#ejecuta la aplicación
ft.app(main)