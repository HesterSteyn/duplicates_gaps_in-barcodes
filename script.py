from duplicateBarcodes import listDuplicateBarcodes, readCSV, writeCSV
from barcodesGaps import gap_List
from os import path

#read CSV
filename = 'PREBarcodesBODATSASep2022.csv'
filepath = r'C:\NSCFTraining\PythonScripts\Barcodes'
fieldname = 'Barcode'
results = readCSV(path.join(filepath,filename), fieldname)

#determine duplicate barcodes
barcodesList = results
duplicates = listDuplicateBarcodes(barcodesList)

#write list of duplicates to CSV
list = duplicates
filepath = r'C:\NSCFTraining\PythonScripts\Barcodes'
fieldname = 'Duplicate Barcodes'
outFile = 'PREDuplicates.csv'
writeCSV(list, fieldname, path.join(filepath,outFile))
print("list of duplicate barcodes saved to file")

#determine gaps in barcodes
gaps = gap_List(barcodesList)

#write list of gaps to CSV
filepath = r'C:\NSCFTraining\PythonScripts\Barcodes'
fieldname = 'Gaps'
outFile = 'PREGaps.csv'
writeCSV(gaps, fieldname, path.join(filepath, outFile))
print("list of gaps saved to file")
