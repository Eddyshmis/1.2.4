import turtle as tl
from random import randint
import time
from colorama import Fore, Back, Style
from time import sleep
window = tl.Screen()
print(window.screensize())
# window.setworldcoordinates(0,0,400,300)

maze_drawer = tl.Turtle()
maze_drawer.pensize(10)


def square_draw(multiply):


    

    

    bottom_side = (maze_drawer.xcor() + (10*multiply))
    right_side = (maze_drawer.ycor() + (10*multiply))
    maze_drawer.goto(bottom_side, maze_drawer.ycor())
    maze_drawer.goto(maze_drawer.xcor(), right_side)

    top_side = (maze_drawer.xcor() - (10*multiply))
    left_side = (maze_drawer.ycor() - (10*multiply))
    maze_drawer.goto(top_side, maze_drawer.ycor())
    maze_drawer.goto(maze_drawer.xcor(), left_side)



def test_whiteline(multiply:int,start:int,end:int):
    
    
    full_distance = (maze_drawer.xcor() + (10*multiply))
    print(full_distance)
    # start_distance
    print(full_distance - start)
    maze_drawer.goto(maze_drawer.distance((full_distance - start),maze_drawer.ycor()), maze_drawer.ycor())
    #gap
    
    maze_drawer.pencolor("white")
    gap_distance = maze_drawer.xcor() + maze_drawer.distance(end,maze_drawer.ycor())
    print(gap_distance - full_distance)
    maze_drawer.goto(gap_distance,maze_drawer.ycor())
    # end
    maze_drawer.pencolor("black")
    end_distance = maze_drawer.xcor() + maze_drawer.distance(full_distance,maze_drawer.ycor())
    maze_drawer.goto(end_distance,maze_drawer.ycor())
    


    




def draw_maze(amount,active_turtle):
    size_multi = amount * 5
    print("size_multi:",size_multi)
    for _ in range(amount):
        size_multi -= 4
        square_draw(size_multi)
        active_turtle.up()
        last_x,last_y = active_turtle.pos()
        active_turtle.goto((last_x + 20),(last_y + 20))
        active_turtle.down()
    

def test_fun(func):
    print("\nstart!!")
    start_time = time.time()
    func(maze_drawer,2)
    end_time = time.time()
    print("\ndone!")
    print(Fore.RED + func.__name__,end="")
    print(Style.RESET_ALL)
    print(f"was done in : {end_time - start_time} seconds")

draw_maze(6,maze_drawer)
maze_drawer.speed(1)
# draw_maze(4,maze_drawer)
test_whiteline(20,50,80)

maze_drawer.up()
maze_drawer.goto(-100,-100)
maze_drawer.down()
test_whiteline(20,50,80)


window.listen()
window.mainloop()