import flet as ft
from stopwatch import Stopwatch

def main(page: ft.Page):
    page.title = "Reign and Aidan's Stopwatch"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.bgcolor = "#f0f2f5"
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 400
    page.window_height = 600

    stopwatch = Stopwatch(60)
    stopwatch.page = page
    button_state = True
    saved_time_value = None

    timer_display = ft.Text("00:00", size=32, weight=ft.FontWeight.BOLD, color="#333")

    lap_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
        height=200,
        divider_thickness=1,
    )

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
        stopwatch.update_stop_test()
        page.update()

    def toggle_on():
        stopwatch.update_toggle(True, page)
        page.update()

    def reset_click(e):
        stopwatch.reset()
        page.update()

    def save_time(e):
        nonlocal saved_time_value
        saved_time_value = stopwatch.get_current_time()
        saved_time.value = saved_time_value
        save_time_button.text = f"Saved Time: \n{saved_time.value}"
        page.update()

    def lap_clicked(e):
        lap_list.controls.append(
            ft.Text(f"Lap {len(lap_list.controls)+1}: {stopwatch.value}", size=16)
        )
        page.update()

    
    saved_time = ft.Text(value=f'{saved_time_value}')
    start_stop_button = ft.ElevatedButton(text="Start", on_click=button_click, width=150, height=60, style=ft.ButtonStyle(padding=20))
    reset_button = ft.ElevatedButton(text='Reset', on_click=reset_click, width=150, height=60, style=ft.ButtonStyle(padding=20))
    save_time_button = ft.ElevatedButton(text="Save Time", on_click=save_time, width=150, height=60, style=ft.ButtonStyle(padding=20))
    lap_button = ft.ElevatedButton(text='Lap', on_click=lap_clicked, width=150, height=60, style=ft.ButtonStyle(padding=20))

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Stylish Stopwatch", size=24, weight="bold", color="#222"),
                    ft.Divider(),
                    ft.Container(
                        content=ft.Column([
                            timer_display,
                            ft.Container(
                                content=stopwatch,
                                alignment=ft.alignment.center,
                                padding=20,
                                bgcolor="#ffffff",
                                border_radius=20,
                                shadow=ft.BoxShadow(blur_radius=8, color="#bbb", spread_radius=1),
                            ),
                        ]),
                        alignment=ft.alignment.center,
                    ),
                    ft.Row(
                        [
                            start_stop_button,
                            lap_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=10,
                    ),
                    ft.Row(
                        [
                            reset_button,
                            save_time_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=10,
                    ),
                    ft.Container(
                        content=lap_list,
                        bgcolor="#fff",
                        border_radius=10,
                        padding=10,
                        height=200,
                        shadow=ft.BoxShadow(blur_radius=6, color="#ccc"),
                    ),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=20,
            bgcolor="#ffffff",
            padding=20,
            shadow=ft.BoxShadow(blur_radius=10, color="#aaa", offset=ft.Offset(2, 2)),
        )
    )

ft.app(target=main)