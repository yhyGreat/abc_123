import xlrd



class people():
    def __init__(self, num=0, name="name", room=0, bed=0, next=0, recode=[], arecode=[]):
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


wb=xlrd.open_workbook("D:\\datap.xls")
wb.sheet_names()
sheet1=wb.sheet_by_index(0)
sheet1.nrows
sheet1.ncols
print(sheet1.row_values(0))

for row  in range(0,20):
    person[row].name=table.cell(row,1).value










