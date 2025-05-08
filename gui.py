import flet as ft
from stopwatch import Stopwatch

def main(page: ft.Page):
    page.title = "Reign and Aiden's Stopwatch"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.bgcolor = "#f0f2f5"
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 400
    page.window_height = 600

    stopwatch = Stopwatch(40)
    stopwatch.page = page
    running = False  # Flag to control the timer loop

    timer_display = ft.Text("00:00", size=32, weight=ft.FontWeight.BOLD, color="#333")

    def update_display():
        timer_display.value = stopwatch.value
        page.update()

    lap_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
        height=200,
        divider_thickness=1,
    )

    async def start_clicked(e):
        nonlocal running
        if not stopwatch.toggle:
            stopwatch.toggle = True
            running = True  # Allow the loop to run
            page.run_task(stopwatch.start)

        while running:
            update_display()
            await page.sleep(0.5)  # Refresh interval

    async def pause_clicked(e):
        nonlocal running
        running = False  # Stop the loop from updating
        stopwatch.stop()
        page.update()

    def reset_clicked(e):
        nonlocal running
        running = False  # Stop updating when reset
        stopwatch.reset()
        lap_list.controls.clear()
        update_display()

    def lap_clicked(e):
        lap_list.controls.append(
            ft.Text(f"Lap {len(lap_list.controls)+1}: {stopwatch.value}", size=16)
        )
        page.update()

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
                            ft.ElevatedButton("Start", on_click=start_clicked, style=ft.ButtonStyle(padding=20)),
                            ft.ElevatedButton("Pause", on_click=pause_clicked, style=ft.ButtonStyle(padding=20)),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=10,
                    ),
                    ft.Row(
                        [
                            ft.OutlinedButton("Reset", on_click=reset_clicked, style=ft.ButtonStyle(padding=20)),
                            ft.OutlinedButton("Lap", on_click=lap_clicked, style=ft.ButtonStyle(padding=20)),
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
