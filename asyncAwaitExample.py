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
    task2 = asyncio.create_task(func2())
    # await func1()
    # await func2()
    print('Bye Sagar')

asyncio.run(main())
