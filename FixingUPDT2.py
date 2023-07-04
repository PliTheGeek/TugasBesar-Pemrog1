print("\n")

occupied = []
while True:
#=====================================================================================#
    def sistem_parkiran(pilih):
        if pilih == "1":
        
            while True:
                
                print(f"\nParkiran ini ada 50 slot")
                print(f"Dan nomor tempat parkir yang terpakai di ")

                for i in occupied:
                    print (i, end=" - ",)

                lokasi = int(input("\nDimana kamu akan parkir : "))

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
            while True:
            
                for i in occupied:
                    print(f"Ini List Nya | {i}",end=" - ")
                keluar_lokasi = int(input("\nMasukan Lokasi Parkir Mu Sebelumnya : ", end=""))

                if keluar_lokasi not in (occupied):
                    print("Tolong Masukan Ulang")


                else:
                    occupied.remove(keluar_lokasi)

                    LamaJam = int(input("Berapa lama parkir : "))

                    if LamaJam == 1:
                        print("gratis")
                    elif LamaJam >= 2:
                        print(" Rp. 2000")
                    elif LamaJam >= 6:
                        print(" Rp. 3000")
                    elif LamaJam >= 12:
                        print(" Rp. 5000")
                    else:
                        print(" Rp. 10000")
                    break

        elif pilih == "3":
            print("\nIni List Nya:")
            for i in occupied:
                print (i,end=" - ")
            print()
                

#=========================================================================================#
    print("Selamat datang di Parkiran Motor! Silahkan pilih menu yang anda inginkan")
    print("1. Parkir Masuk")
    print("2. Keluar Parkir")
    print("3. Tampilkan Info Lokasi Parkir Yang Terpakai")
#=========================================================================================#

    pilih = input("Masukan Pilihanmu : ")
    sistem_parkiran(pilih)

    if pilih == "Keluar Proggram":
            break
            print("--> TERIMAKASIH SUDAN MENGGUNAKAN PROGRAM INI <--")
    elif pilih in ["1", "2", "3"]:
        print()
    else:
        print("\nTolong Masukan Ulang\n")