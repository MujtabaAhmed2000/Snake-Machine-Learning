import tkinter
import pygame

game_height = 600
game_width = 600
game_menu = tkinter.Tk()


def open_game():
    game_menu.withdraw()
    pygame.init()
    snake_game_window = pygame.display.set_mode((game_menu.winfo_width(), game_menu.winfo_height()))
    pygame.display.update()


def main():
    game_menu.title("SNAKE")
    game_menu.geometry(str(game_height) + "x" + str(game_width))
    play_game_player = tkinter.Button(game_menu, text="PLAY", command=open_game)
    play_game_player.pack(side=tkinter.BOTTOM)
    game_menu.mainloop()


if __name__ == "__main__":
    main()
