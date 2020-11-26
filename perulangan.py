
# Program untuk menemukan jumlah bilangan dalam satu list

# List number
numbers = [7, 5, 9, 8, 4, 2, 6, 4, 1]

# variablel untuk menyimpan jumlah

sum = 0

# iterasi
for each in numbers:
    sum = sum + each

# Output: Jumlah semuanya: 46
print("Jumlah semuanya:", sum)

# range
# Output: range(0,10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(2,10))

# Output: [2, 3, 4, 5, 6, 7]
print(range(2,8))

# Output: [2, 5, 8, 11, 14, 17]
print(range(2, 20, 3))

# Program untuk iterasi list menggunakan pengindeksan

mapel = ['matematika', 'fisika', 'kimia']

# iterasi list menggunakan indeks
for i in range(len(mapel)):
    print("Saya suka", mapel[i])

count = -2
while (count < 5):
    print('The count is:', count)
    count = count + 1
print('Good bye!')

# contoh penggunaan statement break
for letter in [7, 5, 9, 8, 4, 2, 6, 4, 1]:
    if letter == 9:
        continue
    print("angka sekarang:", letter)
print("Good bye")

count = 5
while (count < 5):
    print(count, "kurang dari 5")
    count = count + 1
else:
    print(count, "tidak kurang dari 5")