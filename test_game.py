import pytest
from main import Game

class TestGame:
    """
    A class to test the Game class methods.

    :attributes:
        - None
    """

    @pytest.fixture
    def game(self):
        """
        A fixture to create an instance of the Game class for each test method.

        :return:
            - Game: An instance of the Game class.
        """
        return Game()

    def test_initial_grid_size(self, game):
        """
        Test case to ensure that the initial grid size is correct.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        assert len(game.grid) == game.GRID_SIZE
        for row in game.grid:
            assert len(row) == game.GRID_SIZE

    def test_generate_tile(self, game):
        """
        Test case to ensure that the generate_tile method generates tiles properly.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        game.generate_tile()
        empty_cells = sum(1 for row in game.grid for cell in row if cell == 0)
        assert empty_cells == 13  # Since two tiles have been generated initially

    def test_move_up(self, game):
        """
        Test case to ensure that the move_up method moves tiles upwards properly.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        initial_grid = [row.copy() for row in game.grid]
        game.move_up()
        assert game.grid != initial_grid  # Check if grid has changed after move

    def test_move_down(self, game):
        """
        Test case to ensure that the move_down method moves tiles downwards properly.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        initial_grid = [row.copy() for row in game.grid]
        game.move_down()
        assert game.grid != initial_grid  # Check if grid has changed after move

    def test_move_left(self, game):
        """
        Test case to ensure that the move_left method moves tiles left properly.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        initial_grid = [row.copy() for row in game.grid]
        game.move_left()
        assert game.grid != initial_grid  # Check if grid has changed after move

    def test_move_right(self, game):
        """
        Test case to ensure that the move_right method moves tiles right properly.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        initial_grid = [row.copy() for row in game.grid]
        game.move_right()
        assert game.grid != initial_grid  # Check if grid has changed after move

    def test_game_over(self, game):
        """
        Test case to ensure that the game_over method correctly detects game over.

        :arguments:
            - game (Game): An instance of the Game class.

        :return:
            - None
        """
        game.grid = [[2, 4, 2, 4],
                     [4, 2, 4, 2],
                     [2, 4, 2, 4],
                     [4, 2, 4, 2]]
        assert game.game_over()

    def test_game_over_screen_play_again(self, game, monkeypatch):
        """
        Test case to ensure that the game_over_screen method returns True if the player chooses to play again.

        :arguments:
            - game (Game): An instance of the Game class.
            - monkeypatch: Pytest monkeypatch fixture.

        :return:
            - None
        """
        # Mocking user input to simulate 'p' key press
        monkeypatch.setattr('builtins.input', lambda _: 'p')
        assert game.game_over_screen() == True


    def test_game_over_screen(self, game, monkeypatch):
        """
        Test case to ensure that the game_over_screen method ends the game after the user clicked 'q'.

        :arguments:
            - game (Game): An instance of the Game class.
            - monkeypatch: Pytest monkeypatch fixture.

        :return:
            - None
        """
        # Mocking user input to simulate 'q' key press
        monkeypatch.setattr('builtins.input', lambda _: 'q')
        with pytest.raises(SystemExit):
            game.game_over_screen()

if __name__ == "__main__":
    pytest.main()
