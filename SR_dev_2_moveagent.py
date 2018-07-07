import tkinter as tk
import numpy as np
import time

class smooth_movement:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='light green', height=270, width=148)
        self.frame.pack()

    def world(self):

        self.frame.create_rectangle(20, 20, 130, 240, fill='black')
        self.frame.create_line(20, 130, 130, 130, fill='white', width=2)
        self.frame.create_line(18, 20, 130, 20, 130, 240, 20, 240, 20, 20, fill='white', width=5)
        self.frame.pack()

        #self.root.mainloop()

    def sensor_robot(self):

        self.world()

        self.sensor_1 = self.frame.create_rectangle(55, 180, 64, 190, fill='red')
        self.sensor_2 = self.frame.create_rectangle(71, 165, 80, 175, fill='red')
        self.sensor_3 = self.frame.create_rectangle(95, 180, 86, 190, fill='red')
        self.sensor_4 = self.frame.create_rectangle(71, 195, 80, 205, fill='red')
        self.agent = self.frame.create_oval(60, 170, 90, 200, fill='cyan')

        # self.agent = self.frame.create_oval(60, 60, 90, 90, fill='cyan')
        time.sleep(0.1)
        #self.root.mainloop()

    def smooth_transition(self):

        self.sensor_robot()

        agentdata = self.frame.coords(self.agent)
        print('initial COORDS=', agentdata)

        sum_start = 370
        sum_end = 150

        while sum_start > sum_end:

            move_agent = np.array([0, -1])
            move_sensors = np.array([0, -1])

            self.frame.move(self.agent, move_agent[0], move_agent[1])
            self.frame.move(self.sensor_1, move_sensors[0], move_agent[1])
            self.frame.move(self.sensor_2, move_sensors[0], move_agent[1])
            self.frame.move(self.sensor_3, move_sensors[0], move_agent[1])
            self.frame.move(self.sensor_4, move_sensors[0], move_agent[1])

            s = self.frame.coords(self.agent)
            print('coords = ', s)
            self.frame.update()
            sum_start = sum_start -2
            time.sleep(0.01)
            # time.sleep(0.05)

        self.root.mainloop()


data = smooth_movement()

#data.__init__()

# data.world()

#data.sensor_robot()

data.smooth_transition()