from xlrd import *
import os as o
from tkinter import *

class logcheck():

    def verify(self,x,y):
        
        self.y=y
        
        self.x=x+'.xlsx'
        self.p=open_workbook(self.x)
        self.s=self.p.sheet_by_index(0)
        self.__v=self.s.cell_value(0,1)
        
        if self.__v == self.y:
            return True
        
        else :
        
            return False

'''COMMENT, this is.''' 
