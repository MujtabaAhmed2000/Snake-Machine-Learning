import tkinter as tk
import pygame

game_height = 600
game_width = 600


class MainMenu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # tk.Frame.title("SNAKE")
        play_game_player = tk.Button(self, text="PLAY", command=MainMenu.open_game)
        play_game_player.pack(side=tk.BOTTOM)

    def open_game(self):
        root.withdraw()
        pygame.init()
        snake_game_window = pygame.display.set_mode((game_height, game_width))
        pygame.display.update()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("SNAKE")
    root.geometry(str(game_height) + "x" + str(game_width))
    MainMenu(root).pack(side="top", fill="both", expand=True)
    root.mainloop()