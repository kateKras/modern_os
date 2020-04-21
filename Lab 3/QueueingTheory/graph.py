import scipy as sp
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.x = []
        self.y = []

    def title(self, title):
        plt.title(title)

    def set_values(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def y_label(self, label):
        plt.ylabel(label)

    def x_label(self, label):
        plt.xlabel(label)

    def show(self, smooth = False):
        if (smooth):
            p = sp.polyfit(self.x, self.y, deg=5)
            y_ = sp.polyval(p, self.x)
            plt.plot(self.x, y_)
            plt.show()
        else:
            plt.plot(self.x, self.y)
            plt.show()

    def show_hist(self, values):
        plt.hist(values, bins=15)
        plt.show()
