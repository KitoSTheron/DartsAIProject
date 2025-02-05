import tkinter as tk
from GameLogic import GameLogic
from Dartboard import Dartboard
from Player import HumanPlayer, AIPlayer

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dartboard Game")

    # Set the initial dimensions of the window and disable resizing
    initial_width = 1000
    initial_height = 600
    root.geometry(f"{initial_width}x{initial_height}")
    root.resizable(False, False)  # Disable window resizing

    # Create the Dartboard, Player, and GameLogic instances
    dartboard = Dartboard(master=root)
    player1 = HumanPlayer("player1", dartboard, 0)
    player2 = AIPlayer("player2", dartboard, 1)
    game_logic = GameLogic(master=root, dartboard=dartboard, player1=player1, player2=player2)
        # Schedule the playGame method to run after the Tkinter event loop starts
    root.after(100, game_logic.playGame)
    
    root.mainloop()