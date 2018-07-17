import tkinter as tk
import numpy as np
import time

class smooth_movement:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='light green', height=270, width=368)
        self.frame.pack()

    def start_world(self):
        """World"""
        self.frame.create_rectangle(20, 20, 350, 240, fill='black')
        """horizontal lines"""
        self.frame.create_line(20, 20, 350, 20, fill='white', width=2)
        self.frame.create_line(20, 130, 350, 130, fill='white', width=2)
        self.frame.create_line(20, 240, 350, 240, fill='white', width=2)
        """virtical lines"""
        self.frame.create_line(20, 20, 20, 240, fill='white', width=2)
        self.frame.create_line(130, 20, 130, 240, fill='white', width=2)
        self.frame.create_line(240, 20, 240, 240, fill='white', width=2)
        self.frame.create_line(350, 20, 350, 240, fill='white', width=2)

        #self.root.mainloop()

    def robot_state_1(self):
        loop = 1
        """agent"""
        self.sensor_1 = self.frame.create_rectangle(275, 179, 284, 190, fill='red')
        self.sensor_2 = self.frame.create_rectangle(289, 165, 300, 175, fill='red')
        self.sensor_3 = self.frame.create_rectangle(315, 180, 306, 190, fill='red')
        self.sensor_4 = self.frame.create_rectangle(291, 195, 300, 205, fill='red')
        self.agent = self.frame.create_oval(280, 170, 310, 200, fill='cyan')
        self.frame.update()
        time.sleep(1)
        """activate sensors"""
        for i in range(1, 6):
            time.sleep(0.5)
            if i == 1:
                self.beam_1 = self.frame.create_polygon(266, 184, 274, 184, 274, 186, 266, 186, 266, 184, fill='yellow')
                self.beam_2 = self.frame.create_polygon(294, 164, 294, 156, 296, 156, 296, 164, 294, 164, fill='yellow')
                self.beam_3 = self.frame.create_polygon(316, 184, 324, 184, 324, 186, 316, 186, 316, 184, fill='yellow')
                self.beam_4 = self.frame.create_polygon(295, 206, 295, 214, 297, 214, 297, 206, 294, 206, fill='yellow')
                self.frame.update()
            elif i == 2:
                self.beam_5 = self.frame.create_polygon(256, 184, 264, 184, 264, 186, 256, 186, 256, 184, fill='yellow')
                self.beam_6 = self.frame.create_polygon(294, 154, 294, 146, 296, 146, 296, 154, 294, 154, fill='yellow')
                self.beam_7 = self.frame.create_polygon(326, 184, 334, 184, 334, 186, 326, 186, 326, 184, fill='yellow')
                self.beam_8 = self.frame.create_polygon(295, 216, 295, 224, 297, 224, 297, 216, 294, 216, fill='yellow')
                self.frame.update()
            elif i == 3:
                self.beam_9 = self.frame.create_polygon(246, 184, 254, 184, 254, 186, 246, 186, 246, 184, fill='yellow')
                self.beam_10 = self.frame.create_polygon(294, 144, 294, 136, 296, 136, 296, 144, 294, 144,
                                                         fill='yellow')
                self.beam_11 = self.frame.create_polygon(336, 184, 344, 184, 344, 186, 336, 186, 336, 184,
                                                         fill='yellow')
                self.beam_12 = self.frame.create_polygon(295, 226, 295, 234, 297, 234, 297, 226, 294, 226, fill='yellow')
                self.frame.update()
            elif i == 4:
                self.beam_13 = self.frame.create_polygon(236, 184, 244, 184, 244, 186, 236, 186, 236, 184,
                                                         fill='yellow')
                self.beam_14 = self.frame.create_polygon(294, 134, 294, 128, 296, 128, 296, 134, 294, 134, fill='red')
                self.beam_15 = self.frame.create_polygon(346, 184, 352, 184, 352, 186, 346, 186, 346, 184, fill='red')
                self.beam_16 = self.frame.create_polygon(295, 236, 295, 242, 297, 242, 297, 236, 294, 236, fill='red')
                time.sleep(0.5)
                """"add walls and block"""
                self.frame.create_rectangle(241, 21, 349, 129, fill='grey')
                self.frame.create_line(240, 130, 350, 130, fill='white', width=5)
                self.frame.create_line(350, 129, 350, 242, fill='white', width=5)
                self.frame.create_line(240, 240, 352, 240, fill='white', width=5)
                self.frame.update()
                """"delete sensors"""
            elif i == 5:
                time.sleep(0.5)
                self.frame.delete(self.beam_1)
                self.frame.delete(self.beam_2)
                self.frame.delete(self.beam_3)
                self.frame.delete(self.beam_4)
                self.frame.delete(self.beam_5)
                self.frame.delete(self.beam_6)
                self.frame.delete(self.beam_7)
                self.frame.delete(self.beam_8)
                self.frame.delete(self.beam_9)
                self.frame.delete(self.beam_10)
                self.frame.delete(self.beam_11)
                self.frame.delete(self.beam_12)
                self.frame.delete(self.beam_13)
                self.frame.delete(self.beam_14)
                self.frame.delete(self.beam_15)
                self.frame.delete(self.beam_16)
                self.frame.update()

    def smooth_transition(self):
        coords = [[280, 170], [170, 170], [170, 60], [60, 60]]
        self.start_world()
        """initiate move agent and collect data"""
        for i in range(1, 2):
            if i == 1:
                self.move = 'left'
                self.robot_state_1()
            s = self.frame.coords(self.agent)
            previous_state_coords = [int(s[0]), int(s[1])]
            for x in range(len(coords)):
                if coords[x] == previous_state_coords:
                    print('coords[x]=', x)
                    previous_state = (len(coords)) - x
            move = self.move
            print('move=', move)
            next_state = previous_state - previous_state +1
            next_state_coords= coords[next_state]
            start_sum = s[0]+s[3]
            final_sum = start_sum -220
        time.sleep(2)
        """move agent"""
        while start_sum > final_sum:
            print('START SUM =', start_sum)
            move_agent = np.array([-1, 0])
            move_sensors = np.array([-1, 0])
            self.frame.move(self.agent, move_agent[0], move_agent[1])
            self.frame.move(self.sensor_1, move_sensors[0], move_agent[1])
            self.frame.move(self.sensor_2, move_sensors[0], move_agent[1])
            self.frame.move(self.sensor_3, move_sensors[0], move_agent[1])
            self.frame.move(self.sensor_4, move_sensors[0], move_agent[1])
            self.frame.update()
            s = self.frame.coords(self.agent)
            start_sum = start_sum -2
            time.sleep(0.03)

        self.root.mainloop()


data = smooth_movement()

#data.__init__()

# data.start_world()

# data.robot_state_1()

# data.agent_s1()

data.smooth_transition()