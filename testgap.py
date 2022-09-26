from barcodesGaps import gap_List

uniquebarcodes = ['PRE0123456-0', 'PRE0123459-0', 'PRE0123460-0', 'PRE0123463-0']

try:
    gaps = gap_List(uniquebarcodes)
    print(gaps)
except Exception as e:
    print(e)