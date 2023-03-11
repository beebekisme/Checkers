class OutOfTurn(Exception):
    pass

class InvalidSquare(Exception):
    pass

class InvalidPlayer(Exception):
    pass


class Checkers:
    
    def __init__(self):
        self.board = [[None, "White", None, "White", None, "White", None, "White"],
                      ["White", None, "White", None, "White", None, "White", None],
                      [None, "White", None, "White", None, "White", None, "White"],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      ["Black", None, "Black", None, "Black", None, "Black", None],
                      [None, "Black", None, "Black", None, "Black", None, "Black"],
                      ["Black", None, "Black", None, "Black", None, "Black", None]]



    def create_player(self, player_name, player_color):
        available_colors = ["White", "Black"]
        if player_color not in available_colors:
            raise ValueError
        else:
                
            pass

    def play_game(self):
        pass

    def get_checker_details(self, square_location: tuple):
        if square_location[0] > 7 or square_location[1] > 7:
            raise InvalidSquare
        else:
            pass

    def print_board(self):
        return self.board

    def game_winner(self):
        return self.player_name

    


class Player:

    def __init__(self):
        self.player_name = ""
        self.player_color = ""
        
    
    def get_king_count(self):
        return number_of_kings

    def get_triple_king_count(self):
        return number_of_triple_kings

    def get_captured_pieces_count(self):
        return number_of_captured_pieces
        