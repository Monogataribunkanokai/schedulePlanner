from string import Template
from datetime import time

cssPath='SheduleTemplate.css'
headder=Template('<head><link rel="stylesheet" type="text/css" href="$cssPath"/></head>')
print(headder.substitute(cssPath=cssPath))

class Shedule():
    def __init__(self) -> None:
        self.days:list[Event]
class DayEvent():
    def __init__(self) -> None:
        pass
class Event():
    def __init__(self) -> None:
        self.startTime:time
        self.endTime:time
        self.place:Place
class Place():
    def __init__(self) -> None:
        self.Caption:str
class Group():
    def __init__(self) -> None:
        self.members:list[Member]=[]
        self.caption:str
        self.name:str
class Member():
    def __init__(self) -> None:
        self.name:str
        self.grade:tuple
        self.sex:bool
        self.party:Party
        self.role:Role
class Party():
    def __init__(self) -> None:
        pass
class Role():
    def __init__(self) -> None:
        pass