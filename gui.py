import flet as ft
from stopwatch import Stopwatch

def main(page: ft.Page):

    page.title = "Stopwatch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def toggle_off():
        Stopwatch.toggle_off()
        page.update()

    page.add(
        ft.Row(
        [
            ft.Column(
                [
                    Stopwatch(40),
                    ft.ElevatedButton(text = 'Stop', on_click = toggle_off, width = 150, height = 60)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )    
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(main)