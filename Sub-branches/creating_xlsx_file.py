
import xlsxwriter
from time import sleep

# Create a workbook and add a worksheet.
name = str(input('Enter name for the xlsx file:'))
name = name+'.xlsx'
print(name)

workbook = xlsxwriter.Workbook(name)
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = ['Rent', 'Gas', 'Food', 'Gym']



# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item in expenses:
    worksheet.write(row, col, item)
    row += 1

sleep(1)
print('Items added')

sleep(0.5)

workbook.close()
print('workbook created')


