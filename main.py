import pygame
import random

class Game:

    """
    Class representing the 2048 game.
    
    :attributes:
        - GRID_SIZE (int): The size of the game grid.
        - GRID_WIDTH (int): The width of the game grid in pixels.
        - GRID_HEIGHT (int): The height of the game grid in pixels.
        - TILE_SIZE (int): The size of each tile in pixels.
        - WHITE (tuple): RGB tuple representing the color white.
        - BLACK (tuple): RGB tuple representing the color black.
        - GRAY (tuple): RGB tuple representing the color gray.
        - FONT_SIZE (int): The size of the font for text display.
        - screen (pygame.Surface): The Pygame surface representing the game window.
        - colors (dict): Dictionary mapping tile values to their respective colors.
        - grid (list): 2D list representing the game grid.
    """


    def __init__(self):
        """
        Initializes the game.
        """
        # Initialize Pygame
        pygame.init()

        # Game parameters
        self.GRID_SIZE = 4
        self.GRID_WIDTH = 400
        self.GRID_HEIGHT = 400
        self.TILE_SIZE = self.GRID_WIDTH // self.GRID_SIZE
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.FONT_SIZE = 40

        # Initialize the screen
        self.screen = pygame.display.set_mode((self.GRID_WIDTH, self.GRID_HEIGHT))
        pygame.display.set_caption('2048')

        # Colors for different tile values
        self.colors = {
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)
        }

        # Initialize the game board
        self.grid = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]

        # Generate empty tiles
        for _ in range(2):
            self.generate_tile()

    def generate_tile(self):
        """
        Generates a new tile on a random empty cell of the field.
        """
        empty_cells = [(i, j) for i in range(self.GRID_SIZE) for j in range(self.GRID_SIZE) if not self.grid[i][j]]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
            print(f"A new tile was generated at position ({i}, {j}) with value {self.grid[i][j]}")
        else:
            print("No empty cells to generate a new tile.")

    def draw_grid(self):
        """
        Displays the game grid.
        """
        for i in range(self.GRID_SIZE + 1):
            pygame.draw.line(self.screen, self.BLACK, (i * self.TILE_SIZE, 0), (i * self.TILE_SIZE, self.GRID_HEIGHT))
            pygame.draw.line(self.screen, self.BLACK, (0, i * self.TILE_SIZE), (self.GRID_WIDTH, i * self.TILE_SIZE))

    def draw_tiles(self):
        """
        Displays the tiles of the game board.
        """
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                tile = self.grid[i][j]
                if tile:
                    color = self.colors.get(tile, self.GRAY)
                    pygame.draw.rect(self.screen, color, (j * self.TILE_SIZE + 1, i * self.TILE_SIZE + 1, self.TILE_SIZE - 1, self.TILE_SIZE - 1))

                    # Calculate the position of the text to center it in the tile
                    text = str(tile)
                    text_x = j * self.TILE_SIZE + self.TILE_SIZE // 2
                    text_y = i * self.TILE_SIZE + self.TILE_SIZE // 2
                    self.draw_text(text, text_x, text_y, self.BLACK, self.FONT_SIZE)

    def draw_text(self, text, x, y, color, font_size):
        """
        Displays text on the screen.

        :param text: The text to be displayed.
        :param x: The X position to display the text.
        :param y: The Y position to display the text.
        :param color: The color of the text.
        :param font_size: The size of the font.
        """
        font = pygame.font.Font(None, font_size)
        surface = font.render(text, True, color)
        text_rect = surface.get_rect(center=(x, y))
        self.screen.blit(surface, text_rect)

    def move_up(self):
        """
        Moves the tiles up.
        """
        for j in range(self.GRID_SIZE):
            for i in range(1, self.GRID_SIZE):
                if self.grid[i][j] != 0:
                    k = i
                    while k > 0 and self.grid[k - 1][j] == 0:
                        k -= 1
                    if k > 0 and self.grid[k - 1][j] == self.grid[i][j]:
                        self.grid[k - 1][j] *= 2
                        self.grid[i][j] = 0
                    elif k < i:
                        self.grid[k][j] = self.grid[i][j]
                        if k != i:
                            self.grid[i][j] = 0

    def move_down(self):
        """
        Moves the tiles down.
        """
        for j in range(self.GRID_SIZE):
            for i in range(self.GRID_SIZE - 2, -1, -1):
                if self.grid[i][j] != 0:
                    k = i
                    while k < self.GRID_SIZE - 1 and self.grid[k + 1][j] == 0:
                        k += 1
                    if k < self.GRID_SIZE - 1 and self.grid[k + 1][j] == self.grid[i][j]:
                        self.grid[k + 1][j] *= 2
                        self.grid[i][j] = 0
                    elif k > i:
                        self.grid[k][j] = self.grid[i][j]
                        if k != i:
                            self.grid[i][j] = 0

    def move_left(self):
        """
        Moves the tiles left.
        """
        for i in range(self.GRID_SIZE):
            for j in range(1, self.GRID_SIZE):
                if self.grid[i][j] != 0:
                    k = j
                    while k > 0 and self.grid[i][k - 1] == 0:
                        k -= 1
                    if k > 0 and self.grid[i][k - 1] == self.grid[i][j]:
                        self.grid[i][k - 1] *= 2
                        self.grid[i][j] = 0
                    elif k < j:
                        self.grid[i][k] = self.grid[i][j]
                        if k != j:
                            self.grid[i][j] = 0

    def move_right(self):
        """
        Moves the tiles right.
        """
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE - 2, -1, -1):
                if self.grid[i][j] != 0:
                    k = j
                    while k < self.GRID_SIZE - 1 and self.grid[i][k + 1] == 0:
                        k += 1
                    if k < self.GRID_SIZE - 1 and self.grid[i][k + 1] == self.grid[i][j]:
                        self.grid[i][k + 1] *= 2
                        self.grid[i][j] = 0
                    elif k > j:
                        self.grid[i][k] = self.grid[i][j]
                        if k != j:
                            self.grid[i][j] = 0

    def game_over(self):
        """
        Checks if the game is over.

        :return: - True if the game is over, otherwise False.
        """
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if not self.grid[i][j]:
                    return False
                if j < self.GRID_SIZE - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
                if i < self.GRID_SIZE - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
        return True

    def game_over_screen(self):
        """
        Displays the game over screen with options to play again or quit.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return True
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            self.screen.fill(self.WHITE)
            self.draw_text("Game Over!", self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2 - 50, self.BLACK, self.FONT_SIZE)
            self.draw_text("Play Again (P)", self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2, self.BLACK, self.FONT_SIZE)
            self.draw_text("Quit (Q)", self.GRID_WIDTH // 2, self.GRID_HEIGHT // 2 + 50, self.BLACK, self.FONT_SIZE)
            pygame.display.flip()

def main():
    """
    Main function to run the 2048 game.
    """
    # Create an instance of the Game class
    game = Game()
    running = True
    while running:
        try:
            game.screen.fill(game.WHITE)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    grid_before_move = [row.copy() for row in game.grid]
                    if event.key == pygame.K_UP:
                        game.move_up()
                    elif event.key == pygame.K_DOWN:
                        game.move_down()
                    elif event.key == pygame.K_LEFT:
                        game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        game.move_right()

                    # Move tiles and generate a new one if the field has changed
                    if game.grid != grid_before_move and not game.game_over():
                        game.generate_tile()

            # Draw the grid and tiles
            game.draw_grid()
            game.draw_tiles()

            # Display changes
            pygame.display.flip()

            # Check if the game is over
            if game.game_over():
                print("Game Over!")
                if game.game_over_screen():  # If the player chooses to play again
                    # Reset the game board
                    game.grid = [[0] * game.GRID_SIZE for _ in range(game.GRID_SIZE)]
                    # Generate new tiles
                    for _ in range(2):
                        game.generate_tile()
        except Exception as e:
            print(f"An error occurred: {e}")
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
