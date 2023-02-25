#Sandra Wang 14772372
class Game:

    def __init__(self, rows,columns):
        self._rows = rows
        self._columns = columns
        self._board  = self._create_game_board()
        self._state = 'playing'
        
        
    def get_columns(self) -> int:
        return self._columns
    def get_rows(self) -> int:
        return self._rows

    def _create_game_board(self) -> [['']]:
        '''
        creates game board which is a 2d list
        each list within the list represents a column
        and every element inside the lists is a row element
        there are three extra spaces for the spawn area of the fallers
        '''
        board = []
        for i in range(self.get_columns()):
            board.append([])
            for j in range(self.get_rows()+3):
                board[i].append(' ')
        return board 
                
       
    def current_board(self) -> [['']]:
        return self._board

    def update_column(self,column_num:int, new_column:[''] ) -> None:
        self._board[column_num] = new_column

    def update_board(self, board:[['']])-> None:
        self._board = board

    def specified_contents(self,contents:[['']]) -> None:
        '''
        given contents that should be specified
        this function copies those contents onto the board
        and updates the board attribute
        '''
        board = []
        for column in range(self.get_columns()):
            board.append([])
            
        for r in range(self.get_rows()):
            for c in range(self.get_columns()):
                if contents[r][c] != ' ':
                    board[c].append(contents[r][c])

        for column in range(self.get_columns()):
            while len(board[column])< self.get_rows()+3:
                board[column].insert(0,' ')

        self.update_board(board)
                
    
    def column_filled(self) -> bool:
        '''
        Checks if any of the columns enters the spawn area
        which means the column is filled
        '''
        board = self.current_board()
        for column in board:
            if column[2] != ' ':
                return True
        
        return False

    def specific_column_filled(self, column_num:int) -> bool:
        board = self.current_board()
        if board[column_num][3] != ' ':
            return True
        return False
            

    def time_tick(self,faller: 'Faller') -> None:
        '''
        makes the faller shift down and updates its state
        '''
        if faller.get_state() == 'falling':
            faller.shift_down(self)
            faller.set_state(self)
            
        elif faller.get_state() == 'frozen':
            faller.set_state(self)
            
        else:
            faller.set_state(self)
      
        

    def mark_matching(self,match_list:[],start_col:int,start_row:int)->None:
        '''
        Given a list of match information which contains tuples of
        3 elements(solumn shift, row shift, and how many matches there are in that
        direction),function marks all of those elements with stars.
        '''
        if match_list != []:
            board = self.current_board()
            start_column = board[start_col]
            start_cell = start_column[start_row]
            if not '*' in start_cell:
                start_column[start_row] = f'*{start_cell}*'
                self.update_column(start_col, start_column)
            for match in match_list:
                col_shift = match[0]
                row_shift = match[1]
                counter = match[2]
                for x in range(1,counter+1):
                    col_num = start_col+(col_shift*x)
                    row_num = start_row+(row_shift*x)
                    column = board[col_num]
                    content = column[row_num]
                    if not '*' in content:
                        column[row_num] = f'*{content}*'
                        self.update_column(col_num, column)
            

    def _valid_column(self,col_num: int) -> bool:
        if 0<=col_num < self.get_columns():
            return True
        else:
            return False
        
    def _valid_row(self,row_num:int) ->bool:
        if 0<= row_num< self.get_rows()+3:
            return True
        else:
            return False

    
    def _three_or_more_match(self,col:int,row:int,col_shift:int,row_shift:int) -> int:
        '''
        returns how many matches are in a certain direction (column_shift, row_shift)
        and then returns it 
        '''
        board  = self.current_board()
        start_cell = board[col][row]
        counter =0
        if start_cell == ' ':
            return 0
        else:
            while True:
                if self._valid_column(col+col_shift) and self._valid_row(row+row_shift):
                    if start_cell == board[col+col_shift][row+row_shift]:
                        counter+=1
                        col = col_shift+col
                        row = row_shift+row
                    else:
                        break
                else:
                    break

            return counter
        
    def _is_match(self, col:int, row:int) -> [int]:
        '''
        given a current column and row of a cell, function checks which direction
        has three or more matches to the current cell. If there are 3 or more matches,
        function appends a tuple of three elements(column_shift, row_shift, counter)
        (counter represents how many matches there are) into a match_list.
        Then, it returns match_list.
        '''
        board = self.current_board()
        match=[]
        counter_1 = self._three_or_more_match(col,row,0,1)
        counter_2 = self._three_or_more_match(col,row,1,0)
        counter_3 = self._three_or_more_match(col,row,1,1)
        counter_4 = self._three_or_more_match(col,row,-1,0)
        counter_5 = self._three_or_more_match(col,row,0,-1)
        counter_6 = self._three_or_more_match(col,row,-1,-1)
        counter_7 = self._three_or_more_match(col,row,1,-1)
        counter_8 = self._three_or_more_match(col,row,-1,1)
        if counter_1 >=2:
            match.append((0,1,counter_1))
        if counter_2 >=2:
            match.append((1,0,counter_2))
        if counter_3 >=2:
            match.append((1,1,counter_3))
        if counter_4 >=2:
            match.append((-1,0,counter_4))
        if counter_5 >=2:
            match.append((0,-1,counter_5))
        if counter_6 >=2:
            match.append((-1,-1,counter_6))
        if counter_7 >=2:
            match.append((1,-1,counter_7))
        if counter_8 >=2:
            match.append((-1,1,counter_8))


        return match


    def delete_match(self) ->None:
        '''
        function deletes cells with * and shifts everything downwards
        '''
        board = self.current_board()
        for column in range(self.get_columns()):
            new_col = board[column]
            for row in range(self.get_rows()+3):
                if '*' in new_col[row]:
                    new_col.pop(row)
                    new_col.insert(0,' ')
                self.update_column(column, new_col)


    def board_contains_stars(self) -> bool:
        '''
        function returns True if there are stars in the board
        returns False otherwise
        '''
        for column in range(self.get_columns()):
                for row in range(self.get_rows()+3):
                    if '*' in self.current_board()[column][row]:
                        return True
        return False
        
    def mark_all_matches_board(self) -> None:
        '''
        marks all possible matches on the board with *
        '''
        for column in range(self.get_columns()):
            for row in range(self.get_rows()+3):
                match_list = self._is_match(column,row)
                self.mark_matching(match_list,column,row)
                

    def game_over(self)->None:
        '''
        If the board does not contain stars (matches) and a column is filled
        function raises a GameOverError
        '''
        if not self.board_contains_stars() and self.column_filled():
            raise GameOverError
        
class GameOverError(Exception):
    pass
        
class Faller():
    def __init__(self, letters:['letters'],column:int,tick:int):
        self._letters = letters
        self._column = column
        self._tick = tick
        self._state = 'falling'

    def frozen_sequence(self,game:Game)-> None:
        '''
        if faller is frozen, then this function is called to change the symbols
        of that faller to match its frozen state or in otherwords no symbols
        '''
        column = game.current_board()[self._column]
        faller = self._letters
        for space in range(len(column)):
            if '|' in column[space]:
                string = column[space]
                column[space] = string[1:2]
        game.update_column(self._column, column)
        
    def landed_sequence(self,game:Game)-> None:
        '''
        if faller is landed, then this function is called to change the symbols
        of that faller to match its landed state in other words with ||
        '''
        column = game.current_board()[self._column]
        faller = self._letters
        for space in range(len(column)):
            if '[' in column[space]:
                string = column[space]
                column[space] = string[1:2]
                column[space] = f'|{column[space]}|'
        game.update_column(self._column, column)

    def falling_sequence(self,game:Game) -> None:
        '''
        if faller is landed, then this function is called to change the symbols
        of that faller to match its landed state in other words with []
        '''
        column = game.current_board()[self._column]
        faller = self._letters
        for space in range(len(column)):
            if '|' in column[space]:
                string = column[space]
                column[space] = string[1:2]
                column[space] = f'[{column[space]}]'
        game.update_column(self._column, column)

    def set_state(self,game:Game)-> None:
        '''
        function changes the state of the faller :
        1) if faller was previously 'landed' then function will set its state to 'frozen'
        2) if faller's next position is not empty then function will set state to
        'landed'
        3)else it will remain the same state as previous 
        '''
        column = game.current_board()[self._column]
        start = self.index_start(game)
        current_pos= column.index(self.state_symbols(self._letters[2]),start)
        next_pos = current_pos+1
        max_pos= len(column)-1
        current_state = self.get_state()

        if current_state == 'landed':
            self._state = 'frozen'
            self.frozen_sequence(game)
            game.mark_all_matches_board()

        elif current_state == 'frozen':
            pass

        elif current_pos >= max_pos or column[next_pos] != ' ':
            self._state = 'landed'
            self.landed_sequence(game)
        else:
            self._state = 'falling'
        
    
    def get_state(self)-> None:
        return self._state      

    def add_fallers(self,game:Game):
        '''
        when fallers are first created this function adds the faller to the board
        according to its column number
        '''
        column = game.current_board()[self._column]
        for index in range(len(self._letters)):
            column[index] = f'[{self._letters[index]}]'

        game.update_column(self._column, column) 


    def shift_down(self, game:Game)-> None:
        '''
        this function moves the faller down and updates the board every time it
        is called.
        '''
    
        column = game.current_board()[self._column]
        faller = self._letters
        max_pos = len(column)-1

        #If this is the first time this function is called, then add the
        #spawned faller into the column before the 'visible line'
        
        if self.get_tick() == 0:
            self.add_fallers(game)

        start = self.index_start(game)

        
        if self.get_tick() <= 2:
                current_pos = column.index(self.state_symbols(faller[2]), start)
                next_pos = current_pos+1
                if current_pos<max_pos and column[next_pos] == ' ':
                        column.pop(next_pos)
                        column.insert(0,' ')
                self._tick_one()
        else:
            current_pos  = column.index(self.state_symbols(faller[2]),start)
            next_pos = current_pos +1
            if current_pos < max_pos and column[next_pos] == ' ':
                column.pop(next_pos)
                column.insert(0,' ')
                self._tick_one()
          
        game.update_column(self._column,column)
       

    def index_start(self, game:Game) -> int:
        #If there are two of the same jewel (one of them being the first jewel)
        #then make the starting point after the first
        #jewel for the .index() method,that way we always find the
        #index for the first jewel no matter if it is the only one in the faller
        #or not
        column = game.current_board()[self._column]
        faller = self._letters
        if faller.count(self._letters[2]) == 2:
            start = column.index(self.state_symbols(faller[2]))+1
        else:
            start = 0

        return start

    def state_symbols(self,jewel:'content') -> str:
        '''
        To know what to look for, this function returns each jewel with specific
        symbols according to the current state of the faller
        '''
        state = self.get_state()
        if state == 'frozen':
            return jewel
        elif state == 'falling':
            return f'[{jewel}]'
        elif state == 'landed':
            return f'|{jewel}|'

    def update_letters(self) -> None:
        '''
        When faller is rotated, the function updates the letter order
        '''
        fallers = self._letters
        last_jewel = fallers.pop(2)
        fallers.insert(0,last_jewel)
        self._letters = fallers
        
    def rotate(self,game:Game) -> None:
        '''
        Function is in charge of rotating the faller
        '''
        column = game.current_board()[self._column]
        faller = self._letters
        start = self.index_start(game)
        pop_index = column.index(self.state_symbols(faller[2]),start)
        insert_index = column.index(self.state_symbols(faller[0]))
        last_jewel = column.pop(pop_index)
        column.insert(insert_index, last_jewel)
        game.update_column(self._column, column)
        self.update_letters()
        
    
    def get_tick(self)-> None:
        return self._tick

    def _tick_one(self) -> None:
        self._tick+=1



    def shift_right(self,game: Game) -> None:
        '''
        function shifts faller to the right if there is nothing blocking it's way
        Then depending on the situation, it may change the state of the faller
        '''
        column = game.current_board()[self._column]
        faller = self._letters
        start = self.index_start(game)
        start_index = column.index(self.state_symbols(faller[2]),start)
        end_index = start_index+3
        if self._column+1 < game.get_columns():
            next_column = game.current_board()[self._column+1]
            if next_column[start_index] == ' ':
                self.check_below(game,next_column, start_index)
                for counter in range(3):
                    next_column[start_index-counter] = column[start_index-counter]
                    column[start_index-counter] = ' '
                
                game.update_column(self._column+1,next_column)
                game.update_column(self._column,column)
                self._column = self._column+1 
            
            

    def shift_left(self,game:Game)-> None:
        '''
        function shifts faller to the left if there is nothing blocking it's way
        Then depending on the situation, it may change the state of the faller
        '''
        column = game.current_board()[self._column]
        faller = self._letters
        start = self.index_start(game)
        start_index = column.index(self.state_symbols(faller[2]),start)
        if self._column -1 >= 0:
            next_column = game.current_board()[self._column-1]
            if next_column[start_index] == ' ':
                self.check_below(game,next_column, start_index)
                for counter in range(3):
                    next_column[start_index-counter] = column[start_index-counter]
                    column[start_index-counter] = ' '
                game.update_column(self._column-1,next_column)
                game.update_column(self._column,column)
                self._column = self._column-1
            
    def check_below(self, game:Game, next_col: int, current_row: int) ->None:
        '''
        checks if there is anything below the faller
        1) if the next row of the next column is empty, the state of the faller
        will be upated to 'falling'
        2) if the nect row of the next column is not empty, the state of the faller
        will be updates to 'landed'
        '''
        if current_row+1 < game.get_rows()+3:
            if  current_row != game.get_rows()+3 and next_col[current_row+1]==' ':
                self._state = 'falling'
                self.falling_sequence(game)
            else:
                self._state = 'landed'
                self.landed_sequence(game)
                
        
