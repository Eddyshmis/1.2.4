import turtle as tl
from random import randint
import time
from colorama import Fore, Back, Style
from time import sleep
window = tl.Screen()
print(window.screensize())
window.setup(width=800,height=800)
# window.setworldcoordinates(0,-400,800,400)

maze_drawer = tl.Turtle()
maze_drawer.pensize(5)



    






    




def draw_maze(size,white_size):
    # start_distance = abs(distance - white_space_start)
    def wall_left(size):
        maze_drawer.left(90)
        maze_drawer.forward(size)
        maze_drawer.back(size)
        maze_drawer.right(90)
    def wall_right(size):
        maze_drawer.right(90)
        maze_drawer.forward(size)
        maze_drawer.back(size)
        maze_drawer.left(90)
    distance = 0
    need_opening = False
    for i in range(size):
        distance += 5
        if i < 3:
            maze_drawer.forward(distance)
            maze_drawer.forward(white_size)
            maze_drawer.forward(distance)
            maze_drawer.right(90)
        else:
            maze_drawer.forward(distance)
            choice = randint(0,2)
            if choice == 1:
                wall_left(17)
                maze_drawer.up()
                need_opening = False

            elif choice == 0:
                wall_right(17)
                maze_drawer.up()
                need_opening = False
            else:
                need_opening = True
                pass



            # maze_drawer.up()
            maze_drawer.forward(white_size)
            maze_drawer.down()
            maze_drawer.forward(distance)
            maze_drawer.right(90)
    
    
    

def test_fun(func):
    print("\nstart!!")
    start_time = time.time()
    func(maze_drawer,2)
    end_time = time.time()
    print("\ndone!")
    print(Fore.RED + func.__name__,end="")
    print(Style.RESET_ALL)
    print(f"was done in : {end_time - start_time} seconds")

draw_maze(20,30)

window.listen()
window.mainloop()