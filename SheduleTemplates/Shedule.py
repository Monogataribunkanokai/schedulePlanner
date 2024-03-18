from string import Template

cssPath='SheduleTemplate.css'
headder=Template('<head><link rel="stylesheet" type="text/css" href="$cssPath"/></head>')
print(headder.substitute(cssPath=cssPath))

class Shedule():
    def __init__(self) -> None:
        pass