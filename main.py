# Description:
# Let's cheat in a clicker game! - this program was made to help me on a clicker game called Cell to singularity
# This program runs over pyCharm and is a work in progress.
# - please notice this program uses pyautogui.FAILSAFE = False
# Author: @CAZPFITL
# implementation = CPython
# version_info = 3.8.9.final.0
import pyautogui
import numpy as np
import tkinter as tk


class Clicker(object):
    def __init__(self, clicks, fast):
        self.clicks = int(clicks)
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
        print('---------------------\nEnjoy!\nSummary:\nClicks: {}\nFast: {}'.format(self.clicks, self.fast))


class ConsoleInterpreter(object):
    def __init__(self):
        self.clicks = self.ask_for_clicks()
        self.fast = self.ask_for_fast()

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

    def run(self):
        print('STARTING\nisFast: ', self.fast, '\nclicks: ', self.clicks)
        app = Clicker(self.clicks, self.fast)
        app.run()


class TkinterInterpreter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.isFast = True
        self.clicks = None
        self.firstStep = None
        self.hi_there = None
        self.quit = None
        self.slow = None
        self.fast = None
        self.master = master
        self.pack()
        self.create_start_screen()

    def create_start_screen(self):
        self.create_dimensions()
        self.create_quit_button()
        self.create_title()
        self.create_instructions()
        self.create_number_entry()
        self.create_start_button()
        self.create_speed_check_buttons()

    def close_window(self):
        self.master.destroy()
        exit()

    def create_dimensions(self):
        self.master.geometry("500x500")
        self.master.title("Cell to singularity")
        self.master.resizable(False, False)

    def create_quit_button(self):
        self.quit = tk.Button(
            self,
            text="Quit",
            command=self.close_window,
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400,
            width=360
        )
        self.quit.pack(side="top")

    def create_title(self):
        self.firstStep = tk.Label(self, text="")
        self.firstStep.pack()
        self.firstStep = tk.Label(
            self,
            text="Let's cheat in a clicker game!\n"
                 "this program was made to help me on a\n"
                 "clicker game called Cell to singularity\n",
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400
        )

        self.firstStep.pack(side="top")

    def create_instructions(self):
        # ask the user for a number and wait for the answer
        self.firstStep = tk.Label(
            self,
            text="How Many Steps do you want to execute?",
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400
        )
        self.firstStep.pack(side="top")

    def create_number_entry(self):
        self.clicks = tk.Entry(
            self,
            font=("Helvetica", 18),
            justify=tk.CENTER,
            borderwidth=5
        )
        self.clicks.pack()

    def slow_click(self):
        self.isFast = False

    def fast_click(self):
        self.isFast = True

    def create_speed_check_buttons(self):
        self.firstStep = tk.Label(
            self,
            text="How fast do you want to click?",
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400,
        )
        self.firstStep.pack(side="top")

        self.slow = tk.Button(
            self,
            activebackground="white",
            activeforeground="black",
            bg="white",
            fg="black",
            bd=4,
            text="Slow",
            command=self.slow_click,
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400,
            width=360
        )
        self.slow.pack(side="bottom")

        self.fast = tk.Button(
            self,
            activebackground="white",
            activeforeground="black",
            bg="white",
            fg="black",
            bd=4,
            text="Fast",
            command=self.fast_click,
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400,
            width=360
        )
        self.fast.pack(side="bottom")

    def create_start_button(self):
        self.hi_there = tk.Button(
            self,
            text="Start",
            command=self.run,
            font=("Helvetica", 18),
            justify=tk.CENTER,
            wraplength=400,
            width=360
        )
        self.hi_there.pack(side="bottom")

    def run(self):
        print('STARTING\nisFast: ', self.isFast, '\nclicks: ', self.clicks.get())
        app = Clicker(self.clicks.get(), self.isFast)
        app.run()


class Adapter(object):
    def __init__(self, data):
        self.useConsole = data['use_console']

    @staticmethod
    def guiInstance():
        root = tk.Tk()
        app = TkinterInterpreter(master=root)
        app.mainloop()

    @staticmethod
    def consoleInstance():
        app = ConsoleInterpreter()
        app.run()

    def run(self):
        self.consoleInstance() if self.useConsole else self.guiInstance()


def main():
    app = Adapter({"use_console": True})
    app.run()


main()
