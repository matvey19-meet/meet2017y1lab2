import turtle

side_length = 50

turtle.penup()
turtle.goto(0,0)

turtle.pendown()

turtle.goto(0,side_length)
turtle.goto(side_length,side_length)
turtle.goto(side_length,0)
turtle.goto(0,0)

turtle.mainloop()
