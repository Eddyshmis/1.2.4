import turtle as tl
import time
from colorama import Fore, Back, Style
window = tl.Screen()
maze_drawer = tl.Turtle()
size_multiplier = 20
maze_drawer.pensize(10)
maze_drawer.speed(8)
# maze_drawer.shape("circle")
maze_drawer.color("red")
maze_drawer.pencolor("black")
start_white = 40
end_white = 100

def rectangle_draw_pix(active_turtle):
    new_x = active_turtle.xcor() + (10*size_multiplier)
    for i in range(round(new_x)):
        # range start and end of white
        # problem when setting up (for going down) you would need multiple diffrent var's to count the px's for white, since range of i would vary due to pos
        if i > start_white and i < end_white:
            active_turtle.pencolor("white")
        else:
            active_turtle.pencolor("black")
        
        active_turtle.goto(i,active_turtle.ycor())
    
    new_y = active_turtle.ycor() - (10*size_multiplier)
    for i in range(round(active_turtle.ycor()),round(new_y),-1):
        active_turtle.goto(active_turtle.xcor(),i)





    # active_turtle.goto((active_turtle.xcor() + (10*size_multiplier)),active_turtle.ycor())
    # active_turtle.goto(active_turtle.xcor(),(active_turtle.ycor() - (10*size_multiplier)))
    # active_turtle.goto((active_turtle.xcor() - (10*size_multiplier)),active_turtle.ycor())
    # active_turtle.goto(active_turtle.xcor(),(active_turtle.ycor() + (10*size_multiplier)))




def rectangle_draw_basic(active_turtle):
    side_size = (10*size_multiplier)
    for _ in range(4):
        active_turtle.forward(side_size)
        active_turtle.right(90)




def test_fun(func):
    print("\nstart!!")
    start_time = time.time()
    func(maze_drawer)
    end_time = time.time()
    print("\ndone!")
    print(Fore.RED + func.__name__,end="")
    print(Style.RESET_ALL)
    print(f"was done in : {end_time - start_time} seconds")

test_fun(rectangle_draw_basic)

# test_fun(rectangle_draw_pix)




window.mainloop()