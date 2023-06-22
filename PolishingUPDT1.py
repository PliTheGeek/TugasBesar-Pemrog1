while True:
# Sistem Utama
    print("Selamat datang di Parkiran Motor! Silahkan pilih menu yang anda inginkan")
    print("1. Parkir Masuk")
    print("2. Cek Kapasitas Parkir yang Tersedia")



#<><><><><><><><><><>#
    def main():
#======================================================================================#
        while True:

            tampilkan_menu()
            pilihan = input("Masukkan pilihan menu yang anda inginkan (1/2/3): ")
            
            if pilihan == "1":
                parkir_masuk(pilihan)

            elif pilihan == "2":
                hitung_biaya_parkir(pilihan)
            
            elif pilihan == "123":
                shutdown(pilihan)
                
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
#================================================================================#


# Bagian Dhafin 
#=================================================================================#
            array = [23,42,1,50,4,2,6]
            def cek_kapasitas_parkir():
                while True:

                    for i in array: 
                        print (i, end=" ")

                    lokasi = int(input(" ==> Dimana kamu akan parkir : "))
            
                    if lokasi > 50 :
                        print("Kapasitas  Parkir tidak lebih dari 50!, ")
                        print()

                    elif lokasi in array :
                        print("Tolong Masukan Lokasi yang lain...")
                        print()
                
                    else:
                        array.append(lokasi)
                        terpakai = array[:]
                        print("Silahkan Ambil Tiket Parkir")
                        break
        
                    print(array)        
                    print("Terimakasih Selamat jalan\n")
#====================================================================================#
            def parkir_masuk(pilihan):
                print("Menu Masuk parkir ")
                print(f"Parkiran ini tersedia 50 kapasitas ")
                print(f"Dan nomor tempat parkir yang terpakai di : \n")

                cek_kapasitas_parkir()
#============================================================================#

# # Bagian Maria
#============================================================================#
# # Bagian Agil
def shutdown(pilihan):
    while True:
        Pass = int(input("Masukan Password: "))
        if (Pass) == 625789 :
            print("Berhasil")
            break
        else:
            print("Ulangi")

    main()







    