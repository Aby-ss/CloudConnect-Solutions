from datetime import datetime
import csv
import time
from time import sleep
import math
import keyboard
import numpy as np
import asciichartpy

from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body"),
    Layout(name = "Footer")
)

layout["Body"].split_column(
    Layout(name = "Upper_Body"),
    Layout(name = "Lower_Body")
)

layout["Upper_Body"].split_row(
    Layout(name = "UB_1"),
    Layout(name = "UB_2")
)

layout["UB_2"].split_column(
    Layout(name = "UB2_1"),
    Layout(name = "UB2_2", ratio = 1)
)

layout["Lower_Body"].split_row(
    Layout(name = "LB_1"),
    Layout(name = "LB_2")
)

class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "👔", "[b]CloudConnect-Solutions[/] Manager Panel", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white")
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "💻", "[b]Simplifying Collaboration. Empowering Success.[/]", "📊")
        return Panel(grid, style="blue on black")
    


def Employee_comms():
    IT_Comms = []
    HR_comms = []
    Other_comms = []

    for i in range(60):
        IT_Comms.append(15 * math.cos(i * ((math.pi * 2) / 60)))  # values range from -15 to +15
        HR_comms.append(10 * math.sin(i * ((math.pi * 4) / 60)))  # values range from -10 to +10
        Other_comms.append(8 * math.sin(i * ((math.pi * 8) / 60)))  # values range from -8 to +8

    data = [IT_Comms, HR_comms, Other_comms]
    graph = asciichartpy.plot(data, {'height': 15, 'width': 10})  # rescales the graph to ±3 lines
    return Panel(graph, border_style = "Bold white", box = box.SQUARE, title = "Communication channels Analysis", title_align="left")

def Employee_database():
    EDB = Table(title="Employee Database")
    EDB.add_column(justify="left", header="Name")
    EDB.add_column(justify="center", header="Department")
    EDB.add_column(justify="center", header="Current Task")
    EDB.add_column(justify="center", header="ID")
    EDB.add_column(justify="right", header="Status")
    
    EDB.add_row("Ansh Jon", "Finances", "Clear May's final statement ✅", "65", "Active")
    EDB.add_row("Jimmy", "Sales", "Complete the new strategy process ✅", "8", "Offline")
    EDB.add_row("Alfred", "Finances", "Clear debt for previous 5 months 🟥", "56", "Active")
    EDB.add_row("Wayne", "Manufacturing", "Add new products to line up 🟥", "88", "Active")
    EDB.add_row("Jhon", "Security", "Clear up tomorrow event list ✅", "654", "Offline")
    EDB.add_row("Emma", "Marketing", "Launch the new advertising campaign ✅", "12", "Active")
    EDB.add_row("Sarah", "Human Resources", "Conduct employee performance reviews ✅", "25", "Active")
    EDB.add_row("David", "IT", "Upgrade network infrastructure 🟥", "78", "Offline")
    EDB.add_row("Linda", "Operations", "Streamline supply chain processes ✅", "36", "Active")

    return EDB

def team_performance():
    TP_panel = Panel("[b]Finances:[/][b red] 30%[/]\n\n[b]Marketing:[/][b green] 84%[/]\n\n[b]Production:[/][b yellow]5 4%[/]\n\n[b]Human Resources:[/][b green] 90%[/]", title="Team Performance", box = box.SQUARE, border_style = "bold white")
    
    return TP_panel


with Live(layout, refresh_per_second=10, screen=True):
    while True:
        
        layout["Header"].size = 3
        layout["Footer"].size = 3
        layout["Header"].update(Header())
        layout["Footer"].update(Footer())
        layout["UB_1"].update(Employee_comms())
        layout["LB_1"].update(Employee_database())
        layout["UB2_2"].update(team_performance())

        if keyboard.is_pressed("q"):
            exit()
            
print(layout)