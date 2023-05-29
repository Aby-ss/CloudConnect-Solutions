from datetime import datetime
import csv
import time
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
from rich.progress import Progress

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
            "👔", "[b]CloudConnect-Solutions[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
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
    
layout["Header"].size = 3
layout["Footer"].size = 3
layout["Header"].update(Header())
layout["Footer"].update(Footer())

print(layout)