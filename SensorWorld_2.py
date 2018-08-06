from tkinter import *
import numpy as np
import random
import time


class SensorWorld:

    def __init__(self):

        self.root = Tk()
        """WINDOW center"""
        self.root.geometry("610x840+535+30")
        """Window right side"""
        self.root.geometry("610x840+1075+30")
        self.root.title('SENSOR WORLD'.center(150))
        self.frame = Canvas(bg='sea green', width=588, height=820)
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
        self.frame.create_rectangle(20, 20, 570, 790, fill='black')
        """Specials"""
        self.frame.create_rectangle(20, 20, 240, 240, fill='grey')
        self.frame.create_rectangle(350, 20, 570, 240, fill='grey')
        self.frame.create_rectangle(130, 350, 240, 570, fill='grey')
        self.frame.create_rectangle(350, 350, 570, 460, fill='grey')
        self.frame.create_rectangle(350, 570, 570, 680, fill='grey')
        self.frame.create_rectangle(20, 680, 240, 790, fill='grey')
        self.frame.create_rectangle(20, 240, 130, 350, fill='light green')
        self.frame.create_rectangle(20, 350, 130, 460, fill='light green')
        self.frame.create_rectangle(460, 460, 570, 570, fill='yellow')
        self.frame.create_rectangle(460, 240, 570, 350, fill='red')
        self.frame.create_rectangle(240, 20, 350, 130, fill='red')
        self.frame.create_rectangle(460, 680, 570, 790, fill='red')
        """Titles"""
        self.frame.create_text(515, 475, text='Start', font="Verdana 10 bold", fill='black')
        self.frame.create_text(70, 255, text='Goal', font="Verdana 10 bold", fill='black')
        self.frame.create_text(70, 365, text='Goal', font="Verdana 10 bold", fill='black')
        self.frame.create_text(290, 35, text='PIT', font="Verdana 10 bold", fill='black')
        self.frame.create_text(520, 255, text='PIT', font="Verdana 10 bold", fill='black')
        self.frame.create_text(520, 695, text='PIT', font="Verdana 10 bold", fill='black')
        """horizontal lines"""
        self.frame.create_line(240, 130, 350, 130, fill='white', width=3)
        self.frame.create_line(240, 240, 350, 240, fill='white', width=2)
        self.frame.create_line(240, 350, 350, 350, fill='white', width=2)
        self.frame.create_line(240, 460, 350, 460, fill='white', width=2)
        self.frame.create_line(240, 570, 350, 570, fill='white', width=2)
        self.frame.create_line(240, 680, 350, 680, fill='white', width=2)
        self.frame.create_line(20, 350, 130, 350, fill='white', width=3)
        self.frame.create_line(20, 460, 130, 460, fill='white', width=2)
        self.frame.create_line(20, 570, 130, 570, fill='white', width=2)
        """virtical lines"""
        self.frame.create_line(130, 240, 130, 350, fill='white', width=3)
        self.frame.create_line(240, 240, 240, 350, fill='white', width=2)
        self.frame.create_line(350, 240, 350, 350, fill='white', width=2)
        self.frame.create_line(460, 240, 460, 350, fill='white', width=3)
        self.frame.create_line(350, 460, 350, 570, fill='white', width=2)
        self.frame.create_line(460, 460, 460, 570, fill='red', width=3)
        self.frame.create_line(130, 570, 130, 680, fill='white', width=2)
        self.frame.create_line(240, 570, 240, 680, fill='white', width=2)
        self.frame.create_line(350, 680, 350, 790, fill='white', width=2)
        self.frame.create_line(460, 680, 460, 790, fill='white', width=3)
        """Walls AND States"""
        """State 19"""
        self.frame.create_line(20, 460, 130, 460, fill='white', width=3)
        self.frame.create_line(130, 350, 130, 460, fill='white', width=5)
        self.frame.create_line(20, 350, 130, 350, fill='white', width=5)
        self.frame.create_text(70, 410, text='19', font="Verdana 15 bold", fill='black')
        """State 18"""
        self.frame.create_line(130, 460, 130, 570, fill='white', width=5)
        self.frame.create_text(70, 520, text='18', font="Verdana 15 bold", fill='white')
        """State 17"""
        self.frame.create_line(20, 680, 130, 680, fill='white', width=5)
        self.frame.create_text(70, 630, text='17', font="Verdana 15 bold", fill='white')
        """State 16"""
        self.frame.create_line(130, 570, 240, 570, fill='white', width=5)
        self.frame.create_line(130, 680, 240, 680, fill='white', width=5)
        self.frame.create_text(180, 630, text='16', font="Verdana 15 bold", fill='white')
        """State 15"""
        self.frame.create_line(460, 680, 570, 680, fill='white', width=5)
        self.frame.create_line(460, 790, 570, 790, fill='white', width=5)
        self.frame.create_text(510, 740, text='15', font="Verdana 15 bold", fill='white')
        """State 14"""
        self.frame.create_line(350, 680, 460, 680, fill='white', width=5)
        self.frame.create_line(350, 790, 460, 790, fill='white', width=5)
        self.frame.create_text(400, 740, text='14', font="Verdana 15 bold", fill='white')
        """State 13"""
        self.frame.create_line(240, 680, 240, 790, fill='white', width=5)
        self.frame.create_line(240, 790, 350, 790, fill='white', width=5)
        self.frame.create_text(290, 740, text='13', font="Verdana 15 bold", fill='white')
        """State 12"""
        self.frame.create_line(350, 570, 350, 680, fill='white', width=5)
        self.frame.create_text(290, 630, text='12', font="Verdana 15 bold", fill='white')
        """State 11"""
        self.frame.create_text(520, 255, text='PIT', font="Verdana 10 bold", fill='black')
        self.frame.create_text(510, 300, text='11', font="Verdana 15 bold", fill='white')
        self.frame.create_line(460, 240, 460, 350, fill='white', width=3)
        self.frame.create_line(460, 240, 570, 240, fill='white', width=5)
        self.frame.create_line(460, 350, 570, 350, fill='white', width=5)
        """State 10"""
        self.frame.create_line(350, 240, 460, 240, fill='white', width=5)
        self.frame.create_line(350, 350, 460, 350, fill='white', width=5)
        self.frame.create_text(290, 80, text='9', font="Verdana 15 bold", fill='white')
        """State 9"""
        self.frame.create_line(240, 130, 350, 130, fill='white', width=3)
        self.frame.create_line(240, 20, 240, 130, fill='white', width=5)
        self.frame.create_line(350, 20, 350, 130, fill='white', width=5)
        self.frame.create_text(290, 35, text='PIT', font="Verdana 10 bold", fill='black')
        """State 8"""
        self.frame.create_line(240, 130, 240, 240, fill='white', width=5)
        self.frame.create_line(350, 130, 350, 240, fill='white', width=5)
        self.frame.create_text(290, 190, text='8', font="Verdana 15 bold", fill='white')
        """State 7"""
        self.frame.create_line(130, 240, 130, 350, fill='white', width=3)
        self.frame.create_line(20, 240, 130, 240, fill='white', width=5)
        self.frame.create_line(20, 240, 20, 350, fill='white', width=5)
        self.frame.create_text(70, 300, text='7', font="Verdana 15 bold", fill='black')
        """State 6"""
        self.frame.create_line(130, 240, 240, 240, fill='white', width=5)
        self.frame.create_line(130, 350, 240, 350, fill='white', width=5)
        self.frame.create_text(180, 300, text='6', font="Verdana 15 bold", fill='white')
        """State 5"""
        self.frame.create_text(290, 300, text='5', font="Verdana 15 bold", fill='white')
        """State 4"""
        self.frame.create_line(240, 350, 240, 460, fill='white', width=5)
        self.frame.create_line(350, 350, 350, 460, fill='white', width=5)
        self.frame.create_text(290, 410, text='4', font="Verdana 15 bold", fill='white')
        """State 3"""
        self.frame.create_line(240, 460, 240, 570, fill='white', width=5)
        self.frame.create_text(290, 520, text='3', font="Verdana 15 bold", fill='white')
        """State 2"""
        self.frame.create_line(350, 460, 460, 460, fill='white', width=5)
        self.frame.create_line(350, 570, 460, 570, fill='white', width=5)
        self.frame.create_text(400, 520, text='2', font="Verdana 15 bold", fill='white')
        """State 1"""
        self.frame.create_line(460, 460, 570, 460, fill='white', width=5)
        self.frame.create_line(460, 570, 570, 570, fill='white', width=5)
        """BOARDER"""
        self.frame.create_line(18, 20, 570, 20, 570, 790, 20, 790, 20, 20, fill='white', width=5)
        """AGENT"""
        n = 1
        m = 1
        x = 0
        y = 0
        """generic robot and sensor coordinates"""
        r = (500 + n * x, 500 + m * y, 530 + n * x, 530 + m * y)
        s1 = (495 + n * x, 510 + m * y, 504 + n * x, 520 + m * y)
        s2 = (509 + n * x, 495 + m * y, 520 + n * x, 505 + m * y)
        s3 = (535 + n * x, 510 + m * y, 526 + n * x, 520 + m * y)
        s4 = (509 + n * x, 525 + m * y, 520 + n * x, 535 + m * y)
        self.sensor_1 = self.frame.create_rectangle(s1, fill='red')
        self.sensor_2 = self.frame.create_rectangle(s2, fill='red')
        self.sensor_3 = self.frame.create_rectangle(s3, fill='red')
        self.sensor_4 = self.frame.create_rectangle(s4, fill='red')
        self.agent = self.frame.create_oval(r, fill='cyan')
        # self.root.mainloop()

    def start_world(self):
        """World"""
        self.frame.create_rectangle(20, 20, 570, 790, fill='black')
        self.frame.create_line(18, 20, 570, 20, 570, 790, 20, 790, 20, 20, fill='white', width=5)
        """horizontal lines"""
        self.frame.create_line(20, 130, 570, 130, fill='white', width=2)
        self.frame.create_line(20, 240, 570, 240, fill='white', width=2)
        self.frame.create_line(20, 350, 570, 350, fill='white', width=2)
        self.frame.create_line(20, 460, 570, 460, fill='white', width=2)
        self.frame.create_line(20, 570, 570, 570, fill='white', width=2)
        self.frame.create_line(20, 680, 570, 680, fill='white', width=2)
        """virtical lines"""
        self.frame.create_line(130, 20, 130, 790, fill='white', width=2)
        self.frame.create_line(240, 20, 240, 790, fill='white', width=2)
        self.frame.create_line(350, 20, 350, 790, fill='white', width=2)
        self.frame.create_line(460, 20, 460, 790, fill='white', width=2)
        # self.root.mainloop()

    def robot(self):

        global states
        n = ()
        m = ()
        x = ()
        y = ()
        a = 10
        b = 10

        sixtyforty = 0.6
        states = [[1, 'left'], [2, 'left'], [3, 'up', 'down'], [4, 'up'], [5, 'left', 'up', 'right'], [6, 'left'], [7],
                  [8, 'up'], [9], [10, 'right'], [11], [12, 'left', 'down'], [13, 'right'], [14, 'right'], [15],
                  [16, 'left'], [17, 'up'], [18, 'up'], [19]]
        """Initialize robot by deleting it"""
        self.frame.delete(self.agent)
        self.frame.delete(self.sensor_1)
        self.frame.delete(self.sensor_2)
        self.frame.delete(self.sensor_3)
        self.frame.delete(self.sensor_4)
        """call robot by state"""
        """state 1"""
        if current_state == states[0][0]:
            n = 1
            m = 1
            x = 0
            y = 0
            self.move = states[0][1]
        """state 2"""
        if current_state == states[1][0]:
            n = -1
            m = 1
            x = 110
            y = 0
            self.move = states[1][1]
        """state 3"""
        if current_state == states[2][0]:
            choice = np.random.uniform()
            print('choice', choice)
            if choice < sixtyforty:
                self.move = states[2][1]
                print('SIXTY', states[2][1])
            else:
                self.move = states[2][2]
                print('FORTY', states[2][2])
            n = -2
            m = 1
            x = 110
            y = 0
        """state 4"""
        if current_state == states[3][0]:
            n = -2
            m = -1
            x = 110
            y = 110
            self.move = states[3][1]
        """state 5"""
        if current_state == states[4][0]:
            moves1 = ['left', 'up', 'right']
            self.move = random.choice(moves1)
            n = -2
            m = -2
            x = 110
            y = 110
        """state 6"""
        if current_state == states[5][0]:
            n = -3
            m = -2
            x = 110
            y = 110
            self.move = states[5][1]
        """state 7"""
        if current_state == states[6][0]:
            n = -4
            m = -2
            x = 110
            y = 110
        """state 8"""
        if current_state == states[7][0]:
            n = -2
            m = -3
            x = 110
            y = 110
            self.move = states[7][1]
        """state 9"""
        if current_state == states[8][0]:
            n = -2
            m = -4
            x = 110
            y = 110
        """state 10"""
        if current_state == states[9][0]:
            n = -1
            m = -2
            x = 110
            y = 110
            self.move = states[9][1]
        """state 11"""
        if current_state == states[10][0]:
            n = 1
            m = -2
            x = 0
            y = 110
        """state 12"""
        if current_state == states[11][0]:
            moves2 = ['left', 'down']
            self.move = random.choice(moves2)
            n = -2
            m = 1
            x = 110
            y = 110
        """state 13"""
        if current_state == states[12][0]:
            n = -2
            m = 2
            x = 110
            y = 110
            self.move = states[12][1]
        """state 14"""
        if current_state == states[13][0]:
            n = -1
            m = 2
            x = 110
            y = 110
            self.move = states[13][1]
        """state 15"""
        if current_state == states[14][0]:
            n = 1
            m = 2
            x = 0
            y = 110
        """state 16"""
        if current_state == states[15][0]:
            n = -3
            m = 1
            x = 110
            y = 110
            self.move = states[15][1]
        """state 17"""
        if current_state == states[16][0]:
            n = -4
            m = 1
            x = 110
            y = 110
            self.move = states[16][1]
        """state 18"""
        if current_state == states[17][0]:
            n = -4
            m = 1
            x = 110
            y = 0
            self.move = states[17][1]
        """state 19"""
        if current_state == states[18][0]:
            n = -4
            m = -1
            x = 110
            y = 110
        """generic robot and sensor coordinates"""
        r = (500 + n * x, 500 + m * y, 530 + n * x, 530 + m * y)
        s1 = (495 + n * x, 510 + m * y, 504 + n * x, 520 + m * y)
        s2 = (509 + n * x, 495 + m * y, 520 + n * x, 505 + m * y)
        s3 = (535 + n * x, 510 + m * y, 526 + n * x, 520 + m * y)
        s4 = (509 + n * x, 525 + m * y, 520 + n * x, 535 + m * y)
        self.sensor_1 = self.frame.create_rectangle(s1, fill='red')
        self.sensor_2 = self.frame.create_rectangle(s2, fill='red')
        self.sensor_3 = self.frame.create_rectangle(s3, fill='red')
        self.sensor_4 = self.frame.create_rectangle(s4, fill='red')
        self.agent = self.frame.create_oval(r, fill='cyan')
        self.frame.update()
        """Activate sensors"""
        for i in range(1, 5):
            time.sleep(0.1)
            if i == 1:
                self.beam_1 = self.frame.create_polygon(484 + n * x, 514 + m * y, 494 + n * x, 514 + m * y, 494 + n * x,
                                                        516 + m * y, 486 + n * x, 516 + m * y, 486 + n * x, 514 + m * y,
                                                        fill='yellow')
                self.beam_2 = self.frame.create_polygon(513 + n * x, 494 + m * y, 514 + n * x, 486 + m * y, 516 + n * x,
                                                        486 + m * y, 516 + n * x, 494 + m * y, 513 + n * x, 494 + m * y,
                                                        fill='yellow')
                self.beam_3 = self.frame.create_polygon(536 + n * x, 514 + m * y, 544 + n * x, 514 + m * y, 544 + n * x,
                                                        516 + m * y, 536 + n * x, 516 + m * y, 536 + n * x, 514 + m * y,
                                                        fill='yellow')
                self.beam_4 = self.frame.create_polygon(514 + n * x, 536 + m * y, 514 + n * x, 544 + m * y, 516 + n * x,
                                                        544 + m * y, 516 + n * x, 536 + m * y, 514 + n * x, 536 + m * y,
                                                        fill='yellow')
            if i == 2:
                self.beam_5 = self.frame.create_polygon(484 - a + n * x, 514 + m * y, 494 - a + n * x, 514 + m * y,
                                                        494 - a + n * x, 516 + m * y, 486 - a + n * x, 516 + m * y,
                                                        486 - a + n * x, 514 + m * y, fill='yellow')
                self.beam_6 = self.frame.create_polygon(513 + n * x, 494 - b + m * y, 514 + n * x, 486 - b + m * y,
                                                        516 + n * x, 486 - b + m * y, 516 + n * x, 494 - b + m * y,
                                                        513 + n * x, 494 - b + m * y, fill='yellow')
                self.beam_7 = self.frame.create_polygon(536 + a + n * x, 514 + m * y, 544 + a + n * x, 514 + m * y,
                                                        544 + a + n * x, 516 + m * y, 536 + a + n * x, 516 + m * y,
                                                        536 + a + n * x, 514 + m * y, fill='yellow')
                self.beam_8 = self.frame.create_polygon(514 + n * x, 536 + b + m * y, 514 + n * x, 544 + b + m * y,
                                                        516 + n * x, 544 + b + m * y, 516 + n * x, 536 + b + m * y,
                                                        514 + n * x, 536 + b + m * y, fill='yellow')
            if i == 3:
                self.beam_9 = self.frame.create_polygon(484 - 2 * a + n * x, 514 + m * y, 494 - 2 * a + n * x,
                                                        514 + m * y, 494 - 2 * a + n * x, 516 + m * y,
                                                        486 - 2 * a + n * x, 516 + m * y, 486 - 2 * a + n * x,
                                                        514 + m * y, fill='yellow')
                self.beam_10 = self.frame.create_polygon(514 + n * x, 494 - 2 * b + m * y, 514 + n * x,
                                                         486 - 2 * b + m * y, 516 + n * x, 486 - 2 * b + m * y,
                                                         516 + n * x, 494 - 2 * b + m * y, 514 + n * x,
                                                         494 - 2 * b + m * y, fill='yellow')
                self.beam_11 = self.frame.create_polygon(536 + 2 * a + n * x, 514 + m * y, 544 + 2 * a + n * x,
                                                         514 + m * y, 544 + 2 * a + n * x, 516 + m * y,
                                                         536 + 2 * a + n * x, 516 + m * y, 536 + 2 * a + n * x,
                                                         514 + m * y, fill='yellow')
                self.beam_12 = self.frame.create_polygon(514 + n * x, 536 + 2 * b + m * y, 514 + n * x,
                                                         544 + 2 * b + m * y, 516 + n * x, 544 + 2 * b + m * y,
                                                         516 + n * x, 536 + 2 * b + m * y, 514 + n * x,
                                                         536 + 2 * b + m * y, fill='yellow')
            if i == 4:
                self.beam_13 = self.frame.create_polygon(484 - 3 * a + n * x, 514 + m * y, 494 - 3 * a + n * x,
                                                         514 + m * y, 494 - 3 * a + n * x, 516 + m * y,
                                                         486 - 3 * a + n * x, 516 + m * y, 486 - 3 * a + n * x,
                                                         514 + m * y, fill='yellow')
                self.beam_14 = self.frame.create_polygon(514 + n * x, 494 - 3 * b + m * y, 514 + n * x,
                                                         486 - 3 * b + m * y, 516 + n * x, 486 - 3 * b + m * y,
                                                         516 + n * x, 494 - 3 * b + m * y, 514 + n * x,
                                                         494 - 3 * b + m * y, fill='yellow')
                self.beam_15 = self.frame.create_polygon(536 + 3 * a + n * x, 514 + m * y, 544 + 3 * a + n * x,
                                                         514 + m * y, 544 + 3 * a + n * x, 516 + m * y,
                                                         536 + 3 * a + n * x, 516 + m * y, 536 + 3 * a + n * x,
                                                         514 + m * y, fill='yellow')
                self.beam_16 = self.frame.create_polygon(514 + n * x, 536 + 3 * b + m * y, 514 + n * x,
                                                         544 + 3 * b + m * y, 516 + n * x, 544 + 3 * b + m * y,
                                                         516 + n * x, 536 + 3 * b + m * y, 514 + n * x,
                                                         536 + 3 * b + m * y, fill='yellow')
            self.frame.update()
        """"add walls and block"""
        """state 1"""
        if current_state == states[0][0]:
            self.frame.create_rectangle(350, 350, 570, 460, fill='grey')
            self.frame.create_rectangle(350, 570, 570, 680, fill='grey')
            self.frame.create_line(460, 460, 460, 570, fill='white', width=3)
            self.frame.create_line(460, 460, 570, 460, fill='white', width=5)
            self.frame.create_line(460, 570, 570, 570, fill='white', width=5)
        """state 2"""
        if current_state == states[1][0]:
            self.frame.create_line(350, 460, 460, 460, fill='white', width=5)
            self.frame.create_line(350, 570, 460, 570, fill='white', width=5)
        """state 3"""
        if current_state == states[2][0]:
            self.frame.create_rectangle(130, 350, 240, 570, fill='grey')
            self.frame.create_line(240, 460, 240, 570, fill='white', width=5)
        """state 4"""
        if current_state == states[3][0]:
            self.frame.create_line(240, 350, 240, 460, fill='white', width=5)
            self.frame.create_line(350, 350, 350, 460, fill='white', width=5)
        """state 6"""
        if current_state == states[5][0]:
            self.frame.create_rectangle(20, 20, 240, 240, fill='grey')
            self.frame.create_line(130, 240, 240, 240, fill='white', width=5)
            self.frame.create_line(130, 350, 240, 350, fill='white', width=5)
        """state 7"""
        if current_state == states[6][0]:
            self.frame.create_rectangle(20, 240, 130, 350, fill='light green')
            self.frame.create_line(130, 240, 130, 350, fill='white', width=3)
            self.frame.create_line(20, 240, 130, 240, fill='white', width=5)
            self.frame.create_line(20, 240, 20, 350, fill='white', width=5)
            self.frame.create_text(70, 255, text='Goal', font="Verdana 10 bold", fill='black')
        """state 8"""
        if current_state == states[7][0]:
            self.frame.create_rectangle(20, 20, 240, 240, fill='grey')
            self.frame.create_rectangle(350, 20, 570, 240, fill='grey')
            self.frame.create_line(240, 130, 240, 240, fill='white', width=5)
            self.frame.create_line(350, 130, 350, 240, fill='white', width=5)
        """state 9"""
        if current_state == states[8][0]:
            self.frame.create_rectangle(240, 20, 350, 130, fill='red')
            self.frame.create_line(240, 130, 350, 130, fill='white', width=3)
            self.frame.create_line(240, 20, 240, 130, fill='white', width=5)
            self.frame.create_line(350, 20, 350, 130, fill='white', width=5)
            self.frame.create_text(290, 35, text='PIT', font="Verdana 10 bold", fill='black')
        """state 10"""
        if current_state == states[9][0]:
            self.frame.create_line(350, 240, 460, 240, fill='white', width=5)
            self.frame.create_line(350, 350, 460, 350, fill='white', width=5)
        """state 11"""
        if current_state == states[10][0]:
            self.frame.create_rectangle(460, 240, 570, 350, fill='red')
            self.frame.create_line(460, 240, 460, 350, fill='white', width=3)
            self.frame.create_line(460, 240, 570, 240, fill='white', width=5)
            self.frame.create_line(460, 350, 570, 350, fill='white', width=5)
            self.frame.create_text(520, 255, text='PIT', font="Verdana 10 bold", fill='black')
        """state 12"""
        if current_state == states[11][0]:
            self.frame.create_line(350, 570, 350, 680, fill='white', width=5)
        """state 13"""
        if current_state == states[12][0]:
            self.frame.create_rectangle(20, 680, 240, 790, fill='grey')
            self.frame.create_line(240, 680, 240, 790, fill='white', width=5)
            self.frame.create_line(240, 790, 350, 790, fill='white', width=5)
        """state 14"""
        if current_state == states[13][0]:
            self.frame.create_line(350, 680, 460, 680, fill='white', width=5)
        """state 15"""
        if current_state == states[14][0]:
            self.frame.create_rectangle(460, 680, 570, 790, fill='red')
            self.frame.create_line(460, 680, 460, 790, fill='white', width=3)
            self.frame.create_line(460, 680, 570, 680, fill='white', width=5)
            self.frame.create_line(460, 790, 570, 790, fill='white', width=5)
            self.frame.create_text(520, 695, text='PIT', font="Verdana 10 bold", fill='black')
        """"state 16"""
        if current_state == states[15][0]:
            self.frame.create_rectangle(20, 680, 240, 790, fill='grey')
            self.frame.create_line(130, 570, 240, 570, fill='white', width=5)
            self.frame.create_line(130, 680, 240, 680, fill='white', width=5)
        """state 17"""
        if current_state == states[16][0]:
            self.frame.create_line(20, 680, 130, 680, fill='white', width=5)
        """state 18"""
        if current_state == states[17][0]:
            self.frame.create_line(130, 460, 130, 570, fill='white', width=5)
        self.frame.create_line(18, 20, 570, 20, 570, 790, 20, 790, 20, 20, fill='white', width=5)
        """state 19"""
        if current_state == states[18][0]:
            self.frame.create_rectangle(20, 350, 130, 460, fill='light green')
            self.frame.create_line(20, 460, 130, 460, fill='white', width=3)
            self.frame.create_line(130, 350, 130, 460, fill='white', width=5)
            self.frame.create_line(20, 350, 130, 350, fill='white', width=5)
            self.frame.create_text(70, 365, text='Goal', font="Verdana 10 bold", fill='black')
        """"delete sensors"""
        time.sleep(0.1)
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

    def robot_search_phase(self):

        global current_state
        coords = [[500, 500], [390, 500], [280, 500], [280, 390], [280, 280], [170, 280], [60, 280], [280, 170],
                  [280, 60], [390, 280], [500, 280], [280, 610], [280, 720], [390, 720], [500, 720], [170, 610],
                  [60, 610], [60, 500], [60, 390]]
        self.start_world()
        self.frame.create_rectangle(460, 460, 570, 570, fill='lime green')
        self.frame.create_text(520, 475, text='START', font="Verdana 10 bold", fill='black')
        self.frame.create_line(18, 20, 570, 20, 570, 790, 20, 790, 20, 20, fill='white', width=5)
        current_state = 1
        """move the robot main LOOP"""
        for i in range(1, 20):
            for x in range(1, 9):
                # time.sleep(0.1)
                print('x =', x)
                self.robot()
                if current_state == 7 or current_state == 9 or current_state == 11:
                    current_state = 1
                    break
                if current_state == 15 or current_state == 19:
                    current_state = 1
                    break
                s = self.frame.coords(self.agent)
                print('s=', s)
                current_coords = [int(s[0]), int(s[1])]
                print('current coords', current_coords)
                """generate start and final counter"""
                if self.move == 'left':
                    start_sum = s[0] + s[2]
                    adjust = -220
                    final_sum = start_sum + adjust
                    move_agent = np.array([-1, 0])
                    move_sensors = np.array([-1, 0])
                if self.move == 'up':
                    start_sum = s[1] + s[3]
                    adjust = -220
                    final_sum = start_sum + adjust
                    move_agent = np.array([0, -1])
                    move_sensors = np.array([0, -1])
                if self.move == 'right':
                    start_sum = s[0] + s[2]
                    adjust = 220
                    final_sum = start_sum + adjust
                    move_agent = np.array([1, 0])
                    move_sensors = np.array([1, 0])
                if self.move == 'down':
                    start_sum = s[1] + s[3]
                    adjust = 220
                    final_sum = start_sum + adjust
                    move_agent = np.array([0, 1])
                    move_sensors = np.array([0, 1])
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
                        time.sleep(0.01)
                if self.move == 'right' or self.move == 'down':
                    while final_sum > start_sum:
                        self.frame.move(self.agent, move_agent[0], move_agent[1])
                        self.frame.move(self.sensor_1, move_sensors[0], move_agent[1])
                        self.frame.move(self.sensor_2, move_sensors[0], move_agent[1])
                        self.frame.move(self.sensor_3, move_sensors[0], move_agent[1])
                        self.frame.move(self.sensor_4, move_sensors[0], move_agent[1])
                        self.frame.update()
                        """move robot one step at a time"""
                        start_sum = start_sum + 2
                        time.sleep(0.01)
                """definte current state value"""
                s = self.frame.coords(self.agent)
                print('coords = ', s)
                current_state_coords = [int(s[0]), int(s[1])]
                print('state coords =', current_state_coords)
                for a in range(0, len(coords)):
                    if coords[a] == current_state_coords:
                        current_state = states[a][0]
                print('current state =', current_state)

        self.root.mainloop()

data = SensorWorld()
# data.grid()
# data.start_world()
data.robot_search_phase()
