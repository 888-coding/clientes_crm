# main.py
import curses
from curses import wrapper 

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Client Relationship Management")
    stdscr.addstr("\n1. Add client")
    stdscr.addstr("\n2. List all clients")
    stdscr.addstr("\n3.Search client by name")
    stdscr.addstr("\n4.Search client by surname")
    stdscr.addstr("\n5.Delete client")
    stdscr.refresh()
    stdscr.getkey()


wrapper(main)