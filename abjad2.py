abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = int(input('Masukkan cipher text yang anda inginkan = '))
def encode(kalimat):
    kalimat = kalimat.lower()
    hasil_encode=''
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru =(index_lama + key) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_encode = hasil_encode + abjad_baru
        else:
            hasil_encode = hasil_encode +''
    return hasil_encode

kalimat = input('Masukkan kalimat yang ingin dienkripsi = ')
kalimat_hasil = encode(kalimat)
print('kalimat yang dimasukkan adalah ',kalimat)
print('Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key ',key,'adalah ',kalimat_hasil,)
