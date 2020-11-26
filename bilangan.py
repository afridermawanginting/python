a = int(2.5)
2
b = int(3.8)
3
c = float(5)
5.0

print c

import decimal

#output: 0.1
print(0.2)

#output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.2))

string = 'aku bisa membuatmu jatuh cinta kepadaku'

print len(string)

my_list = ["I", "love","python","programming",2017]
# output: I
# print my_list[4]

#output: python
my_list[2]

# list dalam list
your_list = ["hello", [1,2,3], "python"]

# output 1
print(your_list[1][0])

# output 3
print(your_list[1][2])

# IndexError
# my_list[4]

# misal ada nilai yang salah
ganjil = [1,3,4,7,9]

# ubah item ke 3 (indeks ke 2)
ganjil[2] = 5
print(ganjil)

ganjil[2:3] = [11,13,15]
print(ganjil)