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


def square_draw(multiply,white_space):


    

    

    bottom_side = (maze_drawer.xcor() + (10*multiply))
    right_side = (maze_drawer.ycor() + (10*multiply))
    maze_drawer.goto(bottom_side, maze_drawer.ycor())
    maze_drawer.goto(maze_drawer.xcor(), right_side)

    top_side = (maze_drawer.xcor() - (10*multiply))
    left_side = (maze_drawer.ycor() - (10*multiply))
    maze_drawer.goto(top_side, maze_drawer.ycor())
    maze_drawer.goto(maze_drawer.xcor(), left_side)



def test_whiteline(start,end):
    # multiplyer = 20
    # distance = (maze_drawer.xcor() + (10*multiplyer))
    # while(distance != maze_drawer.xcor()):
    #     maze_drawer.forward(1)
        # if maze_drawer
    print(maze_drawer.xcor())
    multiplyer = 20
    full_distance = (maze_drawer.xcor() + (10*multiplyer))

    start_distance = full_distance - maze_drawer.distance(start)

    maze_drawer.goto(start_distance, maze_drawer.ycor())
    maze_drawer.pencolor("white")
    print(maze_drawer.xcor())
    sleep(3)
    continue_distance = maze_drawer.distance(full_distance,maze_drawer.ycor())

    gap_distance = continue_distance - start_distance
    maze_drawer.goto(gap_distance,maze_drawer.ycor())
    print(maze_drawer.xcor())
    sleep(3)

    maze_drawer.pencolor("black")
    maze_drawer.goto((maze_drawer.xcor() + continue_distance),maze_drawer.ycor())
    print(full_distance,start_distance,continue_distance,gap_distance)
    print(maze_drawer.xcor())
    sleep(3)
    print("\n",maze_drawer.distance(200,0))

    # continue_distance = full_distance - (full_distance - end)
    # maze_drawer.goto(continue_distance,maze_drawer.ycor())
    # print(maze_drawer.xcor())

    




def draw_maze(amount,active_turtle):
    size_multi = amount * 5
    for _ in range(amount):
        size_multi -= 4
        square_draw(size_multi,1)
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


maze_drawer.speed(1)
# draw_maze(4,maze_drawer)
test_whiteline(50,80)

window.listen()
window.mainloop()