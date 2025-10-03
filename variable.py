nama = "arya"
hobi = 'coding'
umur = 22
laki = True

print("===Biodata====")
print("nama: %s" % (nama))
print("hobi: %s, umur: %d, laki: %r" % (hobi, umur, laki))

# naming convention variable
pesan = "halo, selamat pagi"
nilai_ujian = 99.2

# assignment
nama = "ucogs"
umur = 22
nama = "ucogs franco"
umur = 21

# deklarasi beserta tipe data
nama: str = "ucogs"
hobi: str = "makan"
umur: int = 22
laki: bool = True
nilai_ujian: float = 99.2

# deklarasi banyak variable sebaris
nilai1, nilai2, nilai3, nilai4 = 22, 21, 33, 44
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4

print("rata-rata nilai: %f" % (nilai_rata_rata))