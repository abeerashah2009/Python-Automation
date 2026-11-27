import openpyxl

workbook = openpyxl.load_workbook('sample.xlsx')
sheet = workbook.active

print(f'Sheet name: {sheet.title}')

cell_value = sheet['A1'].value
print(f'The value in cell A1 is: {cell_value}')

for row in sheet.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
    print(row)

sum_column_B = 0

for row in sheet.iter_rows(
    min_row=2,
    min_col=2,
    max_col=2,
    max_row=sheet.max_row,
    values_only=True
):
    sum_column_B += row[0]

print(f'The sum of values in column B is: {sum_column_B}')
