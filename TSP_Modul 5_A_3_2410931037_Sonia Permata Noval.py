#program toko buku lsik
class Buku:
    def __init__(self, nama, harga, warna, stok):
        self.nama = nama
        self.harga = harga
        self.warna = warna
        self.stok = stok

    def __str__(self):
        return f"{self.nama}, Harga: {self.harga}, Warna Sampul: {self.warna}, Stok: {self.stok}"


class TokoBuku:
    def __init__(self):
        self.daftar_buku = [
            Buku("Novel", 75000, "Putih", 10),
            Buku("Pendidikan", 50000, "Putih", 15),
            Buku("Biografi", 35000, "Kuning", 20)
        ]

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Daftar buku kosong.")
            return
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            print(buku)

    def tambah_buku(self, nama, harga, warna, stok):
        buku_baru = Buku(nama, harga, warna, stok)
        self.daftar_buku.append(buku_baru)
        print(f"{nama} telah ditambahkan ke daftar buku.")

    def hapus_buku(self, nama):
        for buku in self.daftar_buku:
            if buku.nama.lower() == nama.lower():
                self.daftar_buku.remove(buku)
                print(f"{nama} telah dihapus dari daftar buku.")
                return
        print(f"{nama} tidak ditemukan dalam daftar buku.")

    def cari_buku(self, pencarian):
        ditemukan_buku = [
            buku for buku in self.daftar_buku
            if pencarian.lower() in buku.nama.lower() or pencarian.lower() in buku.warna.lower()
        ]
        
        if ditemukan_buku:
            print("Buku yang ditemukan:")
            for buku in ditemukan_buku:
                print(buku)
        else:
            print("Tidak ada buku yang ditemukan.")


def main():
    toko = TokoBuku()

    while True:
        print("\nMenu Toko Buku:")
        print("1. Tampilkan daftar buku")
        print("2. Tambah buku baru")
        print("3. Hapus buku")
        print("4. Cari buku (berdasarkan jenis atau warna)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            toko.tampilkan_buku()
        elif pilihan == "2":
            nama = input("Masukkan nama buku: ")
            try:
                harga = int(input("Masukkan harga buku: "))
                stok = int(input("Masukkan stok buku: "))
            except ValueError:
                print("Harga dan stok harus berupa angka.")
                continue
            warna = input("Masukkan warna buku: ")
            toko.tambah_buku(nama, harga, warna, stok)
        elif pilihan == "3":
            nama = input("Masukkan nama buku yang ingin dihapus: ")
            toko.hapus_buku(nama)
        elif pilihan == "4":
            kata_kunci = input("Masukkan jenis atau warna buku yang dicari: ")
            toko.cari_buku(kata_kunci)
        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
