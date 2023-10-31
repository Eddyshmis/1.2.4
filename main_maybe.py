import turtle as tl
from random import randint
import time
from colorama import Fore, Back, Style
from time import sleep
window = tl.Screen()
print(window.screensize())
# window.setworldcoordinates(0,0,400,300)

maze_drawer = tl.Turtle()
maze_drawer.pensize(4)


def square_draw(multiply,white_space_start,white_space_end):

    distance = maze_drawer.xcor() + (10*multiply)

    
    for _ in range(4):
        start_distance = abs(distance - white_space_start)
        gap_distance = abs(white_space_start - white_space_end)
        end_distance = abs(distance - (start_distance + gap_distance))
        
        maze_drawer.forward(start_distance)
        maze_drawer.pencolor("white")
        maze_drawer.forward(gap_distance)
        maze_drawer.pencolor("black")
        maze_drawer.forward(end_distance)
        maze_drawer.right(90)
    






    




def draw_maze(amount):
    size_multi = amount * 5
    for _ in range(amount):
        size_multi -= 6
        square_draw(size_multi,50,80)
        maze_drawer.up()
        maze_drawer.goto((maze_drawer.xcor() + 20),(maze_drawer.ycor() - 20))
        maze_drawer.down()
    
    

def test_fun(func):
    print("\nstart!!")
    start_time = time.time()
    func(maze_drawer,2)
    end_time = time.time()
    print("\ndone!")
    print(Fore.RED + func.__name__,end="")
    print(Style.RESET_ALL)
    print(f"was done in : {end_time - start_time} seconds")


maze_drawer.speed(4)
draw_maze(10)



window.listen()
window.mainloop()