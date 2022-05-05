import xlrd

# Open the Workbook
workbook = xlrd.open_workbook("your_file_name.xlsx")

# Open the sheet
worksheet = workbook.sheet_by_index(0)

# Iterate rows
for i in range(0, 5):       #rows
    for j in range(0, 3):   #columns
        # Print values 
        print(worksheet.cell_value(i, j), end='\t')
    print('')
