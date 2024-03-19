from string import Template
from datetime import time,date

cssPath='SheduleTemplate.css'
headder=Template('<head><link rel="stylesheet" type="text/css" href="$cssPath"/></head>')
#print(headder.substitute(cssPath=cssPath))
class CaptionColum():
    def __init__(self,name:str='',caption:str='',type='') -> None:
        self.__name=name
        self.__caption=caption
    @property
    def name(self):
        return self.__name
    @property
    def caption(self):
        return self.__caption
class DayEvent():
    """1日単位のイベントの集合
    """
    def __init__(self,caption_column_list:list[CaptionColum]) -> None:
        self.__events:list[Event]=[]
        self.__day_count:int=1
    @property
    def events(self):
        return self.__events
    @property
    def day_count(self):
        return len(self.__events)
    def add_new_event(self):
        new_event=Event()
        self.__events.append(new_event)
        return new_event
class Shedule():
    """生成するためのスケジュール本体
    """
    def __init__(self,start_day:date,name:str='',caption:str='') -> None:
        """スケジュールインスタンス

        Args:
            start_day (date): 予定開始日
            name (str, optional): スケジュールの名前. Defaults to ''.
            caption (str, optional): スケジュールの説明. Defaults to ''.
        """
        self.__days:list[DayEvent]=[]
        self.__start_day=start_day
        self.__name:str=name
        self.__caption:str=caption
        self.__caption_column:list[CaptionColum]
    @property
    def days(self):
        """DayEventリスト

        Returns:
            _type_: DayEventリスト
        """
        return self.__days
    @property
    def start_day(self):
        return self.__start_day
    @property
    def name(self):
        return self.__name
    @property
    def caption(self):
        return self.__caption
    @property
    def caption_column(self):
        return self.__caption_column
    def add_new_day_event(self):
        """新規DayEventを追加する

        Returns:
            _type_: 追加したDayEvent
        """
        dayevent=DayEvent(self.__caption_column)
        self.__days.append(dayevent)
        return dayevent
    def add_new_caption_column(self,name:str='',caption=''):
        capotion_column=CaptionColum(name=name,caption=caption)
        self.__caption_column.append(capotion_column)
        return capotion_column
    def get_days(self):
        return len(self.__days)

class Event():
    def __init__(self) -> None:
        self.__start_time:time
        self.__end_time:time
        self.__exe_time:time
        self.__caption:list[str]=[]
        self.__move_time:time
        self.name:str
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