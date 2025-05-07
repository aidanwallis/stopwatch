import flet as ft
import asyncio
from datetime import timedelta

class Stopwatch(ft.Text):

    def __init__(self, size):
        super().__init__()
        self.toggle = False
        self.size = size
        self.initial_time = dict(hours = 0, minutes = 0, seconds = 0)
        self.total_time = '{:02d} : {:02d} . {:02d}'
        self.initial_state = self.current_state = timedelta(**self.initial_time)

    def did_mount(self):
        self.toggle = True
        self.value = self.total_time.format(0, 0, 0)
        self.page.run_task(self.start)

    def will_unmount(self):
        self.toggle = False

    async def toggle_off(self):
        self.toggle = False

    async def start(self):
        while self.toggle == True:
            self.update()
            await asyncio.sleep(1)
            self.value = self.increment()

    def stop(self):
        self.current_state = self.initial_state

    def increment(self):
        self.current_state += timedelta(seconds=1)
        hours = self.current_state.seconds // 3600
        minutes = (self.current_state.seconds // 60) % 60
        seconds = self.current_state.seconds % 60
        return self.total_time.format(hours, minutes, seconds)

if __name__ == '__main__':
    def main(page: ft.Page):
        page.add(Stopwatch())

    ft.app(main)