import tkinter as tk


class SensorWorld:

    def __init__(self):
        self.root = tk
        self.frame = self.root.Canvas(bg='sea green', height=820, width=588)
        self.frame.pack()
        self.agent = ()
        self.sensor_1 = ()
        self.sensor_2 = ()
        self.sensor_3 = ()
        self.sensor_4 = ()

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
        self.frame.create_rectangle(460, 460, 570, 570, fill='yellow')
        self.frame.create_rectangle(460, 240, 570, 350, fill='red')
        self.frame.create_rectangle(240, 20, 350, 130, fill='red')
        self.frame.create_rectangle(460, 680, 570, 790, fill='red')
        """Titles"""
        self.frame.create_text(515, 475, text='Start', font="Verdana 10 bold", fill='black')
        self.frame.create_text(70, 255, text='Goal', font="Verdana 10 bold", fill='black')
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
        self.frame.create_line(130, 350, 130, 460, fill='white', width=5)
        self.frame.create_text(70, 410, text='19', font="Verdana 15 bold", fill='white')
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
        self.frame.create_line(460, 240, 570, 240, fill='white', width=5)
        self.frame.create_line(460, 350, 570, 350, fill='white', width=5)
        self.frame.create_text(510, 300, text='11', font="Verdana 15 bold", fill='white')
        """State 10"""
        self.frame.create_line(350, 240, 460, 240, fill='white', width=5)
        self.frame.create_line(350, 350, 460, 350, fill='white', width=5)
        self.frame.create_text(400, 300, text='10', font="Verdana 15 bold", fill='white')
        """State 9"""
        self.frame.create_line(240, 20, 240, 130, fill='white', width=5)
        self.frame.create_line(350, 20, 350, 130, fill='white', width=5)
        self.frame.create_text(290, 80, text='9', font="Verdana 15 bold", fill='white')
        """State 8"""
        self.frame.create_line(240, 130, 240, 240, fill='white', width=5)
        self.frame.create_line(350, 130, 350, 240, fill='white', width=5)
        self.frame.create_text(290, 190, text='8', font="Verdana 15 bold", fill='white')
        """State 7"""
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

        self.root.mainloop()

data = SensorWorld()
# data.grid()
data.start_world()
