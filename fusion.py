import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        m = np.array([[0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 0, 0], [0, 1, 0, 0 ,0]]) 
        cluster_1 = np.array([[1, 2, 3], [3, 4, 3]]) 
        c = cluster_1 
        

        for i in range(c.shape[1]): 
            for j in range(c.shape[1]): 
                if m[c[0,i]-1,c[1,j]-1]: 
                 m[c[0,i]-1,c[1,j]-1] = 1
               

        self.x = np.linspace(0, 200, 256)
        self.y = np.linspace(0, 200, 256)



        
        self.line = Line2D([], [], color='black')
        self.robot = Line2D(
            [], [], color='red', marker='v', markeredgecolor='r')
        ax1.add_line(self.line)
        ax1.add_line(self.robot)
        ax1.set_xlim(0, 100)
        ax1.set_ylim(0, 100)
        plt.plot([10, ], [10,],'sk')
       

        animation.TimedAnimation.__init__(self, fig, interval=100, blit=True)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
       

        self.line.set_data(self.x[:i], self.y[:i])
        self.robot.set_data(self.x[head], self.y[head])

       

    def new_frame_seq(self):
        return iter(range(self.x.size))
        
# creation de la grille 
grid_x_ticks = np.arange(1)
grid_y_ticks = np.arange(1)


ani = SubplotAnimation()
plt.grid()
plt.show()
