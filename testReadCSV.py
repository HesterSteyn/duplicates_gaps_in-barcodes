from duplicatesAndGapsInBarcodes import readCSV
from os import path

file = r'NHBarcodes.CSV'
filepath = r'C:\NSCF\barcodes'
filename = path.join(filepath, file)
fieldname = 'BARCODES'

result = readCSV(filename, fieldname)

i = 0


