from output_logic import Game, Faller, GameOverError
import unittest

class GameTests(unittest.TestCase):
    def setUp(self):
        self._game = Game(7,8)
        self._faller = Faller(['s','t','v'],3,0)
        self._faller_1 = Faller(['v','t','s'],0,0)
        self._faller_2 = Faller(['t','v','s'],1,0)
        self._faller_3 = Faller(['s','v','s'],2,0)
        self._faller_4 = Faller(['s','v','t'],2,0)


    def test_create_game_board(self):
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
    def test_specified_contents(self):
        game_2 = Game(4,4)
        contents = [[' ','y',' ','x'],['s',' ','v',' '],['t','x','y','s'],['x',' ','x','y']]
        game_2.specified_contents(contents)
        self.assertEqual(game_2.current_board(), [[' ',' ',' ',' ','s','t','x'],
                                                  [' ',' ',' ',' ',' ','y','x'],
                                                  [' ',' ',' ',' ','v','y','x'],
                                                  [' ',' ',' ',' ','x','s','y']])
    
    def test_column_filled_true_case(self):
        new_faller  = Faller(['s','t','v'],2,0)
        for times in range(7):
            self._game.time_tick(new_faller)
        for times in range(7):
            self._game.time_tick(self._faller_2)
        for times in range(7):
            self._game.time_tick(self._faller_3)
        for times in range(4):
            self._game.time_tick(self._faller_4)

        self.assertEqual(self._game.column_filled(), True)

    def test_column_filled_false_case(self):
        for times in range(7):
            self._game.time_tick(self._faller_1)
        for times in range(7):
            self._game.time_tick(self._faller_2)
        for times in range(7):
            self._game.time_tick(self._faller_3)
        for times in range(4):
            self._game.time_tick(self._faller_4)

        self.assertEqual(self._game.column_filled(), False)

    def test_game_over(self):
        faller_5 = Faller(['s','t','v'],0,0)
        faller_6 = Faller(['f','r','q'],2,0)
        faller_7 = Faller(['s','m','d'],2,0)
        faller_8 = Faller(['p','g','x'],2,0)
        for times in range(7):
            self._game.time_tick(faller_5)
        for times in range(7):
            self._game.time_tick(faller_6)
        for times in range(4):
            self._game.time_tick(faller_7)
        for times in range(2):
            self._game.time_tick(faller_8)
        self.assertRaises(GameOverError,self._game.game_over)
   
        

    def test_check_match_board_double_layer(self):
        for times in range(8):
            self._game.time_tick(self._faller_1)
        for times in range(8):
            self._game.time_tick(self._faller_2)
        for times in range(8):
            self._game.time_tick(self._faller_3)
        for times in range(5):
            self._game.time_tick(self._faller_4)


        self._game.mark_all_matches_board()
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ','v','*t*','*s*'],
                                                      [' ',' ',' ',' ',' ',' ',' ','*t*','v','*s*'],
                                                      [' ',' ',' ',' ','s','v','*t*','s','v','*s*'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        
        

    def test_is_match(self):
    
        for times in range(8):
            self._game.time_tick(self._faller_1)
        for times in range(8):
            self._game.time_tick(self._faller_2)
        for times in range(8):
            self._game.time_tick(self._faller_3)
        for times in range(5):
            self._game.time_tick(self._faller_4)

        self.assertEqual(self._game._is_match(0,9),[(1,0,2)])
        match_list_2 = self._game._is_match(0,8)
        self.assertEqual(self._game._is_match(0,8), [(1,-1,2)])

    def test_mark_all_matches(self):
        for times in range(8):
            self._game.time_tick(self._faller_1)
        for times in range(8):
            self._game.time_tick(self._faller_2)
        for times in range(8):
            self._game.time_tick(self._faller_3)
        for times in range(5):
            self._game.time_tick(self._faller_4)

        self._game.mark_all_matches_board()
        self.assertEqual(self._game.current_board(),[[' ',' ',' ',' ',' ',' ',' ','v','*t*','*s*'],
                                                      [' ',' ',' ',' ',' ',' ',' ','*t*','v','*s*'],
                                                      [' ',' ',' ',' ','s','v','*t*','s','v','*s*'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']] )
    def test_delete_match(self):
        for times in range(8):
            self._game.time_tick(self._faller_1)
        for times in range(8):
            self._game.time_tick(self._faller_2)
        for times in range(8):
            self._game.time_tick(self._faller_3)
        for times in range(5):
            self._game.time_tick(self._faller_4)

        self._game.mark_all_matches_board()
        self._game.delete_match()
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ','v'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ','v'],
                                                      [' ',' ',' ',' ',' ',' ','s','v','s','v'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']] )
        


       
    def test_board_contains_stars_true_case(self):
        for times in range(8):
            self._game.time_tick(self._faller_1)
        for times in range(8):
            self._game.time_tick(self._faller_2)
        for times in range(8):
            self._game.time_tick(self._faller_3)
        for times in range(5):
            self._game.time_tick(self._faller_4)

        self._game.mark_all_matches_board()
        self.assertEqual(self._game.board_contains_stars(),True)

    def test_board_contains_stars_false_case(self):
        faller_5 = Faller(['s','t','v'],0,0)
        faller_6 = Faller(['r','r','q'],1,0)
        faller_7 = Faller(['s','m','d'],2,0)
        faller_8 = Faller(['p','s','d'],3,0)
        for times in range(8):
            self._game.time_tick(faller_5)
        for times in range(8):
            self._game.time_tick(faller_6)
        for times in range(8):
            self._game.time_tick(faller_7)
        for times in range(8):
            self._game.time_tick(faller_8)

        self._game.mark_all_matches_board()
        self.assertEqual(self._game.board_contains_stars(),False)
        

    def test_mark_all_matching_single_layer(self):
    

        for times in range(8):
            self._game.time_tick(self._faller_1)
        for times in range(8):
            self._game.time_tick(self._faller_2)
        for times in range(8):
            self._game.time_tick(self._faller_3)
        for times in range(5):
            self._game.time_tick(self._faller_4)


        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ','v','*t*','*s*'],
                                                      [' ',' ',' ',' ',' ',' ',' ','*t*','v','*s*'],
                                                      [' ',' ',' ',' ','s','v','*t*','s','v','*s*'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']] )

        

        
    

    def test_three_or_more_match_method_empty_start_cell(self):
        second_faller = Faller(['p','t','v'],2,0)
        third_faller = Faller(['r','x','v'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(0,9,1,0), 0)

    def test_three_or_more_match_method_up_vertical_match(self):
        second_faller = Faller(['s','s','v'],1,0)
        third_faller = Faller(['r','x','s'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(5):
            self._game.time_tick(third_faller)
            
        
        self.assertEqual(self._game._three_or_more_match(1,8,0,-1), 2)

    def test_three_or_more_match_method_down_vertical_match(self):
        second_faller = Faller(['s','s','v'],1,0)
        third_faller = Faller(['r','x','s'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(5):
            self._game.time_tick(third_faller)
            
        
        self.assertEqual(self._game._three_or_more_match(1,6,0,1), 2)
    
       
    def test_three_or_more_match_method_left_horizontal_match(self):
        second_faller = Faller(['p','t','v'],2,0)
        third_faller = Faller(['r','x','v'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(3,9,-1,0), 2)

    def test_three_or_more_match_method_right_horizontal_match(self):
        second_faller = Faller(['p','t','v'],2,0)
        third_faller = Faller(['r','x','v'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(1,9,1,0), 2)

    def test_three_or_more_match_method_up_right_diagonal_match(self):
        second_faller = Faller(['t','s','v'],2,0)
        third_faller = Faller(['v','t','s'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(1,9,1,-1), 2)



    def test_three_or_more_match_method_down_right_diagonal_match(self):
        second_faller = Faller(['p','v','r'],2,0)
        third_faller = Faller(['v','x','x'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(1,7,1,1), 2)

       
    def test_three_or_more_match_method_main_up_left_diagonal_match(self):
        second_faller = Faller(['t','v','s'],2,0)
        third_faller = Faller(['v','t','s'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(3,9,-1,-1), 2)

    def test_three_or_more_match_method_main_down_left_diagonal_match(self):
        second_faller = Faller(['t','s','v'],2,0)
        third_faller = Faller(['v','t','s'],1,0)
        for times in range(8):
            self._game.time_tick(self._faller)
        for times in range(8):
            self._game.time_tick(second_faller)
        for times in range(8):
            self._game.time_tick(third_faller)
        self.assertEqual(self._game._three_or_more_match(3,7,-1,1), 2)
        
  
    def test_tick_and_set_state_function(self):
        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'falling')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'falling')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'falling')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'falling')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'falling')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'falling')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'landed')

        self._game.time_tick(self._faller)
        self.assertEqual(self._faller.get_state(), 'frozen')
    


    def test_tick_and_symbols_of_updated_board(self):
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[s]','[t]','[v]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(),[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ','[s]','[t]','[v]',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ','[s]','[t]','[v]',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ','[s]','[t]','[v]',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ','[s]','[t]','[v]',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ','|s|','|t|','|v|'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._game.time_tick(self._faller)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ','s','t','v'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])

    def test_tick_function_stacking_fallers(self):
        second_faller = Faller(['p','t','v'],3,0)
        for i in range(8):
            self._game.time_tick(self._faller)

        for n in range(8):
            self._game.time_tick(second_faller)

        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ','p','t','v','s','t','v'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
            

class FallerTests(unittest.TestCase):
    def setUp(self):
        self._game = Game(7,8)
        self._game_2 = Game(5,6)
        self._faller = Faller(['s','t','v'], 3, 0)
        self._faller_2 = Faller(['s','s','t'],0, 0)
        self._faller_3 = Faller(['s','t','s'],0, 0)

    


    def test_index_start_method(self):
        self._game.time_tick(self._faller_2)
        self.assertEqual(self._faller_2.index_start(self._game), 0)
        
        self._game_2.time_tick(self._faller_3)
        self.assertEqual(self._faller_3.index_start(self._game), 2)
        

    def test_add_fallers_method(self):
        pass

    def test_rotate_method(self):
        self._game.time_tick(self._faller)
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[v]','[s]','[t]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[t]','[v]','[s]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[s]','[t]','[v]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])

    def test_rotate_with_gravity(self):
        
        self._game.time_tick(self._faller)
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[v]','[s]','[t]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[t]','[v]','[s]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[s]','[t]','[v]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self._faller.rotate(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[v]','[s]','[t]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])

    def test_shift_right_method(self):
        self._game.time_tick(self._faller)
        self._faller.shift_right(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[s]','[t]','[v]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        
        self._game.time_tick(self._faller)
        self._faller.shift_right(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        
        self._faller.shift_right(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_right(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' ']])
        self._faller.shift_right(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' ']])


    def test_shift_left_method(self):
        self._game.time_tick(self._faller)
        self._faller.shift_left(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[s]','[t]','[v]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        
        self._game.time_tick(self._faller)
        self._faller.shift_left(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        
        self._faller.shift_left(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_left(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])

    
    def test_update_letters_method(self):
        pass
    


    def test_shift_down_method(self):
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ','[s]','[t]','[v]',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(),[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ','[s]','[t]','[v]',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ','[s]','[t]','[v]',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ','[s]','[t]','[v]',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ','[s]','[t]','[v]',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ','[s]','[t]','[v]',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ','[s]','[t]','[v]'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])
        self._faller.shift_down(self._game)
        self.assertEqual(self._game.current_board(), [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ','[s]','[t]','[v]'],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                                                      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']])


    
        
        

if __name__ == '__main__':
    unittest.main()
