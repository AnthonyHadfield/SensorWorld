import tkinter as tk
import numpy as np
import time

class Sensorworld:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='sea green', height=400, width=500)
        self.frame.pack()

    def reward_table(self):
        s = 0
        x = 11
        y = 5
        self.sr = np.zeros([x, y], dtype=np.object)
        for x in range(11):
            self.sr[:, 1:] = float(0)
            self.sr[x][0] = s
            s = s + 1

        np.save('C:/Users/user/PycharmProjects/Reinforcement Learning/GridWorld/Reward_table', self.sr)
        print(self.sr)
        print('')

    def sensor_robot(self):
        self.frame.create_rectangle(65, 300, 74, 310, fill='red')
        self.frame.create_rectangle(81, 285, 90, 295, fill='red')
        self.frame.create_rectangle(105, 300, 96, 310, fill='red')
        self.frame.create_rectangle(81, 315, 90, 325, fill='red')
        self.agent = self.frame.create_oval(70, 290, 100, 320, fill='cyan')


    def maze_1(self):

        self.frame.create_rectangle(30, 30, 470, 360, fill='black')
        self.frame.create_line(30, 30, 470, 30, 470, 360, 30, 360, 30, 30, fill='white', width=2)

        self.sensor_robot()

        self.root.mainloop()

data = Sensorworld()

#data.__init__()

#data.reward_table()

data.maze_1()