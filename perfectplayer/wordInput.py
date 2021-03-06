import time
import curses


def get_input(seconds):
    def _get_number(stdscr):
        #stdscr.clear()
        timeout = time.time() + seconds
        s = ""
        while time.time() <= timeout:
            time_left = int(timeout - time.time())
            #stdscr.addstr(0, 0, 'Countdown: {} {}'.format(time_left,
            #                                               "*" * time_left + " " * seconds))
            #stdscr.addstr(2, 0, ' ' * 50)
            #stdscr.addstr(2, 0, 'Your Input: {}'.format(s))
            #stdscr.refresh()
            stdscr.timeout(100)
            code = stdscr.getch()
            #stdscr.addstr(10, 0, 'Code: {}'.format(code))  # for debug only
            #stdscr.refresh()

            if code == 10 and s:  # newline
                return s

            if code == 81 or code ==47:  # backspace
                s = s[:-1]

            if 0<=code <= 700:#ord("0") <= code <= ord("9"):
                s += chr(code)
                continue
        return s

    return curses.wrapper(_get_number)

print(get_input(1))
