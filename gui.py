import flet as ft
import asyncio
from stopwatch import Stopwatch

def main(page: ft.Page):

    page.title = "Stopwatch"
    stopwatch = Stopwatch(40)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def toggle_off(e):
        stopwatch.update_toggle(False, page)
        page.update(e)

    def toggle_on(e):
        stopwatch.update_toggle(True, page)
        page.update(e)

    page.add(
        ft.Row(
        [
            ft.Column(
                [
                    stopwatch,
                    ft.ElevatedButton(text = 'Start', on_click = toggle_on, width = 150, height = 60),
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