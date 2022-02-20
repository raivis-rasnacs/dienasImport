import datetime
import dayToDiena

diena = int(input("Ievadi datumu!"))
menesis = int(input("Ievadi mēnesi!"))
gads = int(input("Ievadi gadu!"))

datums = datetime.date(gads, menesis, diena)
dienasNos = datums.strftime("%A")
dienaLv = dayToDiena.latviskotDienu(dienasNos)
print(dienaLv)