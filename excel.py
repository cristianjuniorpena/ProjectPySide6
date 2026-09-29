import openpyxl
wb = openpyxl.Workbook()

ws = wb.active

def exportar_excel(list):
    for i in list:
        ws.append(i)
    wb.save('sample.xlsl')

