import openpyxl

def export_to_excel(linhas, path):
    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        for linha in linhas:
            ws.append(linha)
        wb.save(f'{path}.xlsx')
        return (True, 'arquivo .xlsx criado com sucesso')
    except Exception as error:
        return (False, f'erro ao criar o arquivo xlsx: {error}')