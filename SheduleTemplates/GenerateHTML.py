from string import Template
from datetime import time,date
from Shedule import Shedule


headder=Template('<head><link rel="stylesheet" type="text/css" href="$cssPath"/></head>')
#print(headder.substitute(cssPath=cssPath))

class GenerateSheduleHTML():
    def __init__(self,shedule:Shedule,file_path:str='test.html',css_path:str='Template.css') -> None:
        self.__headder=Template('<head><link rel="stylesheet" type="text/css" href="$css_path"/></head>')
        self.__file_path=file_path
        self.__css_path=css_path
        self.__shedule=shedule
    @property
    def file_path(self):
        return self.__file_path
    @property
    def css_path(self):
        return self.__css_path
    @property
    def shedule(self):
        return self.__shedule
    def __GetCaption(self):
        caption=self.shedule.caption
        t=Template('<caption>$caption</caption>')
        return t.substitute(caption=caption)
    def __GetTable(self):
        caption=self.__GetCaption()
        t=Template('<table class="class">$caption</table>')
        return t.substitute(caption=caption)
    def Generate(self):
        table=self.__GetTable()
        headder=self.__headder
        result=Template('$headder$table').substitute(headder=headder,table=table)
        with open(self.__file_path,mode='w')as file:
            file.write(result)

if __name__ == '__main__':
    start_day=date(2024,8,12)
    caption='aaaaaaaaaaaa'
    name='bbbbbbbb'
    css_path='SheduleTemplate.css'
    file_path='SheduleTemplate.html'
    she=Shedule(start_day=start_day,name=name,caption=caption)
    g=GenerateSheduleHTML(shedule=she,file_path=file_path,css_path=css_path)
    g.Generate()