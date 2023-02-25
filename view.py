#Sandra Wang 14772372
import model
import pygame

class ColumnsGame:
    def __init__(self):
        self._state = model.GameState()
        self._running = True

    def run(self) -> None:
        pygame.init()

        try:

            self._resize_surface((600, 600))

            clock = pygame.time.Clock()

            while self._running:
                clock.tick(1)
                self._handle_events()
                self._redraw()
        except model.GameOverError:
            self._running = False
        finally:
            pygame.quit()
            


    def _handle_events(self) -> None:
        '''
        If user presses Q, ten the game ends
        If user presses left arrow key, then faller will shift left
        If user presses right arrow key, then faller will shift right
        If user presses spacebar, then faller will rotate
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self._state.move_left()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self._state.move_right()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._state.rotate()
        self._state.move_faller_tick()

    def _redraw(self) -> None:
        '''
        constantly updates the view and redraws the cells
        '''

        surface = pygame.display.get_surface()

        surface.fill(pygame.Color(255, 255, 0))
        self._draw_cells()

        pygame.display.flip()

    def _draw_cells(self) -> None:
        '''
        draws every cell in cell list
        '''
        for cell in self._state.all_cells():
            self._draw_cell(cell)


    def _draw_cell(self, cell: model.Cell) -> None:
        '''
        given a cell object, draws each cell as a square
        using its attribute
        '''
        top_left_frac_x, top_left_frac_y = cell.get_location()

        width_frac = cell.get_width()
        height_frac = cell.get_height()

        surface = pygame.display.get_surface()

        max_width = surface.get_width()
        max_height = surface.get_height()

        top_left_pixel_x = top_left_frac_x* max_width
        top_left_pixel_y = top_left_frac_y* max_height

        width_pixel = width_frac*max_width
        height_pixel = height_frac*max_height
        
        cell_shape = pygame.Rect(
            top_left_pixel_x, top_left_pixel_y,
            width_pixel, height_pixel)
        color = pygame.Color(cell.get_color_r(),
                             cell.get_color_g(),
                             cell.get_color_b())
        
        pygame.draw.rect(surface,color, cell_shape)

    def _end_game(self) -> None:
        self._running = False


    def _resize_surface(self, size: (int, int)) -> None:
        pygame.display.set_mode(size, pygame.RESIZABLE)


    


    


if __name__ == '__main__':
    ColumnsGame().run()
