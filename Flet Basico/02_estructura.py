import flet as ft

def main(page:ft.Page):
    
    # de esta manera, primero los crea y luego los coloca
    # con un update
    '''page.controls.append(
        ft.Text("Ejempl")
    )
    page.update()
    '''
    
    # de esta otra, los añade directamente:
    page.title = "Ventana"
    page.window.height = 300
    page.window.width = 300
    
    page.window.resizable = False
    
    page.bgcolor = 'white'
    
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    
    page.add( # se acomodan de arriba hacia abajo
        ft.Text('Ejemplo1', color= 'black'),
        ft.Text('Ejemplo2', color= 'black'),
        ft.Text('Ejemplo3', color= 'black'),
        ft.Text('Ejemplo4', color= 'black'),
        ft.Text('Ejemplo5', color= 'black')
    )
    
ft.app(main)