from openpyxl import Workbook
print("Lendo dados do arquivo de texto")

# 1 - Importando Arquivo txt
file_txt = open('files/gastos.txt', 'r', encoding='utf-8')
file = file_txt.read()
# print(file)
list_data = file.splitlines()
# print(list_data)

# 2 - Interando os valores da lista
for i in range(0,len(list_data)):
    list_data[i] = list_data[i].split(',')
print(list_data)

# 3 - Criação da planilha
wb = Workbook()
ws = wb.active

for row in list_data:
    ws.append(row)
    
wb.save('files/gastos.xlsx')