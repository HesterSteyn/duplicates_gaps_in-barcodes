import pandas as pd
import numpy as np
import csv
from collections import Counter


# dataframe
data = pd.read_csv("PREBarcodesBODATSASep2022.csv")
print(data[:5])

#Initialize array  
barcode = np.array(data['Barcode'])
#print(barcode)

#create list of duplicate barcodes
setOfElems = set()
uniquebarcodes = []
duplicates = []
for elem in barcode:
    if elem in setOfElems:
        duplicates.append(elem)
    else:
        setOfElems.add(elem) 
        uniquebarcodes.append(elem)   
print("Duplicate barcodes:", "\n", duplicates) 
print(len(duplicates))

#write duplicate barcodes to a csv file
def writeCSV(list, outFile):
  with open(outFile, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    fieldnames = ['DuplicateBarcodes']
    writer.writerow(fieldnames)
    for name in list:
      writer.writerow([name])  
  print("saved to file")


writeCSV(duplicates, 'PREDuplicates.csv')

print("Slice numeric part of barcode")
slice_barcode = []
for i in range(len(uniquebarcodes)):
    try:
        slice_barcode.append(int(uniquebarcodes[i][3:10]))
    except:
        pass
#print(slice_barcode[0:200])    

#!!!Missing elements from the list(not working - return 44 million records)
# res = []
# for m,n in zip(slice_barcode,slice_barcode[1:]):
#     if n - m > 1:
#         for i in range(m+1,n):
#             res.append(i)
# print("Missing elements from the list :", "\n" , res[0:200])
# print(len(res))

#!!!Does not work - nothing happens...
# missing_element = []
# for i in range(slice_barcode[0], slice_barcode[-1]+1):
#     if i not in slice_barcode:
#         missing_element.append(i)
        
# print(missing_element)

print("Get list of missing values:")
missing_values = set(range(slice_barcode[0], slice_barcode[-1]+1)) - set(slice_barcode)
missingbarcodes = list(missing_values)
print(missingbarcodes[0:200])
print(len(missingbarcodes))

# !!!Does not work  - error message: "cannot import name 'map' from 'itertools' (unknown location)"
# from itertools import map, chain
# from operator import sub
# print (list(chain.from_iterable((slice_barcode[i] + d for d in xrange(1, diff))
#     for i, diff in enumerate(map(sub, slice_barcode[1:], slice_barcode))
#         if diff > 1)))






