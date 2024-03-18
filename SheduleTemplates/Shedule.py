from string import Template
from datetime import time,date

cssPath='SheduleTemplate.css'
headder=Template('<head><link rel="stylesheet" type="text/css" href="$cssPath"/></head>')
#print(headder.substitute(cssPath=cssPath))

class DayEvent():
    def __init__(self) -> None:
        self.__events:list[Event]=[]
class Shedule():
    def __init__(self,start_day:date,name:str='',caption:str='') -> None:
        self.__days:list[DayEvent]=[]
        self.__start_day=start_day
        self.__name:str=name
        self.__caption:str=caption
    @property
    def days(self):
        return self.__days
    @property
    def start_day(self):
        return self.__start_day
    @property
    def name(self):
        return self.__name
    @property
    def caption(self):
        return self.caption
    def add_day(self,day):
        self.__days.append(day)
    def get_days(self):
        return len(self.__days)
class Event():
    def __init__(self) -> None:
        self.__start_time:time
        self.__end_time:time
        self.__exe_time:time
        self.__caption:str
        self.__Place:list[Place]=[]
class Place():
    def __init__(self,Name:str,Caption:str) -> None:
        self.__name=Name
        self.__caption=Caption
    @property
    def name(self):
        return self.__name
    @property
    def caption(self):
        return self.__caption
class Group():
    def __init__(self) -> None:
        self.members:list[Family]=[]
        self.caption:str=''
        self.coordinator:Member
        self.name:str
class Family():
    def __init__(self) -> None:
        self.members:list[Member]
        self.familyCap:Member
class Member():
    def __init__(self) -> None:
        self.name:str
        self.sex:bool
        self.party:Party
        self.role:Role
class Party():
    def __init__(self) -> None:
        pass
class Role():
    def __init__(self) -> None:
        pass

if __name__ == '__main__':
    start_day=date(2024,8,12)
    caption='春キャンプ'
    name='2024春キャン'
    Spring=Shedule(start_day=start_day,caption=caption,name=name)