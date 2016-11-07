table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table():
   col_widths = [0] * len(table_data) 
   for i in range(len(table_data)):
        for y in range(len(table_data[i])):
            if col_widths[i] < len(table_data[i][y]):
                col_widths[i] = len(table_data[i][y])

   largest_col = 0
   for i in range(len(col_widths)):
        if largest_col < col_widths[i]:
            largest_col = col_widths[i]

   for i in range(len(table_data[i])):
       for y in range(len(table_data)):
           print(table_data[y][i].rjust(largest_col), end='')
       print()

print_table()
print()
