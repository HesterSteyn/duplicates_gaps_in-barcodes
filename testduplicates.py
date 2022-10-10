from duplicatesAndGapsInBarcodes import listDuplicateBarcodes

list = ['PRE0123456-0', 'PRE0123459-0', 'PRE0123456-0', 'PRE0123460-0', 'PRE0123463-0']

try:
    duplicates = listDuplicateBarcodes(list)
    print(duplicates)
except Exception as e:
    print(e)