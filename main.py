# Description:
# Let's cheat in a clicker game! - this program was made to help me on a clicker game called Cell to singularity
# This program runs over pyCharm and is a work in progress.
# - please notice this program uses pyautogui.FAILSAFE = False
# Author: @CAZPFITL
# implementation = CPython
# version_info = 3.8.9.final.0

import pyautogui
import numpy as np


class Interpreter(object):
    def __init__(self):
        self.clicks = Interpreter.ask_for_clicks()
        self.fast = Interpreter.ask_for_fast()

    @staticmethod
    def ask_for_clicks():
        def get_random_answer():
            # ask the user for a number and wait for the answer
            while True:
                try:
                    return int(input('Want a random?. \n 1. Yes \n 2. No\n'))
                except ValueError:
                    print('Please enter a number.\n')

        def ask_the_user_for_a_number():
            # ask the user for a number and wait for the answer
            while True:
                try:
                    return int(input('How many clicks do you want?\n'))
                except ValueError:
                    print('Please enter a number.\n')

        # get answer from user
        answer = get_random_answer()

        # if enter is pressed, return a random number
        if answer < 2:
            return np.random.randint(1000, 10000)
        # if enter is not pressed, ask how many clicks the user wants
        else:
            return ask_the_user_for_a_number()

    @staticmethod
    def ask_for_fast():
        def ask_for_speed():
            # ask the user for a number and wait for the answer
            while True:
                try:
                    return int(input('How fast do you want to execute the clicks?\n1. Fast\n2. Slow\n'))
                except ValueError:
                    print('Please enter a number.')
        return True if (ask_for_speed() < 2) else False


class Clicker(object):
    def __init__(self, clicks, fast):
        self.clicks = clicks
        self.fast = fast

    @staticmethod
    def disable_security():
        # set pyautogui.FAILSAFE to False
        pyautogui.FAILSAFE = False

    def do_the_clicks(self):
        if self.fast:
            pyautogui.click(clicks=self.clicks)

        else:
            for i in range(self.clicks):
                pyautogui.click()
                print(self.clicks - i)

    @staticmethod
    def move_to_center():
        # the cursor is moved to the center of the main screen.
        pyautogui.moveTo(x=650, y=400)

    def run(self):
        self.disable_security()
        self.move_to_center()
        self.do_the_clicks()
        print('Enjoy!\nSummary:\nClicks: {}\nFast: {}'.format(self.clicks, self.fast))


def main():
    _Interpreter = Interpreter()
    _Clicker = Clicker(_Interpreter.clicks, _Interpreter.fast)
    _Clicker.run()


main()
