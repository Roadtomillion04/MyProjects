# Here we gonna create timer
import time

def countdown_timer(time_in_sec):
    print(divmod(time_in_sec, 60)) # this converts after 60 to 1 like min
    # this gives two values we take it as min & sec

    while time_in_sec > 0:
        min, sec = divmod(time_in_sec, 60)

        # 0 = The conversion will be zero padded for numeric values.
        # d = Signed integer decimal.
        timer = '{:02d}:{:02d}'.format(min, sec)
        # 02 is given, now two values will be displayed

        print(timer, end='\r') # \r clears words & prints in same line
        time.sleep(1)
        time_in_sec -= 1

    print('Completed!')

user_input = int(input('Enter time in sec: '))
countdown_timer(user_input)
