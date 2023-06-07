import customtkinter as ctk
from customwidgets.spinbox import FloatSpinbox

class WidgetFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)

        self.exprWidgetFrame = ExpressionWidgetFrame(self, window)
        self.exprWidgetFrame.grid(row=0, column=0, padx=10, pady=10, sticky="EWNS")

        self.graphValuesFrame = GraphValuesWidgetFrame(self, window)
        self.graphValuesFrame.grid(row=1, column=0, padx=10, pady=10, sticky="EWNS")

        self.appearanceWidgetFrame = AppearanceWidgetFrame(self, window)
        self.appearanceWidgetFrame.grid(row=2, column=0, padx=10, pady=10, sticky="EWNS")

class ExpressionWidgetFrame(ctk.CTkFrame):
    def __init__(self, window, MAIN_WINDOW):
        super().__init__(window)
        self.graphWidget = ExpressionWidgets(self, MAIN_WINDOW.expressionplotter)

class AppearanceWidgetFrame(ctk.CTkFrame):
    def __init__(self, window, MAIN_WINDOW):
        super().__init__(window)
        self.appearanceWidget = AppearanceWidgets(self, MAIN_WINDOW.expressionplotter)

class GraphValuesWidgetFrame(ctk.CTkFrame):
    def __init__(self, window, MAIN_WINDOW):
        super().__init__(window)
        self.graphvalueWIdget = GraphValuesWidgets(self, MAIN_WINDOW.expressionplotter)

class GraphValuesWidgets():
    def __init__(self, frame, plotter):
        self.plotter = plotter

        self.editValue = ctk.CTkOptionMenu(frame, values=
                                           ["Left X", "Right X", "Bottom Y", "Top Y"],
                                           command=self.setEditValue)
        self.editValue.grid(row=0, column=0, padx=10, pady=10)

        
        self.valueLabel = ctk.CTkLabel(master=frame, text="Editing value Left X")
        self.valueLabel.grid(row=0, column=1, padx=10)

        # default value
        self.valueButton = ctk.CTkButton(
            frame,
            text=f"Edit left X",
            command=self.editXmin,
            width=100,
        )
        self.valueButton.grid(row=1, column=0, padx=10, pady=10)

        # default value
        self.value_spinbox = FloatSpinbox(frame, 
                                            width=150, step_size=100, 
                                            command=lambda : self.setXmin(self.value_spinbox)
                                            )
        self.value_spinbox.set(self.plotter.xmin)
        self.value_spinbox.grid(row=1, column=1, padx=10, pady=10)


    def setEditValue(self, choice):
        if choice == "Left X":
            self.valueButton.configure(text="Edit left X", command=self.editXmin)

            self.value_spinbox.command = lambda : self.setXmin(self.value_spinbox)
            self.value_spinbox.set(self.plotter.xmin)
            
        elif choice == "Right X":
            self.valueButton.configure(text="Edit right X", command=self.editXmax)

            self.value_spinbox.command = lambda : self.setXmax(self.value_spinbox)
            self.value_spinbox.set(self.plotter.xmax)

        elif choice == "Bottom Y":
            self.valueButton.configure(text="Edit bottom Y", command=self.editYmin)

            self.value_spinbox.command = lambda : self.setYmin(self.value_spinbox)
            self.value_spinbox.set(self.plotter.ymin)

        elif choice == "Up Y":
            self.valueButton.configure(text="Edit up Y", command=self.editYmax)

            self.value_spinbox.command = lambda : self.setYmax(self.value_spinbox)
            self.value_spinbox.set(self.plotter.ymax)


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

        self.value_spinbox.set(self.plotter.ymin)

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

        self.value_spinbox.set(self.plotter.ymax)

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

        self.value_spinbox.set(self.plotter.xmin)
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

        self.value_spinbox.set(self.plotter.xmax)


class ExpressionWidgets():
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
        )
        self.button.grid(row=0, column=1, padx=10)



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



        self.appearance_mode = ctk.CTkOptionMenu(frame,
                                                  values=["System", "Dark", "Light"],
                                                  command=self.setAppearance)
        self.appearance_mode.grid(row=0, column=1, padx=10, pady=10)

    def setGrid(self):
        self.plotter.haveGrid = True if self.isGrid.get()=="on" else False
        self.plotter.updateplot(self.plotter.expression)
    def setAppearance(self, choice):
        ctk.set_appearance_mode(choice.lower())