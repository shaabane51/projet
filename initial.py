import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        

        
        self.x = np.linspace(0, 20, 256)
        self.y = np.linspace(0, 20, 256)
        

        
        self.line = Line2D([], [], color='black')
        self.arrow = Line2D(
            [], [], color='red', marker='v', markeredgecolor='r')
        ax1.add_line(self.line)
        ax1.add_line(self.arrow)
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 10)
        plt.plot([1, 2, 3, 4,5,6,7,8,9,10,], [1,2,3, 4,5,6,7,8,9,10,],'^k')
        

        animation.TimedAnimation.__init__(self, fig, interval=350, blit=True)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
       

        self.line.set_data(self.x[:i], self.y[:i])
        self.arrow.set_data(self.x[head], self.y[head])

       

    def new_frame_seq(self):
        return iter(range(self.x.size))


ani = SubplotAnimation()

plt.show()
