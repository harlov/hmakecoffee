import time
import random
import sys

class MakeCoffeeService():
    make_coffee_steps = [
        'lock door',
        'ground coffee',
        'put in the machine',
        'cook',
        'pour into a cup',
        'add sugar',
        'add milk',
        'release lock door'
    ]
    beetween_steps_second = [1,10]

    def __init__(self):
        print("heating coffee maker...")
        random.seed()
        time.sleep(3)
        print("coffee maker is ready!")

    def print_progres(self):
        sys.stdout.flush()
        timeout_sec = random.randint(self.beetween_steps_second[0], self.beetween_steps_second[1])
        while timeout_sec > 0:
            time.sleep(1)
            timeout_sec -= 1
            sys.stdout.write('.')
            sys.stdout.flush()
        print
            

    def get_cup(self):
        print("Wait, you coffee is prepaid...")
        for x in self.make_coffee_steps:
            print(" doing step : %s" % (x, )),
            self.print_progres()


        print("Ok, get you coffee!")