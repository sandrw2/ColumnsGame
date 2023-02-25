#Sandra Wang 14772372
import output_logic
import random
from output_logic import GameOverError

class Cell:
    def __init__(self,height:float,width:float,
                 location:(float,float),color:[int,int,int]):
        self._cells = []
        self._height= height
        self._width= width
        self._color=color
        self._location =location


    def get_height(self) -> float:
        '''
        returns the height of each cell
        '''
        return self._height
    def get_width(self) -> float:
        '''
        returns the width of each cell
        '''
        return self._width
    def get_location(self)-> (float,float):
        '''
        returns the location of each cell
        '''
        return self._location
    def get_color_r(self)-> int:
        '''
        returns the red value of the color RGB color values
        If the value is greater than 255 then the red color value
        will be set to 255
        If the value is less than 0 then the red color value will be set
        to 0
        '''
        if self._color[0]>255:
            self._color[0] = 255
        if self._color[0]<0:
            self._color[0] = 0
        return self._color[0]

    def get_color_g(self) -> int:
        '''
        returns the green value of the color RGB color values
        If the value is greater than 255 then the green color value
        will be set to 255
        If the value is less than 0 then the green color value will be set
        to 0
        '''
        if self._color[1]>255:
            self._color[1] = 255
        if self._color[1]<0:
            self._color[1] = 0
        return self._color[1]

    def get_color_b(self) -> int:
        '''
        returns the blue value of the color RGB color values
        If the value is greater than 255 then the blue color value
        will be set to 255
        If the value is less than 0 then the blue color value will be set
        to 0
        '''
        if self._color[2]>255:
            self._color[2] = 255
        if self._color[2]<0:
            self._color[2] = 0
        return self._color[2]


class GameState:
    def __init__(self):
        self._game = output_logic.Game(13,6)
        self._cells = self.accumulate_cells()
        self._random_faller = self.random_faller()

    def all_cells(self) -> [Cell]:
        '''
        returns a list of all the cells
        '''
        return self._cells

    def random_faller(self) -> 'Faller':
        '''
        creates a random faller and returns it
        '''
        faller_letters = self._faller_list()
        new_faller = output_logic.Faller(faller_letters,
                                        self._random_column(),0)
        return new_faller

    def _random_column(self) -> int:
        '''
        returns a random column number that does not correspond to a column
        that is already filled
        If ALL columns are already filled, then it just returns a random column
        number
        '''
        column = random.choice(range(6))
        if self._game.column_filled():
            return column
        else:
            while self._game.specific_column_filled(column):
                column = random.choice(range(6))
            return column
        
            
    def _faller_list(self) -> ['letters']:
        '''
        creates a random letter list for the faller
        then returns it
        '''
        faller=[]
        for times in range(3):
            letter_list = ['S','T','V','W','X','Y','Z']
            random_letter = random.choice(letter_list)
            if faller.count(random_letter)<2:
                faller.append(random_letter)
            else:
                letter_list.remove(random_letter)
                faller.append(random.choice(letter_list))
        return faller
    
    def move_faller_tick(self)-> None:
        '''
        moves the faller downwards and updates the cells list
        '''
        if self._random_faller.get_state()=='frozen':
            if self._game.board_contains_stars():
                self._game.delete_match()
                self._game.mark_all_matches_board()
                self._cells = self.accumulate_cells()
                return
            self._game.game_over()
            self._random_faller = self.random_faller()

        self._game.time_tick(self._random_faller)
        self._cells = self.accumulate_cells()
        
    
    def move_left(self)-> None:
        '''
        moves the faller to the left if nothing is blocking it
        and then updaates the cell list.
        If the faller was in a landing state and then shifts the left
        where nothing is below it, the state changes from landing to falling.
        vice versa
        '''
        if self._random_faller.get_state() != 'frozen':
            self._random_faller.shift_left(self._game)
            self._cells = self.accumulate_cells()
            

    def move_right(self) -> None:
        '''
        moves the faller to the right if nothing is blocking it
        and then updaates the cell list.
        If the faller was in a landing state and then shifts the right
        where nothing is below it, the state changes from landing to falling.
        vice versa
        '''
        if self._random_faller.get_state() != 'frozen':
            self._random_faller.shift_right(self._game)
            self._cells = self.accumulate_cells()
            

    def rotate(self) ->None:
        '''
        rotates the faller and updates the cell list
        '''
        if self._random_faller.get_state() != 'frozen':
            self._random_faller.rotate(self._game)
            self._cells = self.accumulate_cells()
            
        

    def accumulate_cells(self) -> [Cell]:
        '''
        This function updates the self._cells list by constantly checking
        each element in game.current_board()
        '''
        cell_list = []
        counter_y=0
        board = self._game.current_board()
        for r in range(3,self._game.get_rows()+3):
            counter_x=0
            for c in range(self._game.get_columns()):
                cell_list.append(Cell(0.062,0.062,
                                 (0.05+(counter_x*0.072),0.05+(counter_y*0.072)),
                                 self._color_value(board[c][r])))
                counter_x+=1
            counter_y+=1
        return cell_list

    def  _color_value(self, cell_value:str) -> ['R','G','B']:
        '''
        Adds saturation value to all three rgb values and returns new color. 
        '''
        
        saturation = self._state_saturation(cell_value)
        
        if cell_value == ' ':
            return [142,124,124]
        if 'S' in cell_value:
            return [saturation+255,saturation+219,saturation+31]
        if 'T' in cell_value:
            return [saturation+255,saturation+115,saturation+0]
        if 'V' in cell_value:
            return [saturation+255,saturation+152,saturation+166]
        if 'W' in cell_value:
            return [saturation+169,saturation+100,saturation+166]
        if 'X' in cell_value:
            return [saturation+37,saturation+100,saturation+166]
        if 'Y' in cell_value:
            return [saturation+77,saturation+180,saturation+128]
        if 'Z' in cell_value:
            return [saturation+208,saturation+45,saturation+46]

    def _state_saturation(self,cell_value:str)-> int:
        '''
        Depending on the contents in the specific cell, the color
        of the cell will either be dimmed or brightened.
        If the cell is marked as falling, the color will stay normal
        if the cell is marked as landed, the color will be dimmed
        if the cell is marked as frozen, the color will be return back to normal
        if the cell is marked as matched, the color will be brightened
        Brightening = positive saturation value
        dimming = negative saturation value 
        '''
        if '*' in cell_value:
            return 100
        if '|' in cell_value:
            return int(-100)
        if '[' in cell_value:
            return 0
        return 0
    
        
