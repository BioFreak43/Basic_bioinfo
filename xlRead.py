import xlrd
import xlwt
psm = {}
book = xlrd.open_workbook('Table1.xlsx')
sh = book.sheet_by_index(0)
for row_index in range(1, sh.nrows):
    psm [(sh.cell_value(rowx=row_index, colx=0))] = \
    int(sh.cell_value(rowx=row_index, colx = 6))
unique_list = xlrd.open_workbook('Table3.xlsx')
unique = {}
j = 1
sh = unique_list.sheet_by_index(0)
for row_index in range(1, sh.nrows):
    unique [sh.cell_value(rowx = row_index, colx = 0)] = \
    sh.cell_value(rowx = row_index, colx = 1)

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet1')
ws.write(0, 0, 'Uniprot Accession')
ws.write(0, 1, 'Protein Name')
ws.write(0, 2, 'PSM')
i = 1
for x in psm:
    for y in unique:
        if x == y:
            ws.write(i, 0, x)
            ws.write(i, 2, psm.get(x))
            ws.write(i, 1, unique.get(y))
    i+=1
wb.save('Protein.xls')
