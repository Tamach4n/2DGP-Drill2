from pico2d import *
import math

open_canvas()

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
rooped = False
sq = True

while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if sq:
        if x < 780:
            x = x + 2

        else:
            if y != 550:
                y = y + 2

            elif y == 550:
                if x > 20:
                    x = x - 2

                else:
                    if y > 90:
                        y = y - 2

                    else:
                        rooped = True

        if rooped == True & x == 400 & y == 90:
            sq = False
        
        
    else:
        theta = 0
        
        x = 250 * math.cos(theta)
        y = 250 * math.sin(theta)

        theta = theta + 2

        if theta == 360:
            theta = 0
            sq = True
    
    delay(0.001)

close_canvas()
