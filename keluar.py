def hitung_biaya_parkir(jam_masuk, jam_keluar):
    biaya_parkir = 0
    durasi_jam = jam_keluar - jam_masuk

    if durasi_jam <= 2:
        biaya_parkir = 2000
    else:
        biaya_parkir = 2000 + (durasi_jam - 2) * 2000

    return biaya_parkir

jam_masuk = int(input("Masukkan jam masuk (0-23): "))
jam_keluar = int(input("Masukkan jam keluar (0-23): "))

biaya = hitung_biaya_parkir(jam_masuk, jam_keluar)


print("Biaya parkir: Rp", biaya)

