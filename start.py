import xlrd
import sys



class people():
    def __init__(self, num=0, name="abc", room=0, bed=0, next=0, recode=[], arecode=[]):
        self.num = num
        self.name = name
        self.room = room
        self. bed =  bed
        self.recode=[]
        self.arecode=[]
        self.next = next

person=[]
for i in range(1,20):
    person.append('people()')


data=xlrd.open_workbook("D:\\datap.xls")


page = len(data.sheets())                             #获取sheet的数量
table = data.sheets()[0]                                #打开第一张表
nrows = table.nrows                                     #获取总行数
ncols = table.ncols                                       #获取总列数

for i in range(nrows):                                     #循环打印每行的数据
  print(table.row_values(i))

#a=table.cell(1,0)
a=table.cell_value(1,0)
print(a)

person[0].room=124






