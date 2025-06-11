#Program Pemesanan Tiket Pesawat 
print("Selamat Datang di Bandara Minangkabau")
print("Kota tujuan yang tersedia: Medan, Jakarta, Batam")

kota_tujuan =  input ("Masukkan kota tujuan anda : ")

if kota_tujuan == "Medan":
    harga_sekali = 1002600
elif kota_tujuan == "Jakarta":
    harga_sekali = 2142900
elif kota_tujuan == "Batam":
    harga_sekali = 665400
else:
    print("Pilihan anda tidak tersedia")

jenis_tiket = input ("Apakah anda ingin tiket pulang pergi (PP) atau sekali jalan (Sekali)? ")

if jenis_tiket == "Sekali":
        total_harga = harga_sekali
        print ("Harga tiket untuk", {kota_tujuan}, "Sekali Jalan = Rp ", total_harga)
elif jenis_tiket == "PP":
        total_harga = harga_sekali * 2 * 0.8
        print ("Harga tiket untuk", {kota_tujuan}, "PP = Rp ", total_harga)
else:
        print("Pilihan anda tidak tersedia")



