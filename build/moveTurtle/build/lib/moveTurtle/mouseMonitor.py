import scipy
import numpy as np


from pynput.mouse import Listener
from pynput.mouse import Button, Controller

xvals = []
yvals = []

def on_click(x,y,button,pressed):
    if pressed: 
        if button == Button.right:
            return False
        elif button == Button.left:
            print(f'Point at ({x,y}) added')
            xvals.append(x)
            yvals.append(y)
        

with Listener(
    on_click=on_click
) as listener:
    listener.join()