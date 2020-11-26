panjang1 = 1
panjang2 = 2
panjang3 = 3
panjang4 = 4

jumlah = panjang1 + panjang2 + \
    panjang3 + \
    panjang4

# print(jumlah)

paragraf = """Ini adalah paragraf. Paragraf
      terdiri dari beberapa baris."""

# print(paragraf)

x = y = z = "i love you"

a, b, c = 1, 3.4, "Umar"

# print c

# x = 5 
# print(x, "tipenya adalah ", type(x))
# x = 2.0
# print(x, "tipenya adalah ", type(x))
# x = 1+2j
# print(x, "tipenya adalah ",type(x))

# a = 1234567899999999999999999999
# print a

# b = 0.123456789123456789
# print b

# c = 1+4j
# print c

# kalimat = "Nama saya Umar"

# print(kalimat)      # print string lengkap
# print(kalimat[0])   # print karakter pertama
# print(kalimat[-1])  # print karakter terakhir
# print(kalimat[6:9]) # print dari indeks 4 - 6
# print(kalimat[:4])  # print dari indeks 0 - 3

# ============================

# list

# a = [5,10,15,20,25,30,35,40]

# # a[2] = 15
# print("a[2] = ", a[2])

# # a[0:3] = [5, 10, 15]
# print("a[0:3] = ", a[0:3])

# # a[5:] = [30, 35, 40]
# print("a[5:] = ", a[5:]) 
# ============================

# tuple 

# white = (255,255, 255)
# red = (255,0,0)
# print(white)
# print(red[0])
# print(red[1])

# akan menghasilkan error
# tuple bersifat
# =============================

# set

# set integer 
# my_set = {1,2,3} 
# print(my_set) 

# # set dengan menggunakan fungsi set() 
# my_set = set([1,2,3]) 
# print(my_set) 

# # set data campuran 
# my_set = {1, 2.0, "Python", (3,4,5)} 
# print(my_set) 

# # bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# # output: {1,2,3} 
# my_set = {1,2,2,3,3,3} 
# print(my_set) 

# # set tidak bisa berisi anggota list 
# # contoh berikut akan muncul error TypeError 
# my_set = {1,2,[3,4,5]} 

# =====================
# dictionary

d = {1:'satu', 2:'dua', 'tiga':3}
print(type(d))
print("d[1] = ", d[1])
print("d['tiga'] = ", d['tiga'])
# # Error
print("d[3] = ", d[3])