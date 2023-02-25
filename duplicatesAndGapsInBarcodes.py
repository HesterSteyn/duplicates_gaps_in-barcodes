import pandas as pd
import numpy as np
import re
import csv


# function to read csv as dataframe and create list of barcodes
def readCSV(filename, fieldname):
  try:
    data = pd.read_csv(filename)
    barcodes = np.array(data[fieldname])
    return barcodes
  except:
    print("file or fieldname invalid")


#function to create list of duplicate barcodes
def listDuplicateBarcodes(barcodesList):
  setOfElems = set()
  uniqueBarcodes = []
  duplicateBarcodes = []
  for elem in barcodesList:
      if elem in setOfElems:
          duplicateBarcodes.append(elem)
      else:
          setOfElems.add(elem) 
          uniqueBarcodes.append(elem)   
  print(len(duplicateBarcodes), "duplicate barcodes")
  return duplicateBarcodes


#function to create a list of gaps in unique barcodes
def gap_List(barcodesList):
    #Strip the non-numeric part of barcodes
    uniqueBarcodes = list(set(barcodesList))
    numericalsInBarcode = []
    for barcode in uniqueBarcodes:
        try:
            num = re.findall('(\d+)', barcode)[0]
            numericalsInBarcode.append(num)
            #numericalsInBarcode.append(int(barcode[3:10]))
        except:
            pass
    #Finding missing integers in list
    uniqueBarcodes = None
    gaps = []
    numericalsInBarcode.sort()
    fullList = range(numericalsInBarcode[0], numericalsInBarcode[-1]+1)
    numericalsInBarcode = set(numericalsInBarcode)
    for i in fullList:
        if i not in numericalsInBarcode:
            gaps.append(i)
    return gaps


#function to write duplicate barcodes/gaps to a .csv file
def writeCSV(list, fieldname, outFile):
  with open(outFile, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([fieldname])
    for name in list:
      writer.writerow([name])  




