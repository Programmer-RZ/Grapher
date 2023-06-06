import customtkinter as ctk
import customwidgets as cw

class WidgetFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)

        self.state = "expressionwidget"

        if self.state == "expressionwidget":
            self.equationWidget = ExpressionWidgets(self, window.expressionplotter)

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
            border_width=3
        )
        self.button.grid(row=0, column=1)



        # edit graph values
        self.xmin_label = ctk.CTkLabel(frame, 
                                       text=f"Min X = {self.plotter.xmin}"
                                       )
        self.xmin_label.grid(row=1, padx=10)

        self.xmin_spinbox = cw.FloatSpinbox(frame, 
                                            min=self.plotter.xmin_limits[0],
                                            max=self.plotter.xmin_limits[1],
                                            width=150, step_size=10, 
                                            command=lambda : self.editXmin(self.xmin_spinbox)
                                            )
        self.xmin_spinbox.set(self.plotter.xmin)
        self.xmin_spinbox.grid(row=1, column=1)


        self.xmax_label = ctk.CTkLabel(frame, 
                                       text=f"Max X = {self.plotter.xmax}"
                                       )
        self.xmax_label.grid(row=2, padx=10)

        self.xmax_spinbox = cw.FloatSpinbox(frame, 
                                            min=self.plotter.xmax_limits[0],
                                            max=self.plotter.xmax_limits[1],
                                            width=150, step_size=10, 
                                            command=lambda : self.editXmax(self.xmax_spinbox)
                                            )
        self.xmax_spinbox.set(self.plotter.xmax)
        self.xmax_spinbox.grid(row=2, column=1)

    def editXmin(self, xmin):
        self.plotter.xmin = xmin.get()
        self.plotter.updateplot(self.plotter.expression)
        self.xmin_label.configure(text=f"Min X = {self.plotter.xmin}")
    def editXmax(self, xmax):
        self.plotter.xmax = xmax.get()
        self.plotter.updateplot(self.plotter.expression)
        self.xmax_label.configure(text=f"Max X = {self.plotter.xmax}")

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

        