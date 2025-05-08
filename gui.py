import flet as ft
from stopwatch import Stopwatch

def main(page: ft.Page):
    page.title = "⏱️ Stylish Stopwatch"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = "#f0f2f5"
    page.scroll = ft.ScrollMode.AUTO
    page.window_width = 400
    page.window_height = 600

    stopwatch = Stopwatch(40)
    stopwatch.font_family = "Courier New"
    stopwatch.color = "#333"
    stopwatch.weight = ft.FontWeight.BOLD

    lap_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
        height=200,
        divider_thickness=1,
    )

    async def start_clicked(e):
        if not stopwatch.toggle:
            stopwatch.toggle = True
            page.run_task(stopwatch.start)

    async def pause_clicked(e):
        await stopwatch.toggle_off()
        page.update()

    def reset_clicked(e):
        stopwatch.stop()
        stopwatch.value = stopwatch.total_time.format(0, 0, 0)
        stopwatch.current_state = stopwatch.initial_state
        lap_list.controls.clear()
        page.update()

    def lap_clicked(e):
        lap_list.controls.append(
            ft.Text(f"Lap {len(lap_list.controls)+1}: {stopwatch.value}", size=16)
        )
        page.update()

    # App Layout
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Stylish Stopwatch", size=24, weight="bold", color="#222"),
                    ft.Divider(),
                    ft.Container(
                        content=stopwatch,
                        alignment=ft.alignment.center,
                        padding=20,
                        bgcolor="#ffffff",
                        border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=8, color="#bbb", spread_radius=1),
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
