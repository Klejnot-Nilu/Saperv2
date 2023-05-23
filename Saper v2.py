import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.mines = []
        self.generate_mines()
    
    def generate_mines(self):
        positions = [(x, y) for x in range(self.width) for y in range(self.height)]
        self.mines = random.sample(positions, self.num_mines)
    
    def play(self):
        print("Welcome to Minesweeper!")
        print("Uncover cells to find all non-mine cells.")
        print("Enter the x and y coordinates to make a move.")
        print("Let's begin!")
        
        game_over = False
        while not game_over:
            self.print_board()
            x, y = self.get_move()
            if (x, y) in self.mines:
                print("Game over! You hit a mine.")
                game_over = True
            else:
                self.update_board(x, y)
                if self.is_board_complete():
                    print("Congratulations! You won!")
                    game_over = True
    
    def print_board(self):
        print("Current board:")
        print('  ' + ' '.join([str(i) for i in range(self.width)]))
        print('  ' + '- ' * self.width)
        for i, row in enumerate(self.board):
            print(f'{i}|' + ' '.join(row))
        print()
    
    def get_move(self):
        while True:
            try:
                x = int(input("Enter the x-coordinate: "))
                y = int(input("Enter the y-coordinate: "))
                if 0 <= x < self.width and 0 <= y < self.height:
                    return x, y
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
    
    def update_board(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (x + dx, y + dy) in self.mines:
                    count += 1
        self.board[y][x] = str(count)
    
    def is_board_complete(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

# Prompt user for board dimensions
width = int(input("Enter the number of columns: "))
height = int(input("Enter the number of rows: "))
num_mines = int(input("Enter the number of mines: "))

# Play the game
game = Minesweeper(width, height, num_mines)
game.play()
