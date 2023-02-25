import output_logic
from output_logic import GameOverError

class QuitError(Exception):
    pass

def create_game():
   '''
   After asking for input from user for rows columns and content,
   function creates the game object with those answers
   If they specfied for empty board then an empty game board is created
   else they can specify the contents and their contents will be used to create
   a game board
   '''
   rows = int(input())
   columns = int(input())
   contents = input()
   game = output_logic.Game(rows,columns)
   if contents == 'EMPTY':
       pass
   elif contents == 'CONTENTS':
       elements_list = get_contents(game)
       game.specified_contents(elements_list)

   return game

def get_contents(game):
    '''
    if the user specifies content then this function is called.
    User is then asked to input the rows of content.
    Content is then split and made into a 2d list
    Finally that list is returned
    '''
    elements_list = []
    for r in range(game.get_rows()):
        row_contents = input()
        elements_list.append(list(row_contents))
    return elements_list
                 
def play():
    '''
    This is the main function that dictates how the game will play out.
    At any time if the Q function is called the program will end
    '''
    game = create_game()
    game.mark_all_matches_board()
    print_board(game)
    matches_found(game)
    while True:
        try: 
            main_input = input()
            if main_input == 'Q':
                raise QuitError
            jewel = main_input.split()[2:]
            column_num = int(main_input.split()[1])-1
            faller = output_logic.Faller(jewel, column_num, 0)
            game.time_tick(faller)
            print_board(game)

            faller_actions(game,faller)

            if faller.get_state()=='frozen':
                game.mark_all_matches_board()
                matches_found(game)
          
            game.game_over()

        except GameOverError:
            print('GAME OVER')
            break
        except QuitError:
            break
           

def matches_found(game):
    '''
    checks for matches then deletes match
    '''
    while game.board_contains_stars():
        user_input = input()
        if user_input == 'Q':
            raise QuitError
        if user_input == '':
            game.delete_match()
            game.mark_all_matches_board()
            print_board(game)
    
def faller_actions(game,faller):
    '''
    While a faller is not frozen yet, user can do these series of actions
    (Q, '','R','>','<')
    quit
    pass time
    rotate
    shift right
    shift left
    '''
    while faller.get_state()!= 'frozen':

        user_input = input()
        if user_input == 'Q':
            raise QuitError
        if user_input == '':
            game.time_tick(faller)
        elif user_input == 'R':
            faller.rotate(game)
        elif user_input == '>':
            faller.shift_right(game)
        elif user_input == '<':
            faller.shift_left(game)
            
        print_board(game)

def print_board(game):
    '''
    prints the current board
    '''
    board = game.current_board()
    for r in range(3,game.get_rows()+3):
        row = '|'
        for c in range(game.get_columns()):
            if not '*' in board[c][r]\
            and not '[' in board[c][r]\
            and not '|' in board[c][r]:
                row+=' ' + board[c][r] + ' '
            else:
                row+= board[c][r]
        row+='|'
        print(row)
    print(bottom_row(game))
            
                
def bottom_row(game):
    '''
    prints the bottom row of the board
    '''
    bottom_board = ' '
    for column in range(game.get_columns()):
        bottom_board += '---'
    bottom_board += ' '
    return(bottom_board)
        


if __name__ == '__main__':
    play()
    
