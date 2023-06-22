# tic-tac-toe
import random


class Player:
    """Registration for the game."""
    list_players = []

    def __init__(self):
        """Initializing player data and adding them to the list"""
        self.name = input('ENTER YOUR NAME:  ')
        self.symbol = input('ENTER YOUR SYMBOL:  ')
        Player.list_players.append(self.name)


class Field:
    """Working with the playing field class"""

    def __init__(self):
        """Первоначальная инициализация игрового поля"""
        letters = ['A', 'B', 'C']
        numbers = [' ', 1, 2, 3]
        self.field = [[i, '_', '_', '_'] for i in letters]
        self.field.append(numbers)

    def show_field(self):
        """Initial initialization of the playing field"""
        for i in self.field:
            print(*i)


def check_winner_position(field):
    # Checking the horizontal gain
    for row in field[:3]:
        if all(symbol == row[1] for symbol in row[1:]) and row[1] != '_':
            Game.sym.append(row[1])
            return True

    # Check the vertical gain
    for column in range(1, 4):
        if all(row[column] == field[column][1] for row in field[:3]) and field[column][1] != '_':
            Game.sym.append(field[column][1])
            return True

    # Checking winnings diagonally (from left to right)
    if field[0][1] != '_' and field[0][1] == field[1][2] == field[2][3]:
        Game.sym.append(field[0][1])
        return True

    # Check the winnings diagonally (from right to left)
    if field[0][3] != '_' and field[0][3] == field[1][2] == field[2][1]:
        Game.sym.append(field[0][3])
        return True

    # If none of the conditions are met, we return False
    return False


def get_winner(p1, p2):
    if Game.sym[0] == p1.symbol:
        print(f"{p1.name} is WIN!!!!!")
    elif Game.sym[0] == p2.symbol:
        print(f"{p2.name} is WIN!!!!!")


class Game:
    """Class determines the player who will go first and the general mechanics of the game"""
    sym = []

    def __init__(self):
        """Determining the order of players"""
        self.position_of_players = None
        self.position = None
        self.first_player = random.choice(Player.list_players)
        print(f"{self.first_player} goes first!")
        f.show_field()

    def step(self, player, field):
        """Player move method"""
        self.position = list(input('ENTER YOUR POSITION:  ').upper())
        field.show_field()
        all_positions = []
        if len(self.position) == 2:
            if int(self.position[1]) in range(1, 4):
                if self.position in all_positions:
                    print('INVALID POSITION')
                    return self.step(player, field)
                else:
                    if self.position[0] == 'A':
                        field.field[0][int(self.position[1])] = player.symbol
                        all_positions.append(self.position)
                        field.show_field()

                    elif self.position[0] == 'B':
                        field.field[1][int(self.position[1])] = player.symbol
                        all_positions.append(self.position)
                        field.show_field()
                    elif self.position[0] == 'C':
                        field.field[2][int(self.position[1])] = player.symbol
                        all_positions.append(self.position)
                        field.show_field()
                    else:
                        print('Invalid position')
                        return self.step(player, field)
            else:
                print('INVALID POSITION')
                return self.step(player, field)
        else:
            print('INVALID POSITION')
            return self.step(player, field)


player1 = Player()
player2 = Player()
f = Field()
game = Game()

if game.first_player == player1:
    while not check_winner_position(f.field):
        game.step(player1, f)
        if check_winner_position(f.field):
            get_winner(player1, player2)
            break

        game.step(player2, f)
        if check_winner_position(f.field):
            get_winner(player1, player2)
            break

    else:
        get_winner(player1, player2)
else:
    while not check_winner_position(f.field):
        game.step(player2, f)
        if check_winner_position(f.field):
            get_winner(player1, player2)
            break

        game.step(player1, f)
        if check_winner_position(f.field):
            get_winner(player1, player2)
            break

    else:
        get_winner(player1, player2)
