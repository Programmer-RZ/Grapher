import customtkinter as ctk
from plotter import ExpressionPlotter
from widgets import WidgetFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("system")
        ctk.ThemeManager.load_theme("blue")

        self.title("Grapher")
        self.geometry("1200x500")

        # configure columns and rows
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.expressionplotter = ExpressionPlotter(self)

        self.widgetFrame = WidgetFrame(self)
        self.widgetFrame.grid(row=0, column=0, padx=20, pady=20, stick="EWNS")

