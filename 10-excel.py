from openpyxl import Workbook

# 1 - Criando o workbook
wb = Workbook()
name = 'files/test.xlsx'

# 2 - Utilizando Worksheet
ws1 = wb.active
ws1.title =  'Planilha1'

# 3 - adicionando os dados
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2021, '25%', '40%'],
    [2022, '45%', '50%'],
    [2023, '15%', '10%']
]

for line in data:
    ws1.append(line)
    
    
ws2 = wb.create_sheet(title='Pi')
ws2['D2'] = 3.14

wb.save(filename=name)
