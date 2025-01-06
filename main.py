#main test file

from Creature import Creature
import Interface as UI
def main():
    window = UI.Interface(UI.gameMaster)
    window.mainloop()


if __name__ == '__main__':
    main()