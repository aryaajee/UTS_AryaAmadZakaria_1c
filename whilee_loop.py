# a =1 
# while a < 10:
#     print(f'Arya kaya-{a}')
#     a+=1

# for a in range (10):
#   if a == 7:
#     break
#   print(a)

# y = 1
# while y< 10:
#     if y % 2 == 1:
#          print(f'{y}- Bilangan Genap')
#     else:
#          print(f'{y}- Bilangan Ganjil') 
#     y+=1
 #cara berenti ctrl+c
# while True:
#     print('aja kaya kue')

# for q in range(7):
#     if q == 3:
#         break
#     print(q)


# for q in range(7):
#     if q == 3:
#         continue
#     print(q)


jumlah_siswa =int(input('masukan jumlah siswa:'))
total_nilai = 0
for a in range(jumlah_siswa):
     nilai =float(input(f'massukan nilai ujian siswa ke -{a + 1}:'))
    total_nilai+= nilai
    
if jumlah_siswa> 0:
     rata_rata = total_nilai / jumlah_siswa
     print(f'rata-rata nilai dari{jumlah_siswa}siswa adalah{rata_rata:.}')