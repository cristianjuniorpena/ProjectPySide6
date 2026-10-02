import openpyxl
wb = openpyxl.Workbook()

ws = wb.active

def export_excel(list):
    for i in list:
        ws.append(i)
    wb.save('./arquivosExcel/sample.xlsl')

