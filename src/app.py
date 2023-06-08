import customtkinter as ctk
from plotter import ExpressionPlotter
from widgets import WidgetFrame

from settings import openJson, readJson

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        data = openJson()
        expression, xmin, xmax, ymin, ymax, theme, grid = readJson(data)

        ctk.set_appearance_mode(theme)
        ctk.ThemeManager.load_theme("blue")

        self.title("Grapher")
        self.geometry("1200x500")

        # configure columns and rows
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.expressionplotter = ExpressionPlotter(
            self,
            expression=expression,
            xmin=xmin,
            xmax=xmax,
            ymin=ymin,
            ymax=ymax,
            grid=grid
        )

        self.widgetFrame = WidgetFrame(self)
        self.widgetFrame.grid(row=0, column=0, padx=20, pady=20, stick="EWNS")

