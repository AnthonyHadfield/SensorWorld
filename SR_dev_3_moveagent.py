import tkinter as tk
import numpy as np
import time


class SmoothMovement:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='sea green', height=380, width=588)
        self.frame.pack()
        self.agent = ()
        self.move = ()
        self.sensor_1 = ()
        self.sensor_2 = ()
        self.sensor_3 = ()
        self.sensor_4 = ()
        self.beam_1 = ()
        self.beam_2 = ()
        self.beam_3 = ()
        self.beam_4 = ()
        self.beam_5 = ()
        self.beam_6 = ()
        self.beam_7 = ()
        self.beam_8 = ()
        self.beam_9 = ()
        self.beam_10 = ()
        self.beam_11 = ()
        self.beam_12 = ()
        self.beam_13 = ()
        self.beam_14 = ()
        self.beam_15 = ()
        self.beam_16 = ()

    def grid(self):
        """World"""
        self.frame.create_rectangle(20, 20, 570, 350, fill='black')
        """Specials"""
        self.frame.create_rectangle(20, 20, 130, 130, fill='light green')
        self.frame.create_rectangle(460, 20, 570, 130, fill='red')
        self.frame.create_rectangle(20, 130, 240, 350, fill='grey')
        self.frame.create_rectangle(350, 130, 570, 240, fill='grey')
        """horizontal lines"""
        self.frame.create_line(20, 20, 570, 20, fill='white', width=2)
        self.frame.create_line(20, 130, 570, 130, fill='white', width=2)
        self.frame.create_line(240, 240, 350, 240, fill='white', width=2)
        self.frame.create_line(20, 350, 570, 350, fill='white', width=2)
        """virtical lines"""
        self.frame.create_line(20, 20, 20, 350, fill='white', width=2)
        self.frame.create_line(130, 20, 130, 130, fill='white', width=2)
        self.frame.create_line(240, 20, 240, 350, fill='white', width=2)
        self.frame.create_line(350, 20, 350, 350, fill='white', width=2)
        self.frame.create_line(460, 20, 460, 130, fill='white', width=2)
        self.frame.create_line(460, 240, 460, 350, fill='white', width=2)
        """Walls"""
        """State 9"""
        self.frame.create_line(460, 20, 573, 20, fill='white', width=5)
        self.frame.create_line(570, 20, 570, 130, fill='white', width=5)
        self.frame.create_line(460, 130, 570, 130, fill='white', width=5)
        self.frame.create_line(570, 130, 570, 240, fill='white', width=5)
        """State 8"""
        self.frame.create_line(350, 20, 460, 20, fill='white', width=5)
        self.frame.create_line(350, 130, 460, 130, fill='white', width=5)
        """State 7"""
        self.frame.create_line(18, 20, 130, 20, fill='white', width=5)
        self.frame.create_line(20, 20, 20, 130, fill='white', width=5)
        self.frame.create_line(20, 130, 130, 130, fill='white', width=5)
        self.frame.create_line(20, 130, 20, 350, fill='white', width=5)
        self.frame.create_line(18, 350, 130, 350, fill='white', width=5)
        """State 6"""
        self.frame.create_line(130, 20, 240, 20, fill='white', width=5)
        self.frame.create_line(130, 130, 240, 130, fill='white', width=5)
        """State 5"""
        self.frame.create_line(240, 20, 350, 20, fill='white', width=5)
        """State 4"""
        self.frame.create_line(240, 130, 240, 240, fill='white', width=5)
        self.frame.create_line(350, 130, 350, 240, fill='white', width=5)
        """State 3"""
        self.frame.create_line(240, 350, 350, 350, fill='white', width=5)
        self.frame.create_line(240, 240, 240, 350, fill='white', width=5)
        self.frame.create_line(130, 350, 240, 350, fill='white', width=5)
        """State 2"""
        self.frame.create_line(350, 350, 460, 350, fill='white', width=5)
        self.frame.create_line(350, 240, 460, 240, fill='white', width=5)
        """State 1"""
        self.frame.create_line(570, 240, 570, 353, fill='white', width=5)
        self.frame.create_line(460, 240, 570, 240, fill='white', width=5)
        self.frame.create_line(460, 350, 570, 350, fill='white', width=5)

        # self.root.mainloop()

    def start_world(self):
        """World"""
        self.frame.create_rectangle(20, 20, 570, 350, fill='black')
        """horizontal lines"""
        self.frame.create_line(20, 20, 570, 20, fill='white', width=2)
        self.frame.create_line(20, 130, 570, 130, fill='white', width=2)
        self.frame.create_line(20, 240, 570, 240, fill='white', width=2)
        self.frame.create_line(20, 350, 570, 350, fill='white', width=2)
        """virtical lines"""
        self.frame.create_line(20, 20, 20, 350, fill='white', width=2)
        self.frame.create_line(130, 20, 130, 350, fill='white', width=2)
        self.frame.create_line(240, 20, 240, 350, fill='white', width=2)
        self.frame.create_line(350, 20, 350, 350, fill='white', width=2)
        self.frame.create_line(460, 20, 460, 350, fill='white', width=2)
        self.frame.create_line(570, 20, 570, 350, fill='white', width=2)

    def robot(self):

        global states

        n = ()
        m = ()
        x = ()
        y = ()
        a = ()
        b = ()

        states = [[1, 'left'], [2, 'left'], [3, 'up'], [4, 'up'], [5, 'left', 'right'], [6, 'left'], [7], [8, 'right'],
                  [9]]
        """call robot by state"""
        if current_state == states[0][0]:
            n = 0
            m = 0
            x = 0
            y = 0
            a = 10
            b = 10
            self.move = states[0][1]
            print('move =', self.move)
        if current_state == states[1][0]:
            n = -1
            x = 110
            m = 1
            y = 0
            a = 10
            b = 10
            self.move = states[1][1]
        """generic robot and sensor coordinates"""
        r = (500 + n * x, 280 + m * y, 530 + n * x, 310 + m * y)
        s1 = (495 + n * x, 290 + m * y, 504 + n * x, 300 + m * y)
        s2 = (509 + n * x, 275 + m * y, 520 + n * x, 285 + m * y)
        s3 = (535 + n * x, 290 + m * y, 526 + n * x, 300 + m * y)
        s4 = (509 + n * x, 305 + m * y, 520 + n * x, 315 + m * y)
        self.sensor_1 = self.frame.create_rectangle(s1, fill='red')
        self.sensor_2 = self.frame.create_rectangle(s2, fill='red')
        self.sensor_3 = self.frame.create_rectangle(s3, fill='red')
        self.sensor_4 = self.frame.create_rectangle(s4, fill='red')
        self.agent = self.frame.create_oval(r, fill='cyan')
        self.frame.update()
        time.sleep(0.5)
        """activate sensors"""
        for i in range(1, 6):
            time.sleep(0.5)
            if i == 1:
                self.beam_1 = self.frame.create_polygon(486 + n * x, 294 + m * y, 494 + n * x, 294 + m * y, 494 + n * x,
                                                        296 + m * y, 486 + n * x, 296 + m * y, 486 + n * x, 294 + m * y,
                                                        fill='yellow')
                self.beam_2 = self.frame.create_polygon(515 + n * x, 274 + m * y, 515 + n * x, 266 + m * y, 517 + n * x,
                                                        266 + m * y, 517 + n * x, 274 + m * y, 514 + n * x, 274 + m * y,
                                                        fill='yellow')
                self.beam_3 = self.frame.create_polygon(536 + n * x, 294 + m * y, 544 + n * x, 294 + m * y, 544 + n * x,
                                                        296 + m * y, 536 + n * x, 296 + m * y, 536 + n * x, 294 + m * y,
                                                        fill='yellow')
                self.beam_4 = self.frame.create_polygon(515 + n * x, 316 + m * y, 515 + n * x, 324 + m * y, 517 + n * x,
                                                        324 + m * y, 517 + n * x, 316 + m * y, 514 + n * x, 316 + m * y,
                                                        fill='yellow')
            if i == 2:
                self.beam_5 = self.frame.create_polygon(486 - a + n * x, 294 + m * y, 494 - a + n * x, 294 + m * y,
                                                        494 - a + n * x, 296 + m * y, 486 - a + n * x, 296 + m * y,
                                                        486 - a + n * x, 294 + m * y, fill='yellow')
                self.beam_6 = self.frame.create_polygon(515 + n * x, 274 - b + m * y, 515 + n * x, 266 - b + m * y,
                                                        517 + n * x, 266 - b + m * y, 517 + n * x, 274 - b + m * y,
                                                        514 + n * x, 274 - b + m * y, fill='yellow')
                self.beam_7 = self.frame.create_polygon(536 + a + n * x, 294 + m * y, 544 + a + n * x, 294 + m * y,
                                                        544 + a + n * x, 296 + m * y, 536 + a + n * x, 296 + m * y,
                                                        536 + a + n * x, 294 + m * y, fill='yellow')
                self.beam_8 = self.frame.create_polygon(515 + n * x, 316 + b + m * y, 515 + n * x, 324 + b + m * y,
                                                        517 + n * x, 324 + b + m * y, 517 + n * x, 316 + b + m * y,
                                                        514 + n * x, 316 + b + m * y, fill='yellow')
            if i == 3:
                self.beam_9 = self.frame.create_polygon(486 - 2 * a + n * x, 294 + m * y, 494 - 2 * a + n * x,
                                                        294 + m * y, 494 - 2 * a + n * x, 296 + m * y,
                                                        486 - 2 * a + n * x, 296 + m * y, 486 - 2 * a + n * x,
                                                        294 + m * y, fill='yellow')
                self.beam_10 = self.frame.create_polygon(515 + n * x, 274 - 2 * b + m * y, 515 + n * x,
                                                         266 - 2 * b + m * y, 517 + n * x, 266 - 2 * b + m * y,
                                                         517 + n * x, 274 - 2 * b + m * y, 514 + n * x,
                                                         274 - 2 * b + m * y, fill='yellow')
                self.beam_11 = self.frame.create_polygon(536 + 2 * a + n * x, 294 + m * y, 544 + 2 * a + n * x,
                                                         294 + m * y, 544 + 2 * a + n * x, 296 + m * y,
                                                         536 + 2 * a + n * x, 296 + m * y, 536 + 2 * a + n * x,
                                                         294 + m * y, fill='yellow')
                self.beam_12 = self.frame.create_polygon(515 + n * x, 316 + 2 * b + m * y, 515 + n * x,
                                                         324 + 2 * b + m * y, 517 + n * x, 324 + 2 * b + m * y,
                                                         517 + n * x, 316 + 2 * b + m * y, 514 + n * x,
                                                         316 + 2 * b + m * y, fill='yellow')
            if i == 4:
                self.beam_13 = self.frame.create_polygon(486 - 3 * a + n * x, 294 + m * y, 494 - 3 * a + n * x,
                                                         294 + m * y, 494 - 3 * a + n * x, 296 + m * y,
                                                         486 - 3 * a + n * x, 296 + m * y, 486 - 3 * a + n * x,
                                                         294 + m * y, fill='yellow')
                self.beam_14 = self.frame.create_polygon(515 + n * x, 274 - 3 * b + m * y, 515 + n * x,
                                                         266 - 3 * b + m * y, 517 + n * x, 266 - 3 * b + m * y,
                                                         517 + n * x, 274 - 3 * b + m * y, 514 + n * x,
                                                         274 - 3 * b + m * y, fill='yellow')
                self.beam_15 = self.frame.create_polygon(536 + 3 * a + n * x, 294 + m * y, 544 + 3 * a + n * x,
                                                         294 + m * y, 544 + 3 * a + n * x, 296 + m * y,
                                                         536 + 3 * a + n * x, 296 + m * y, 536 + 3 * a + n * x,
                                                         294 + m * y, fill='yellow')
                self.beam_16 = self.frame.create_polygon(515 + n * x, 316 + 3 * b + m * y, 515 + n * x,
                                                         324 + 3 * b + m * y, 517 + n * x, 324 + 3 * b + m * y,
                                                         517 + n * x, 316 + 3 * b + m * y, 514 + n * x,
                                                         316 + 3 * b + m * y, fill='yellow')
            self.frame.update()
        """"add walls and block"""
        if current_state == states[0][0]:
            self.frame.create_rectangle(350, 130, 570, 240, fill='grey')
            self.frame.create_line(570, 240, 570, 353, fill='white', width=5)
            self.frame.create_line(460, 240, 570, 240, fill='white', width=5)
            self.frame.create_line(460, 350, 570, 350, fill='white', width=5)
        if current_state == states[1][0]:
            self.frame.create_line(350, 350, 460, 350, fill='white', width=5)
            self.frame.create_line(350, 240, 460, 240, fill='white', width=5)
        """"delete sensors"""

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

    def move_agent(self):

        global current_state
        coords = [[500, 280], [390, 280], [280, 280], [280, 170], [280, 60], [170, 60], [60, 60], [390, 60], [500, 60]]
        """generic coordinates"""
        self.start_world()
        current_state = 1
        """move the robot main LOOP"""
        for i in range(1, 3):
            self.robot()
            s = self.frame.coords(self.agent)
            print('s=', s)
            current_coords = [int(s[0]), int(s[3])]
            print('current coords', current_coords)
            """generate start and final counter"""
            if self.move == 'left':
                start_sum = s[0] + s[3]
                adjust = -220
                final_sum = start_sum + adjust
                move_agent = np.array([-1, 0])
                move_sensors = np.array([-1, 0])
            if self.move == 'up':
                start_sum = s[1] + s[4]
                adjust = -220
                final_sum = start_sum + adjust
                move_agent = np.array([0, -1])
                move_sensors = np.array([0, -1])
            if self.move == 'right':
                start_sum = s[0] + s[3]
                adjust = 220
                final_sum = start_sum + adjust
                move_agent = np.array([1, 0])
                move_sensors = np.array([1, 0])
            """moving the robot LOOP"""
            if self.move == 'left' or self.move == 'up':
                while start_sum > final_sum:
                    self.frame.move(self.agent, move_agent[0], move_agent[1])
                    self.frame.move(self.sensor_1, move_sensors[0], move_agent[1])
                    self.frame.move(self.sensor_2, move_sensors[0], move_agent[1])
                    self.frame.move(self.sensor_3, move_sensors[0], move_agent[1])
                    self.frame.move(self.sensor_4, move_sensors[0], move_agent[1])
                    self.frame.update()
                    """move robot one step at a time"""
                    start_sum = start_sum - 2
                    time.sleep(0.03)
            if self.move == 'right':
                while start_sum < final_sum:
                    self.frame.move(self.agent, move_agent[0], move_agent[1])
                    self.frame.move(self.sensor_1, move_sensors[0], move_agent[1])
                    self.frame.move(self.sensor_2, move_sensors[0], move_agent[1])
                    self.frame.move(self.sensor_3, move_sensors[0], move_agent[1])
                    self.frame.move(self.sensor_4, move_sensors[0], move_agent[1])
                    self.frame.update()
                    """move robot one step at a time"""
                    start_sum = start_sum + 2

            s = self.frame.coords(self.agent)
            print('coords = ', s)
            current_state_coords = [int(s[0]), int(s[1])]
            print('state coords =', current_state_coords)
            for x in range(0, len(coords)):
                if coords[x] == current_state_coords:
                    current_state = states[x][0]
            print('current state =', current_state)

        self.root.mainloop()

data = SmoothMovement()

# data.__init__()

# data.grid()

# data.start_world()

# data.robot_state_1()

# data.agent_s1()

data.move_agent()
