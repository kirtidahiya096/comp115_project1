import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()                                            # Created a turtle object names pen 
pen.speed(0)
pen.width(3)


def draw_square(size, color):                                   # Using square function with size and color as parameter                           
    pen.color(color)
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

def draw_circle(radius, color):                                 # Using circle function with radius and color as parameter 
    pen.color(color)
    pen.begin_fill()                                            # Starting the fill color of circle 
    pen.circle(radius)
    pen.end_fill()

def move_to(x, y):                                              # Moving the pen to coordinates x and y without drawing 
    pen.up()
    pen.goto(x, y)
    pen.down()


def draw_ground():                                              # Trying to draw the ground in the scene 
    move_to(-400, -150)                                         # Moving the pen to the bottom left corner to start drawing the ground 
    pen.color("green")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(800)
        pen.right(90)
        pen.forward(250)
        pen.right(90)
    pen.end_fill()                                                   # Fills the rectangle with green color to represent the ground 

def draw_sun(x=200, y=120, radius=50):                               # Trying to draw sun in the sky 
    move_to(x, y-radius)                                             # Moving the pen to top right in sky 
    draw_circle(radius, "yellow")                                    # Draw an yellow circle with radius 50 

def draw_sun_rays(x=200, y=120, radius=50, num_rays=12, ray_length=30):
    move_to(x, y)
    pen.setheading(0)
    for _ in range(num_rays):
        pen.up()
        pen.forward(radius)
        pen.down()
        pen.forward(ray_length)
        pen.up()
        pen.backward(radius + ray_length)
        pen.left(360 / num_rays) 
 
def draw_bird(x, y, size=20):                                          # Trying to draw birds           
    move_to(x, y) 
    pen.color("black")
    pen.setheading(45) 
    pen.down()
    pen.forward(size)
    pen.backward(size)
    pen.setheading(135)
    pen.forward(size)
    pen.backward(size)
    pen.up()       

def draw_tree(x, y):                                                 # Trying to draw trees 
    move_to(x, y) 
    pen.color("brown")                                               # Drawing the thrunk of tree 
    pen.begin_fill()                 
    for _ in range(2):
        pen.forward(20)                                         
        pen.left(90)
        pen.forward(60)
        pen.left(90)
    pen.end_fill()

    trunk_center_x = x + 10 
    trunk_top_y = y + 60 
    move_to(trunk_center_x, trunk_top_y)                                   
    draw_circle(50, "green")


def draw_flower(x, y):                                          # Tring to draw flowers on the ground 
    move_to(x, y)
    colors = ["red", "yellow", "purple", "pink"]                # List of petal colors 
    for color in colors:
        pen.color(color)
        pen.circle(10)
        pen.left(90)


def draw_scene():                                               # Main Drawing function to call all the other functions to draw the complete scene 
    draw_ground()
    draw_sun()
    draw_sun_rays(200, 120, 50, 12, 30) 

    draw_tree(-250, -150)                                       # Drawing four trees at different positions on the ground 
    draw_tree(-100, -150)
    draw_tree(50, -150)
    draw_tree(200, -150)

    flower_positions = [(-200, -180), (-150, -180), (-50, -180), (0, -180), (100, -180), (200, -180), (-180, -300), (-120, -300), (-60, -300), (20, -300), (80, -300)]                  # List of flower positions on the ground 
    for pos in flower_positions:                                 # Looping through the list and calling draw_flower function to draw flowers at those positions 
        draw_flower(pos[0], pos[1])

    bird_positions = [(-100, 200), (-50, 200), (0, 180), (50, 210)] 
    for pos in bird_positions: 
        draw_bird(pos[0], pos[1], 20)  

draw_scene()

pen.hideturtle()                                                # Hiding the pen to make it look cleaner 
screen.mainloop()                                               # keeping the window open until user closes it 