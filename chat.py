import turtle

# Initialize Turtle
t = turtle.Turtle()
screen = turtle.Screen()

# Set up grid parameters
rows = 10
columns = 10
cell_size = 20

# Create a grid of cells
def draw_grid():
    for i in range(rows):
        for j in range(columns):
            x = j * cell_size
            y = i * cell_size
            screen.tracer(0)
            t.penup()
            t.goto(x, y)
            t.pendown()
            for _ in range(4):
                t.forward(cell_size)
                t.right(90)
            screen.tracer(1)

# Depth-First Search algorithm to generate maze
def dfs(x, y):
    if 0 <= x < columns and 0 <= y < rows and grid[y][x] == 1:
        grid[y][x] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            t.penup()
            t.goto(x * cell_size, y * cell_size)
            t.pendown()
            if dx == 1:
                t.goto((x + 1) * cell_size, y * cell_size)
            elif dx == -1:
                t.goto((x - 1) * cell_size, y * cell_size)
            elif dy == 1:
                t.goto(x * cell_size, (y + 1) * cell_size)
            elif dy == -1:
                t.goto(x * cell_size, (y - 1) * cell_size)
            dfs(x + dx, y + dy)

# Initialize grid
grid = [[1 for _ in range(columns)] for _ in range(rows)]

# Start DFS from a random cell
import random
start_x, start_y = random.randint(0, columns-1), random.randint(0, rows-1)
dfs(start_x, start_y)

# Draw the grid
draw_grid()

# Hide turtle and display the result
t.hideturtle()
screen.mainloop()
