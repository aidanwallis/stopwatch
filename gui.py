import flet as ft
from stopwatch import Stopwatch

def main(page: ft.Page):

    page.title = "Stopwatch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    button_state = True
    
    def button_click(e):
        nonlocal button_state
        button_state = not button_state

        if button_state:
            start_stop_button.text = "Start"
            toggle_off()
        else:
            start_stop_button.text = "Stop"
            toggle_on()
        page.update()

    def toggle_off():
        stopwatch.update_toggle(False, page)
        page.update()

    def toggle_on():
        stopwatch.update_toggle(True, page)
        page.update()

    def reset_click(e):
        stopwatch.reset()
        page.update()

    stopwatch = Stopwatch(60)
    start_stop_button = ft.ElevatedButton(text="Start", on_click=button_click, width=150, height=60)
    reset_button = ft.ElevatedButton(text='Reset', on_click=reset_click, width=150, height=60)
    buttons = ft.Row(
                [
                start_stop_button,
                reset_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

    page.add(
        ft.Row(
        [
            ft.Column(
                [
                    stopwatch,
                    buttons
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