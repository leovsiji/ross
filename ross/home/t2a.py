from pyfiglet import Figlet

COLORS = {
    "No Color": "",
    "BLACK": "black",
    "RED": "red",
    "GREEN": "green",
    "BLUE": "blue",
    "CYAN": "cyan",
}

def textoa(text, font, color_name):
    fig = Figlet(font=font)
    color = COLORS.get(color_name, "")
    return fig.renderText(text)

def code(text, font, color_name):
    if color_name == "No Color":
        return f'''from pyfiglet import Figlet

fig = Figlet(font="{font}")
print(fig.renderText("{text}"))
'''
    else:
        return f'''from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

fig = Figlet(font="{font}")
print(Fore.{color_name} + fig.renderText("{text}") + Style.RESET_ALL)
'''