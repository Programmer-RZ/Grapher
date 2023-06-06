import customtkinter as ctk
from customwidgets.spinbox import FloatSpinbox

class WidgetFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)

        self.graphWidgetFrame = GraphWidgetFrame(self, window)
        self.graphWidgetFrame.grid(row=0, column=0, padx=10, pady=10, sticky="EWNS")

        self.appearanceWidgetFrame = AppearanceWidgetFrame(self, window)
        self.appearanceWidgetFrame.grid(row=1, column=0, padx=10, pady=10, sticky="EWNS")

class GraphWidgetFrame(ctk.CTkFrame):
    def __init__(self, window, MAIN_WINDOW):
        super().__init__(window)
        self.graphWidget = GraphWidgets(self, MAIN_WINDOW.expressionplotter)

class AppearanceWidgetFrame(ctk.CTkFrame):
    def __init__(self, window, MAIN_WINDOW):
        super().__init__(window)
        self.appearanceWidget = AppearanceWidgets(self, MAIN_WINDOW.expressionplotter)



class GraphWidgets():
    def __init__(self, frame, plotter):
        self.plotter = plotter
        

        self.text_frame = ctk.CTkFrame(master=frame)
        self.label = ctk.CTkLabel(
            master=self.text_frame,
            text=f"y = {plotter.expression}",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.pack(padx=10, pady=10)
        self.text_frame.grid(row=0, padx=10, pady=20)



        # edit expression
        self.button = ctk.CTkButton(
            master=frame, 
            text="Edit expression", 
            command=self.editEquation,
            border_width=3
        )
        self.button.grid(row=0, column=1)




        # left most x value
        self.xmin_label = ctk.CTkButton(frame, 
                                       text=f"Left X",
                                       command=self.editXmin,
                                       width=100,
                                       border_width=3,
                                       )
        self.xmin_label.grid(row=1, padx=10)

        self.xmin_spinbox = FloatSpinbox(frame, 
                                            width=150, step_size=100, 
                                            command=lambda : self.setXmin(self.xmin_spinbox)
                                            )
        self.xmin_spinbox.set(self.plotter.xmin)
        self.xmin_spinbox.grid(row=1, column=1, padx=10)




        # right most x value
        self.xmax_label = ctk.CTkButton(frame, 
                                       text=f"Right X",
                                       width=100,
                                       command=self.editXmax,
                                       border_width=3,
                                       )
        self.xmax_label.grid(row=2, padx=10, pady=10)

        self.xmax_spinbox = FloatSpinbox(frame, 
                                            width=150, step_size=100, 
                                            command=lambda : self.setXmax(self.xmax_spinbox)
                                            )
        self.xmax_spinbox.set(self.plotter.xmax)
        self.xmax_spinbox.grid(row=2, column=1, padx=10, pady=10)




        # bottom most y value
        self.ymin_label = ctk.CTkButton(frame, 
                                       text=f"Bottom Y",
                                       width=100,
                                       command=self.editYmin,
                                       border_width=3,
                                       )
        self.ymin_label.grid(row=3, padx=10)

        self.ymin_spinbox = FloatSpinbox(frame, 
                                            width=150, step_size=1000, 
                                            command=lambda : self.setYmin(self.ymin_spinbox)
                                            )
        self.ymin_spinbox.set(self.plotter.ymin)
        self.ymin_spinbox.grid(row=3, column=1, padx=10)




        # up most y value
        self.ymax_label = ctk.CTkButton(frame, 
                                       text=f"Up Y",
                                       width=100,
                                       command=self.editYmax,
                                       border_width=3,
                                       )
        self.ymax_label.grid(row=4, padx=10, pady=10)

        self.ymax_spinbox = FloatSpinbox(frame, 
                                            width=150, step_size=1000, 
                                            command=lambda : self.setYmax(self.ymax_spinbox)
                                            )
        self.ymax_spinbox.set(self.plotter.ymax)
        self.ymax_spinbox.grid(row=4, column=1, padx=10, pady=10)




    def setXmin(self, xmin):
        self.plotter.xmin = xmin.get()
        self.plotter.updateplot(self.plotter.expression)
    def setXmax(self, xmax):
        self.plotter.xmax = xmax.get()
        self.plotter.updateplot(self.plotter.expression)
    def setYmin(self, ymin):
        self.plotter.ymin = ymin.get()
        self.plotter.updateplot(self.plotter.expression)
    def setYmax(self, ymax):
        self.plotter.ymax = ymax.get()
        self.plotter.updateplot(self.plotter.expression)



    def editYmin(self):
        dialog = ctk.CTkInputDialog(
            text=f"Type in a value.", 
            title="Edit bottom Y value"
        )

        try:
            new_ymin = int(dialog.get_input())
        except ValueError:
            return
        except TypeError:
            return

        self.plotter.ymin = new_ymin
        self.plotter.updateplot(self.plotter.expression)

        self.ymin_spinbox.set(self.plotter.ymin)

    def editYmax(self):
        dialog = ctk.CTkInputDialog(
            text=f"Type in a value.", 
            title="Edit up Y value"
        )

        try:
            new_ymax = int(dialog.get_input())
        except ValueError:
            return
        except TypeError:
            return

        self.plotter.ymax = new_ymax
        self.plotter.updateplot(self.plotter.expression)

        self.ymax_spinbox.set(self.plotter.ymax)

    def editXmin(self):
        dialog = ctk.CTkInputDialog(
            text=f"Type in a value.", 
            title="Edit left X value"
        )

        try:
            new_xmin = int(dialog.get_input())
        except ValueError:
            return
        except TypeError:
            return

        self.plotter.xmin = new_xmin
        self.plotter.updateplot(self.plotter.expression)

        self.xmin_spinbox.set(self.plotter.xmin)
    def editXmax(self):
        dialog = ctk.CTkInputDialog(
            text=f"Type in a value.", 
            title="Edit right X value"
        )

        try:
            new_xmax = int(dialog.get_input())
        except ValueError:
            return
        except TypeError:
            return

        self.plotter.xmax = new_xmax
        self.plotter.updateplot(self.plotter.expression)

        self.xmax_spinbox.set(self.plotter.xmax)




    def editEquation(self):
        dialog = ctk.CTkInputDialog(
            text="Type in a linear or quadratic expression.\nExample: x+5", 
            title="Edit expression"
        )

        new_expression = dialog.get_input()

        if new_expression == None:
            return

        # lowercase the whole expression
        new_expression.lower()

        if "x" not in new_expression:
            return
        
        # check no consecutive letters
        isLetter = False
        for symbol in new_expression:
            if symbol.lower().isalpha():
                if isLetter:
                    # previous letter was letter
                    # it's consecutive
                    return
                else:
                    isLetter = True
            else:
                isLetter = False

        # all requirements match up
        self.plotter.updateplot(new_expression)
        self.label.configure(text=f"y = {new_expression}")

class AppearanceWidgets:
    def __init__(self, frame, plotter):
        self.plotter = plotter

        self.isGrid = ctk.StringVar(value="on")
        self.gridCheckButton = ctk.CTkCheckBox(
            frame, 
            text="Grid", 
            command=self.setGrid,
            variable=self.isGrid,
            onvalue="on",
            offvalue="off"
        )
        self.gridCheckButton.grid(row=0, column=0, padx=10, pady=10)



        self.appearance_mode = ctk.CTkOptionMenu(frame, values=["System", "Dark", "Light"])
        self.appearance_mode.grid(row=0, column=1, padx=10, pady=10)

    def setGrid(self):
        self.plotter.haveGrid = True if self.isGrid.get()=="on" else False
        self.plotter.updateplot(self.plotter.expression)
    def setAppearance(self, choice):
        ctk.set_appearance_mode(choice.lower())