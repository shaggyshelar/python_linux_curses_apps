import curses
import os
from playsound import playsound
import asyncio

def func1():
	playsound('pyGen.wav')
	return

def func2():
    playsound('marathi.wav')
    return

def main():
    print('hello sagar')
    task1 = asyncio.create_task(func1())
    print('Bye Sagar')
# asyncio.run(main())

def main(stdscr):
    
	while 1:
		key = stdscr.getch()

		# clear existing texts
		stdscr.clear()

		if key == curses.KEY_UP:
			stdscr.addstr(0, 0, "You pressed Up key!")
            # os.system('flite "Hey Sagar. Flite is a small fast run-time synthesis engine" pyGen.wav')
			os.system('flite "Hey Sagar. Flite is a small fast run-time synthesis engine" pyGen.wav')
			# os.system('flite -voice ~/BL/flite/voices/cmu_indic_mar_aup.flitevox "आपण निवडलेल्<200d>या भाषेमध्<200d>ये टाइप करणे सोपे बनवतात" marathi.wav')
			# stdscr.addstr(0, 0, output)
		elif key == curses.KEY_DOWN:
			stdscr.addstr(0, 0, "You pressed Down key!")
			func1()
            # task1 = asyncio.create_task(func1())
			stdscr.clear()
			stdscr.addstr(0, 0, "Done Playing 111!")
		elif key == curses.KEY_ENTER or key in [10, 13]:
			stdscr.addstr(0, 0, "Playing!")
			task2 = asyncio.create_task(func2())
			stdscr.addstr(0, 0, "Done Playing 222!")
		else:
			break

		# update screen
		stdscr.refresh()
curses.wrapper(main)