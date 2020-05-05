# Import Error

try:
    import msvcrt


    def getkey():
        "Wiat for key press in microsoft key board"
        return msvcrt.getch()
except ImportError as e:

    import sys
    import tty
    import termios

    print(e, file=sys.stderr)

    def getkey():
        "Wiat for key press in linux key board"
        fd = sys.stdin.fileno()
        original_attr = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attr)
            return ch
