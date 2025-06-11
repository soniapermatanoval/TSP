print("Menentukan Biaya Parkir Motor Dan Mobil")
print("======================================================================")

nim = input("NIM :")

print("Biaya parkir motor dan mobil")
biaya_motor = (2*25000-3*16000)/(5*2-3*3)
biaya_mobil = (16000-3*biaya_motor)/2 

print(f"Biaya parkir untuk 1 motor = Rp{biaya_motor}")
print(f"Biaya parkir untuk 1 mobil = Rp{biaya_mobil}")

print("=======================================================================")

print("Biaya Parkir Motor Dan Mobil Berdasarkan 4 Angka Terakhir NIM")
banyak_motor = (int(nim[6:8]))
banyak_mobil = (int(nim[8:]))

total_parkir_motor = biaya_motor * banyak_motor
total_parkir_mobil = banyak_mobil * biaya_mobil
total_keseluruhan = total_parkir_mobil+total_parkir_motor

print("Jadi biaya parkir yang harus dikeluarkan yaitu:")
print("Biaya motor = Rp", total_parkir_motor)
print("Biaya mobil = Rp", total_parkir_mobil)
print("Total biaya parkir keseluruhan = Rp", total_keseluruhan)
print("=======================================================================")