angka = []
for i in range(5) :
    x = int(input('Masukan Bilangan : '))
    angka.append(x)
print('Angka sebelum diurutkan :',angka)
list.sort(angka)
print('Angka setelah diurutkan :',angka)
