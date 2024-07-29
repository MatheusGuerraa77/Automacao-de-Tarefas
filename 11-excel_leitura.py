from openpyxl import load_workbook

# 1 - Lendo Workbook e buscando planilhas
wb = load_workbook(filename='files/test.xlsx')
planilha1 = (wb['Planilha1'])

# 2 - Acessando um determinado valor
# print(planilha1['B2'].value)

# 3 - Interando valores por meio de loop
for i in range(2, 5):
    # print(f'{planilha1['A{i}'].value}')
    ano = planilha1['A%s' %i].value
    lucro = planilha1['B%s' %i].value
    custo = planilha1['C%s' %i].value
    print("{0} teve {1} de lucro e {2} de custo".format(ano, lucro, custo))