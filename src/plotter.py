import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

from numpy import arange
from re import sub

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
    def __init__(self, window, 
                 expression="x", 
                 xmin=-100, 
                 xmax=100, 
                 ymin=0, 
                 ymax=1000,
                 grid=True):
        self.x = []
        self.y = []
        self.expression = expression

        self.xmin = xmin
        self.xmax = xmax

        self.ymin = ymin
        self.ymax = ymax


        self.haveGrid = grid

        self.fig = Figure(figsize = (10, 5), dpi=100)
        self.ax1 = self.fig.add_subplot(1, 1, 1)

        self.updateplot(self.expression)

        self.graphframe = GraphFrame(window, self.fig)
        self.graphframe.grid(row=0, column=1, padx=20, pady=20, sticky="EWNS")

    def updateplot(self, expression):
        self.x = arange(self.xmin, self.xmax, 1)
        self.updateExpression(expression)

        self.fig.clear()

        self.ax1 = self.fig.add_subplot(1, 1, 1)

        self.ax1.set_ylim(self.ymin, self.ymax)
        self.ax1.set_xlim(self.xmin, self.xmax)
        self.ax1.plot(self.x, self.y)

        if self.haveGrid:
            self.ax1.grid()

        self.fig.canvas.draw()

    def updateExpression(self, expression):
        try:
            # sanitize the expression
            allowed_chars = r"[0-9+\-*/()x\s]"
            if sub(allowed_chars, '', expression):
                raise ValueError("Invalid characters")

            x = self.x
            self.y = eval(expression)
            self.expression = expression

        except Exception as e:
            print(f"Invalid expression: {repr(e)}")


