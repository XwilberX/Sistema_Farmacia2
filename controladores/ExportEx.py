import xlsxwriter

workbook = xlsxwriter.Workbook('tables.xlsx')
worksheet = workbook.add_worksheet()

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]

row = '1'
header = ["A","B","C","D","E","F","G","H","I","J"]
header2 = ["A","B","C","D", "E"]

for x in range(len(header2)):
     a = str(header[x])

b = len(data) + 1

worksheet.add_table('A{0}:{1}{2}'.format(row, a, b), {'data': data,
                              'columns': [{'header': 'Product'},
                                          {'header': 'Quarter 1'},
                                          {'header': 'Quarter 2'},
                                          {'header': 'Quarter 3'},
                                          {'header': 'Quarter 4'},
                                          ]})
workbook.close()