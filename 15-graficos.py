from openpyxl import Workbook
from openpyxl.chart import(
    AreaChart,
    Reference,
    Series
)

wb = Workbook()
ws = wb.active

rows = [
    ['Ano', 'Lucro', 'Custos'],
    [2017, 40, 30],
    [2018, 35, 25],
    [2019, 30, 20],
    [2020, 10, 5],
    [2021, 15, 10],
    [2022, 25, 15]
]

for row in rows:
    ws.append(row)
    
chart = AreaChart()
chart.title = 'Lucros x Custos'
chart.style = 13
chart.x_axis.title = "Ano"
chart.y_axis.title = "Porcentagem"

categorias = Reference(
    ws,
    min_col=1,
    min_row=1,
    max_row=7
)
dados = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_col=3,
    max_row=7
)

chart.add_data(dados, titles_from_data=False)
chart.set_categories(categorias)
ws.add_chart(chart, "A10")
wb.save('files/chart.xlsx')