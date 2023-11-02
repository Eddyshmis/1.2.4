import turtle as tl
from random import randint
import os
import time
try:
    from colorama import Fore,Style
except:
    os.system("pip install colorama")
    from colorama import Fore,Style

window = tl.Screen()
window.setup(width=800,height=800)

window.tracer(1,0)
maze_drawer = tl.Turtle()
maze_drawer.pensize(5)
maze_drawer.speed(0)
timer = tl.Turtle()
width,hight = window.screensize()
timer.up()
timer.goto((width - 150),(hight - 5))
current_time = 0
set_timer = 40

def draw_maze(size,white_size):
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
    distance = 5
    def draw_walls():
                gap_rand = randint(0,4)
                if gap_rand == 0:
                    maze_drawer.up()
                    maze_drawer.forward(white_size)
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                elif gap_rand == 1:
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.up()
                    maze_drawer.forward(white_size)
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                elif gap_rand == 2:
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.up()
                    maze_drawer.forward(white_size)
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                elif gap_rand == 3:
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.up()
                    maze_drawer.forward(white_size)
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                elif gap_rand == 4:
                    maze_drawer.down()
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(white_size)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
    for i in range(size):
        distance += 5

        if i < 6:

            maze_drawer.forward(distance)
            maze_drawer.forward(white_size)
            maze_drawer.forward(distance)
            maze_drawer.right(90)
        elif i > (size - 6):
            maze_drawer.forward(distance)
            maze_drawer.forward(white_size)
            maze_drawer.forward(distance)
            maze_drawer.right(90)
        else:
            wall_rand = randint(0,2)
            maze_drawer.forward(distance/4)
            maze_drawer.forward(distance/4)
            if wall_rand == 0:
                 

                choice = randint(0,2)
                if choice == 1:
                    wall_left(17)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)

                elif choice == 0:
                    wall_right(17)
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                else:
                    maze_drawer.forward(distance/4)
                    maze_drawer.forward(distance/4)
                    pass
            if wall_rand == 1:
                 
                maze_drawer.forward(distance/4)
                
                choice = randint(0,2)
                if choice == 1:
                    maze_drawer.forward(distance/4)
                    wall_left(17)
                    
    
                elif choice == 0:
                    maze_drawer.forward(distance/4)
                    wall_right(17)
                    
                else:
                    maze_drawer.forward(distance/4)
                    pass
            if wall_rand == 2:
                 
                maze_drawer.forward(distance/4)
                
                choice = randint(0,2)
                if choice == 1:

                    wall_left(17)
                    maze_drawer.forward(distance/4)

                elif choice == 0:

                    wall_right(17)
                    maze_drawer.forward(distance/4)

                    
                else:
                    maze_drawer.forward(distance/4)
                    pass

            
            draw_walls()
            

            maze_drawer.right(90)
    

def play_maze():
    
    # list_keys = ["w","a","s","d"]
    
    
    player.speed(0)
    movement_speed = 3
    def move_up():
        player.seth(90)
        player.forward(movement_speed)
    def move_down():
        player.seth(270)
        player.forward(movement_speed)
    def move_left():
        player.seth(180)
        player.forward(movement_speed)

    def move_right():
        player.seth(0)
        player.forward(movement_speed)




    tl.onkeypress(move_up,"w")
    tl.onkeypress(move_left,"a")
    tl.onkeypress(move_down,"s")
    tl.onkeypress(move_right,"d")
    timer.hideturtle()

    def count_time():
        global current_time,set_timer
        current_time += 1
        timer.clear()
        timer.write(f"Timer:{current_time}",False,"center",("Arial",20,"normal"))
        if current_time >= set_timer:
            tl.onkeypress(None,"w")
            tl.onkeypress(None,"a")
            tl.onkeypress(None,"s")
            tl.onkeypress(None,"d")
            player.hideturtle()
            timer.clear()
            timer.write("TIME IS UP!",False,"center",("Arial",20,"normal"))
            maze_drawer.clear()
            player.clear()
            maze_drawer.up()
            maze_drawer.goto(0,0)
            player.up()
            player.goto(0,0)
            player.down()
            maze_drawer.down()
            start_turtle.showturtle()
            start_turtle.write("Click circle to start!",False,"center",("Arial",20,"normal"))
            pass
        else:
            window.ontimer(count_time,1000)

    count_time()
    

def test_func(func):
    print("\nstart!!")
    start_time = time.time()
    func(60,30)
    end_time = time.time()
    print("\ndone!")
    print(Fore.RED + func.__name__,end="")
    print(Style.RESET_ALL)
    print(f"was done in : {end_time - start_time} seconds")

def run_everything(x,y):
    global current_time
    current_time = 0
    start_turtle.clear()
    for turlte in tl.turtles():
        turlte.showturtle()
    start_turtle.hideturtle()
    test_func(draw_maze)
    play_maze()

player = tl.Turtle()

start_turtle = tl.Turtle()
start_turtle.shape("circle")

for turlte in tl.turtles():
    turlte.hideturtle()
start_turtle.showturtle()
start_turtle.write("Click circle to start!",False,"center",("Arial",20,"normal"))
start_turtle.onclick(run_everything)





window.listen()
window.mainloop()