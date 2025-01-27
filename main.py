import threading
from console.interface import start_tkinter
from operations.__keyboard_listener import start_keyboard_listener


def main():
    keyboard_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
    keyboard_thread.start()

    start_tkinter()

if __name__ == "__main__":
    main()
