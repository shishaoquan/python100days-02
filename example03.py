
row_number = int(input())
col_number = int(input())

for i in range(row_number):
    for j in range(col_number):
        print((i + 1) * (j + 1), end='\t')
    print()