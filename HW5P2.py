'''
Homework 5 Part 1 - coding
Maher Harkati
Problem 2 - Treasure Chest 
'''
import random

class PirateTreasureGame:
    def __init__(self):
        self.treasure_chest = {
            'gold_coin': 5,
            'silver_coin': 10,
            'ruby': 2,
            'diamond': 1,
            'empty': 50  # Represents an empty grab
        }
        self.bank_account = 100

    def display_treasure_chest(self):
        print("Treasure Chest:")
        for item, count in self.treasure_chest.items():
            print(f"{item.capitalize()}: {count}")

    def play_game(self, wager):
        if wager > self.bank_account:
            print("Insufficient funds. Game over.")
            return

        grabbed_item = random.choices(list(self.treasure_chest.keys()), weights=list(self.treasure_chest.values()))[0]
        self.treasure_chest[grabbed_item] -= 1

        if grabbed_item == 'empty':
            print("Oh no! The chest is empty. Better luck next time.")
        else:
            print(f"You grabbed a {grabbed_item} from the treasure chest!")

        self.bank_account -= wager

    def display_bank_account(self):
        print(f"Current Bank Account: {self.bank_account}")

# Example Usage
pirate_game = PirateTreasureGame()

while pirate_game.bank_account > 0:
    pirate_game.display_bank_account()
    pirate_game.display_treasure_chest()

    wager = int(input("\nPlace your wager: "))
    pirate_game.play_game(wager)

    input("Press Enter to continue...")

print("Game Over! Your bank account is 0 or below.")
