import asyncio
from abc import ABC, abstractmethod
from curses import ERR, KEY_RESIZE, curs_set, wrapper
from playsound import playsound

import _curses

async def func1():
	playsound('pyGen.wav')
	
async def func2():
    playsound('marathi.wav')
    
class Display(ABC):
    def __init__(self, stdscr: "_curses._CursesWindow"):
        self.stdscr = stdscr
        self.done: bool = False

    @abstractmethod
    def make_display(self) -> None:
        pass
    
    @abstractmethod
    def make_message(self, message) -> None:
        pass

    @abstractmethod
    def handle_char(self, char: int) -> None:
        pass

    def set_exit(self) -> None:
        self.done = True

    async def run(self) -> None:
        curs_set(0)
        self.stdscr.nodelay(True)
        self.make_display()
        speech_task = None

        while not self.done:
            char = self.stdscr.getch()
            if char == ERR:
                await asyncio.sleep(0.1)
            elif char == _curses.KEY_UP:
                self.make_message("Running Up")
                speech_task = asyncio.ensure_future(func1())
                self.make_message("Up Completed")
            elif char == _curses.KEY_DOWN:
                self.make_message("Running Down")
                speech_task = asyncio.ensure_future(func2())
                self.make_message("Down Completed")
            elif char == _curses.KEY_LEFT:
                self.make_message("Cancelling...")
                speech_task.cancel()
            elif char == KEY_RESIZE:
                self.make_display()
            else:
                self.handle_char(char)


class MyDisplay(Display):
    def make_display(self) -> None:
        msg1 = "Resize at will"
        msg2 = "Press 'q' to exit"

        maxy, maxx = self.stdscr.getmaxyx()
        self.stdscr.erase()

        self.stdscr.box()
        self.stdscr.addstr(
            int(maxy / 2) - 1, int((maxx - len(msg1)) / 2), msg1
        )
        self.stdscr.addstr(
            int(maxy / 2) + 1, int((maxx - len(msg2)) / 2), msg2
        )

        self.stdscr.refresh()
        
    def make_message(self, msg1) -> None:
        # msg1 = "Custom message here"

        maxy, maxx = self.stdscr.getmaxyx()
        self.stdscr.erase()

        self.stdscr.box()
        self.stdscr.addstr(
            int(maxy / 2) - 1, int((maxx - len(msg1)) / 2), msg1
        )

        self.stdscr.refresh()

    def handle_char(self, char: int) -> None:
        if chr(char) == "q":
            self.set_exit()


async def display_main(stdscr):
    display = MyDisplay(stdscr)
    await asyncio.ensure_future(display.run())


def main(stdscr) -> None:
    return asyncio.run(display_main(stdscr))


if __name__ == "__main__":
    wrapper(main)