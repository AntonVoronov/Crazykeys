
import keyboard
import sys
sys.path.append('..')
import time

"""
def print_pressed_keys(e):
	line = ', '.join(str(code) for code in keyboard._pressed_events)
	# '\r' and end='' overwrites the previous line.
	# ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
	print('\r' + line + ' '*40, end='')
	
keyboard.hook(print_pressed_keys)
keyboard.wait()
"""

def changekey(): 
    while True:

        if keyboard.is_pressed('a'): 
            keyboard.press_and_release('backspace')
            time.sleep(0.01)


            keyboard.press('alt')
            time.sleep(0.05)
            keyboard.press_and_release(82)
            
            keyboard.press_and_release(80)

            keyboard.press_and_release(80)

            keyboard.press_and_release(73)

            time.sleep(0.05)
            keyboard.release('alt')

            time.sleep(0.05)
            

        else:
            
            
            
            time.sleep(0.05)
            pass
changekey()

