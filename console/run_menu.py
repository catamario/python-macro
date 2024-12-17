import pynput
from pynput.keyboard import Listener, Key

optiune = False
def tasta(key):
    global optiune
    if key == Key.f2:  # Verifică dacă tasta F2 este apăsată
        print("ai ales optiunea de inregistrare")
        optiune = True

def run_menu():
    while True:
        print("f2 - inregistreaza miscari mouse")
        with Listener(on_press=tasta) as listener:
            print("Aștept apăsarea tastei F2...")
            listener.join()
if __name__ == "__main__":
    run_menu()