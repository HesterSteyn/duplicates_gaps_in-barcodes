import csv


#function to create a list of gaps in unique barcodes
def gap_List(barcodesList):
    #Strip the non-numeric part of barcodes
    uniqueBarcodes = list(set(barcodesList))
    numericalsInBarcode = []
    for barcode in uniqueBarcodes:
        try:
            numericalsInBarcode.append(int(barcode[3:10]))
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


    


