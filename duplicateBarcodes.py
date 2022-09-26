import pandas as pd
import numpy as np
import csv


# function to read csv as dataframe and create list of barcodes
def readCSV(filename, fieldname):
  try:
    data = pd.read_csv(filename)
    barcodes = np.array(data[fieldname])
    return barcodes
  except:
    "file or fieldname invalid"



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


#function to write duplicate barcodes/gaps to a .csv file
def writeCSV(list, fieldname, outFile):
  with open(outFile, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fieldname)
    for name in list:
      writer.writerow([name])  




