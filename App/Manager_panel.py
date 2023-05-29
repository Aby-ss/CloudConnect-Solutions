from datetime import datetime
import csv
import time
from time import sleep
import math
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

def Teams_stats():
    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    job_progress.add_task("[green]Downloading firm data from cloud")
    job_progress.add_task("[magenta]Performing finances", total=200)
    job_progress.add_task("[cyan]Calculating porfits", total=400)

    total = sum(task.total for task in job_progress.tasks)
    overall_progress = Progress()
    overall_task = overall_progress.add_task("All Jobs", total=int(total))

    progress_table = Table.grid(expand=True)
    progress_table.add_row(
        Panel(
            overall_progress,
            title="Overall Progress",
            border_style="green",
            padding=(2, 2),
        ),
        Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
    ) 
    
    return progress_table


layout["Header"].size = 3
layout["Footer"].size = 3
layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["UB_1"].update(Employee_comms())
layout["UB2_1"].update(Teams_stats())


print(layout)