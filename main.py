from wordle import Wordle

def main():
    game = Wordle(path_to_dictonary="./sjp_slownik_do_gier/slowa_5_liter.txt")
    game.play()

if __name__ == "__main__":
    main()