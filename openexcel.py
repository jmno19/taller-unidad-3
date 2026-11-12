import openpyxl

wb = openpyxl.load_workbook('data1.xlsx')
sheet = wb['Data']

data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    data.append(row)

print(f"Total de registros leídos con openpyxl: {len(data)}")