class Produk:
    def __init__(self, id_produk, nama, manufacturer, tipe, tahun, harga, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.manufacturer = manufacturer
        self.tipe = tipe
        self.tahun = tahun
        self.harga = harga
        self.stok = stok

def tampilkan_produk(produk_list):
    if len(produk_list) == 0:
        print("Belum ada produk.")
    else:
        print("\nDaftar Produk:")
        print("ID | Nama | Manufacturer | Tipe | Tahun | Harga | Stok")
        print("-" * 60)
        for p in produk_list:
            print(p.info())
        print("-" * 60)

def tambah_produk(produk_list):
    print("\nTambah Produk")
    id_p = input("ID produk: ")
    for p in produk_list:
        if p.id_produk == id_p:
            print("ID sudah ada! Gagal tambah produk.")
            return
    nama = input("Nama produk: ")
    manuf = input("Manufacturer: ")
    tipe = input("Tipe: ")
    try:
        tahun = int(input("Tahun pembuatan: "))
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
    except ValueError:
        print("Tahun, harga, dan stok harus angka!")
        return
    produk_list.append(Produk(id_p, nama, manuf, tipe, tahun, harga, stok))
    print("Produk berhasil ditambah.")

def hapus_produk(produk_list):
    print("\nHapus Produk")
    id_p = input("Masukkan ID produk untuk dihapus: ")
    for i, p in enumerate(produk_list):
        if p.id_produk == id_p:
            konfirmasi = input(f"Yakin hapus {p.nama}? (y/n): ")
            if konfirmasi.lower() == 'y':
                produk_list.pop(i)
                print("Produk dihapus.")
            else:
                print("Batal hapus.")
            return
    print("Produk tidak ditemukan.")

def main():
    produk_list = [
        Produk("P001", "TV Samsung", "Samsung", "LED", 2020, 4500000, 10),
        Produk("P002", "Kulkas LG", "LG", "2 Pintu", 2019, 3500000, 5),
        Produk("P003", "Mesin Cuci Panasonic", "Panasonic", "Front Load", 2021, 4000000, 7),
        Produk("P004", "AC Daikin", "Daikin", "Split", 2022, 3000000, 8),
        Produk("P005", "Microwave Sharp", "Sharp", "700W", 2018, 1200000, 15)
    ]

    while True:
        print("\nMenu Produk") 
        print("1. Tampilkan Produk")
        print("2. Tambah Produk")
        print("3. Hapus Produk")
        print("4. Keluar")
        pilihan = input("Pilih (1-4): ")
        if pilihan == "1":
            tampilkan_produk(produk_list)
        elif pilihan == "2":
            tambah_produk(produk_list)
        elif pilihan == "3":
            hapus_produk(produk_list)
        elif pilihan == "4":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
