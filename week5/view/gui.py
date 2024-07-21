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

        self.cell_width = 800 // self.environment.get_width()
        self.cell_height = 600 // self.environment.get_height()

        # Dictionary to store previous state of each cell
        self.previous_state = {}

        self.agent_colors = {
            Shark: "red",
            Sardine: "blue",
            Plankton: "green",
        }

        # Initialize the canvas with the initial state of the environment
        self.initialize_canvas()

    def initialize_canvas(self):
        for row in range(self.environment.get_height()):
            for col in range(self.environment.get_width()):
                location = Location(col, row)
                agent = self.environment.get_agent(location)

                # Calculate rectangle coordinates
                x0 = col * self.cell_width
                y0 = row * self.cell_height
                x1 = x0 + self.cell_width
                y1 = y0 + self.cell_height

                # Determine the color to use
                color = self.agent_colors.get(type(agent), "white") if agent else "white"

                # Create a unique key for the cell
                key = (col, row)

                # Draw initial state
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
                self.previous_state[key] = color

    def update_display(self):
        for row in range(self.environment.get_height()):
            for col in range(self.environment.get_width()):
                location = Location(col, row)
                agent = self.environment.get_agent(location)

                # Calculate rectangle coordinates
                x0 = col * self.cell_width
                y0 = row * self.cell_height
                x1 = x0 + self.cell_width
                y1 = y0 + self.cell_height

                # Determine the color to use
                color = self.agent_colors.get(type(agent), "white") if agent else "white"

                # Create a unique key for the cell
                key = (col, row)

                # Check if the state of the cell has changed
                if self.previous_state.get(key) != color:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
                    self.previous_state[key] = color

        self.update_idletasks()
