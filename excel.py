import openpyxl


def export_excel(linhas):
    wb = openpyxl.Workbook()
    ws = wb.active
    for linha in linhas:
        ws.append(linha)
    wb.save('./arquivosExcel/sample.xlsx')
