import datetime
from dayToDiena import latviskotDienu

diena = int(input("Ievadi datumu!"))
menesis = int(input("Ievadi mēnesi!"))
gads = int(input("Ievadi gadu!"))

datums = datetime.date(gads, menesis, diena)
dienasNos = datums.strftime("%A")
dienaLv = latviskotDienu(dienasNos)
print(dienaLv)