# PROJECT TOKO NOVEL SEDERHANA

# Class Novel
class Novel:
    def __init__(self, judul, penulis, harga, stok):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga
        self.stok = stok

    def tampilkan(self):
        print("Judul   :", self.judul)
        print("Penulis :", self.penulis)
        print("Harga   : Rp", self.harga)
        print("Stok    :", self.stok)
        print("------------------------")


# Class Toko
class TokoNovel:
    def __init__(self):
        self.daftar_novel = [
            Novel("Laskar Pelangi", "Andrea Hirata", 85000, 10),
            Novel("Dilan 1990", "Pidi Baiq", 75000, 8),
            Novel("Bumi", "Tere Liye", 95000, 5)
        ]

    def tampilkan_novel(self):
        print("\n=== DAFTAR NOVEL ===")
        for novel in self.daftar_novel:
            novel.tampilkan()

    def tambah_novel(self):
        print("\n=== TAMBAH NOVEL ===")
        judul = input("Judul novel: ")
        penulis = input("Nama penulis: ")
        harga = int(input("Harga novel: "))
        stok = int(input("Stok novel: "))

        novel = Novel(judul, penulis, harga, stok)
        self.daftar_novel.append(novel)

        print("Novel berhasil ditambahkan!")

    def beli_novel(self):
        self.tampilkan_novel()

        judul = input("Masukkan judul novel: ")

        for novel in self.daftar_novel:
            if novel.judul.lower() == judul.lower():

                jumlah = int(input("Jumlah beli: "))

                if jumlah > 0 and jumlah <= novel.stok:
                    total = novel.harga * jumlah
                    novel.stok -= jumlah

                    print("\n=== STRUK PEMBELIAN ===")
                    print("Novel :", novel.judul)
                    print("Jumlah:", jumlah)
                    print("Total : Rp", total)
                    print("Pembelian berhasil!")

                else:
                    print("Stok tidak mencukupi!")

                return

        print("Novel tidak ditemukan!")


# Program utama
toko = TokoNovel()

while True:
    print("\n===== TOKO NOVEL =====")
    print("1. Tampilkan Novel")
    print("2. Tambah Novel")
    print("3. Beli Novel")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        toko.tampilkan_novel()

    elif pilihan == "2":
        toko.tambah_novel()

    elif pilihan == "3":
        toko.beli_novel()

    elif pilihan == "4":
        print("Terima kasih telah berbelanja!")
        break

    else:
        print("Pilihan tidak tersedia!")