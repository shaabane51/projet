import turtle
from turtle import *
import random


def map(size):
  matrice = []
  for i in range(size+1):
    matrice.append([0]*size)

  liste_obstacles = [[1,1], [2,1], [2,2],[4,0], [4,1], [4,3], [4,4], [5,6], [1,6]]

  for i in liste_obstacles:
    position_i = i[1]
    position_j = i[0]

    matrice[position_i][position_j] = -1

  return matrice

 
def dessiner_rectangle(plateau,x,y,width,height,size,color,fill):
  plateau.fillcolor(fill)
  plateau.pencolor(color)
  plateau.pensize(size)
  plateau.setheading(0)
 
  plateau.begin_fill()  
  plateau.up()
  plateau.goto(x,y)
  plateau.down()
  plateau.forward(width)
  plateau.right(90)
  plateau.forward(height)
  plateau.right(90)
  plateau.forward(width)
  plateau.right(90)
  plateau.forward(height)
  plateau.end_fill()
 
def dessiner_plateau(plateau, matrice, size):
  for x in range(1,size+1):
    for y in range(1,size+1):
      if matrice[x-1][y-1] == -1 :
          dessiner_rectangle(plateau,-230+x*50,-170+y*50,50,50,2,"white","black")
      
    

def bouger_turtle(plateau, matrice_, dimension_plateau):
  dessiner_rectangle(plateau,-230+1*45,-170+1*45,40,40,5,"red","red")
  plateau.penup()
  plateau.speed("slowest")
  plateau.goto(-180, -150)

  plateau.shape("square")
  s = Shape("compound")
  poly1 = ((0,0),(0,10),(10,10),(10,0))
  s.addcomponent(poly1, "red", "red")
  register_shape("myshape", s)
  plateau.shape("myshape")
  plateau.shapesize(2,2)
  plateau.pendown()

  position_turtle_x = 1
  position_turtle_y = 1
  turtle_est_bloque = False

  while(not turtle_est_bloque) :
    print("bouger_turtle", turtle_est_bloque, position_turtle_x, position_turtle_y)
    turtle_est_bloque = True 
    if position_turtle_y < dimension_plateau :
      if matrice[position_turtle_x-1][position_turtle_y] == 0 :
        turtle_est_bloque = False
        position_turtle_y = position_turtle_y + 1

    if turtle_est_bloque and position_turtle_x < dimension_plateau :
      if matrice[position_turtle_x][position_turtle_y-1] == 0 :
        turtle_est_bloque = False
        position_turtle_x = position_turtle_x + 1


    plateau.goto(-215+position_turtle_x*50, -200+position_turtle_y*50)

  plateau.speed("fast")
  dessiner_rectangle(plateau,-230+7*50+5,-170+7*50,40,40,5,"black","red")
  plateau.penup()
  plateau.goto(-215+position_turtle_x*50, -200+position_turtle_y*50)


#----------------- lancement du programme --------------- #

turtle.setup(400,400)
plateau = turtle.Turtle()
plateau.shape("turtle")
plateau.speed("fast")
dimension_plateau = 7
matrice = map(dimension_plateau)

dessiner_plateau(plateau, matrice, dimension_plateau)
bouger_turtle(plateau, matrice, dimension_plateau)

turtle.done()