from duplicatesAndGapsInBarcodes import listDuplicateBarcodes, gap_List, readCSV, writeCSV
from os import path

#read CSV
filename = 'PREBarcodesBODATSASep2022.csv'
filepath = r'C:\NSCFTraining\PythonScripts'
fieldname = 'Barcode'
results = readCSV(path.join(filepath,filename), fieldname)

#determine duplicate barcodes
barcodesList = results
duplicates = listDuplicateBarcodes(barcodesList)

#write list of duplicates to CSV
list = duplicates
filepath = r'C:\NSCFTraining\PythonScripts'
fieldname = 'Duplicate Barcodes'
outFile = 'PREDuplicates.csv'
writeCSV(list, fieldname, path.join(filepath,outFile))
print("list of duplicate barcodes saved to file")

#determine gaps in barcodes
gaps = gap_List(barcodesList)

#write list of gaps to CSV
filepath = r'C:\NSCFTraining\PythonScripts'
list = gaps
fieldname = 'Gaps'
outFile = 'PREGaps.csv'
writeCSV(list, fieldname, path.join(filepath, outFile))
print("list of gaps saved to file")
