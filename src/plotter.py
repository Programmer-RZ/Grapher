import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

from numpy import arange

class GraphFrame(ctk.CTkFrame):
    def __init__(self, window, fig):
        super().__init__(window)

        self.canvas = FigureCanvasTkAgg(fig, master=self)  
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(padx=20, pady=20)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
      
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()

class ExpressionPlotter:
    def __init__(self, window):
        self.x = []
        self.y = []
        self.expression = "x"

        self.xmin = -100
        self.xmax = 100

        self.ymin = 0
        self.ymax = 200

        self.fig = Figure(figsize = (10, 5), dpi=100)
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax1.grid()

        self.updateplot(self.expression)

        self.graphframe = GraphFrame(window, self.fig)
        self.graphframe.grid(row=0, column=1, padx=20, pady=20, sticky="EWNS")

    def updateplot(self, expression):
        self.x = arange(self.xmin, self.xmax, 1)
        self.updateExpression(expression)
        self.y = self.y

        self.fig.clear()

        self.ax1 = self.fig.add_subplot(1, 1, 1)

        self.ax1.set_ylim(self.ymin, self.ymax)
        self.ax1.set_xlim(self.xmin, self.xmax)

        self.ax1.grid()
        self.ax1.plot(self.x, self.y)

        self.fig.canvas.draw()

    def updateExpression(self, expression):
        try:
            x = self.x
            self.y = eval(expression)
            self.expression = expression
        except SyntaxError:
            pass


