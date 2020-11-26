# set integer 
# my_set = {1,2,3} 
# print(my_set) 

# set dengan menggunakan fungsi set() 
# my_set = set([1,2,3]) 
# print(my_set) 

# set data campuran 
# my_set = {1, 2.0, "Python", (3,4,5)} 
# print(my_set) 

# Membuat set A and B 
A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8} 

# Gabungan menggunakan operator | 
# output: {1, 2, 3, 4, 5, 6, 7, 8} 
print(A | B) 

# Menggunakan fungsi union() 
# output: {1, 2, 3, 4, 5, 6, 7, 8} 
A.union(B) 

# output: {1, 2, 3, 4, 5, 6, 7, 8} 
B.union(A) 

# Membuat set A and B 
A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8} 

# Irisan menggunakan operator & 
# output: {4,5} 
print(A & B) 
# Menggunakan fungsi intersection() 
# output: {4,5} 
A.intersection(B) 

# output: {4,5} 
B.intersection(A) 

# membuat A and B 
A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8} 

# Menggunakan operator - pada A 
# Output: {1, 2, 3} 
print(A - B) 

# Output: {1, 2, 3} 
A.difference(B) 

# Menggunakan operator - pada B 
# Output: {8, 6, 7} 
print(B - A) 