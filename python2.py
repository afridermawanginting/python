result = ''
message = ''
choice = ''

while choice != 0:
    choice = input("\nApakah anda mau Enkripsi dan Dekripsi pesan?\
    \nMasukkan 1 untuk Enkripsi, 2 untuk Dekripsi dan 0 untuk Keluar.\
    \nPilihan ");
    if choice == '1':
        message=input("\nMasukkan Pesan untuk Enkripsi ")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)
        print(result + '\n\n')
        result = ''
    elif choice == '2':
        message = input("\nMasukkan Pesan Dekripsi ")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)
        print(result + '\n\n')
        result=''
    elif choice == '0':
        print("Inputan Invalid! \n\n")

