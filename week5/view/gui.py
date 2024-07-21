import tkinter as tk
from week5.model.location import Location
from week5.model.plankton import Plankton
from week5.model.sardine import Sardine
from week5.model.shark import Shark


class GUI(tk.Tk):

    def __init__(self, environment, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.environment = environment
        self.title("Ocean Simulator")
        self.geometry("800x600")
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()
        self.agent_colors = {
            Shark: "red",
            Sardine: "blue",
            Plankton: "green",
        }
        self.update_display()

    def update_display(self):
        self.canvas.delete("all")
        cell_width = 800 // self.environment.get_width()
        cell_height = 600 // self.environment.get_height()
        for row in range(self.environment.get_height()):
            for col in range(self.environment.get_width()):
                location = Location(col, row)
                agent = self.environment.get_agent(location)
                x0 = col * cell_width
                y0 = row * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height
                if agent is None:
                    color = "white"
                else:
                    color = self.agent_colors.get(type(agent), "black")
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        self.update_idletasks()
