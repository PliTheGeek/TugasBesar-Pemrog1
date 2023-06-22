occupied = [ 23, 42, 1, 50, 4, 2, 6,20 ]
while True:
#=====================================================================================#
    def sistem_parkiran(pilih):
        
        if pilih == "1":
        
            while True:
                
                print(f"Parkiran ini ada 50 slot")
                print(f"Dan nomor tempat parkir yang terpakai di ")

                for i in occupied:
                    print (i, end=" - ")

                lokasi = int(input("Dimana kamu akan parkir : "))

                if lokasi > 50 :
                    print("Slot Parkir tidak lebih dari 50!, ")
                    print()

                elif lokasi not in occupied :
                    occupied.append(lokasi)
                    print("Ini Tiketnya")
                    break
                               
                else:
                    print("Tolong Masukan Lokasi yang lain...")
                    print()
#=====================================================================================#
        elif pilih == "2":
            
            for i in occupied:
                print (i,end=" - ")

            keluar_lokasi = int(input("Masukan Lokasi Parkir Mu Sebelumnya : "))
            occupied.remove(keluar_lokasi)

            jamMasuk = int(input("Masukan Jam awal masuk : "))
            jamKeluar = int(input("Jam Keluar : "))
            lamanya = jamKeluar - jamMasuk
            
            if lamanya == 1:
                print("gratis")
            elif lamanya >= 3:
                print(" Rp. 2000")
            elif lamanya >= 6:
                print(" Rp. 3000")
            elif lamanya >= 12:
                print(" Rp. 5000")
            else:
                print(" Rp. 10000")

        elif pilih == "3":
            for i in occupied:
                print (i, end=" - ")

#=========================================================================================#
    print("Selamat datang di Parkiran Motor! Silahkan pilih menu yang anda inginkan")
    print("1. Parkir Masuk")
    print("2. Keluar Parkir")
    print("3. Tampilkan Info Lokasi Parkir Yang Terpakai")
#=========================================================================================#

    pilih = input("Masukan Pilihanmu : ")
    sistem_parkiran(pilih)

    if pilih == "Matikan Daya":
            break
            print("--> TERIMAKASIH SUDAN MENGGUNAKAN PROGRAM INI <--")
    elif pilih in ["1", "2", "3"]:
        print()
    else:
        print("\nTolong Masukan Ulang\n")