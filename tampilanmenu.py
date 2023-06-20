# Sistem Utama
def tampilkan_menu():
    print("Selamat datang di Parkiran Motor! Silahkan pilih menu yang anda inginkan")
    print("1. Parkir Masuk")
    print("2. Cek Kapasitas Parkir yang Tersedia")
    print("3. Parkir Keluar")
    print("4. Keluar dari Program")

def main():
    
    while True:

        tampilkan_menu()
        pilihan = input("Masukkan pilihan menu yang anda inginkan (1/2/3/4): ")
        
        if pilihan == "1":
            
            parkir_masuk(pilihan)



        elif pilihan == "2":
            print("Anda memilih Cek Kapasitas Parkir")
            # Tambahkan logika atau fungsi (codingan)
        
        elif pilihan == "3":
            print("Anda memilih Parkir Keluar")
            # Tambahkan logika atau fungsi (codingan)
        
        elif pilihan == "4":
            print("Anda memilih Keluar dari Program")
            
            break
        
        else:

            print("Pilihan tidak valid. Silakan pilih kembali.")

# Bagian Dhafin 

def cek_kapasitas_parkir():


    array = [23,42,1,50,4,2,6]
    
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

# Bagian Dhafin

def parkir_masuk(pilihan):

            print("Menu Masuk parkir ")
    
           
            
            print(f"Parkiran ini tersedia 50 kapasitas ")
            print(f"Dan nomor tempat parkir yang terpakai di : \n")

            
            cek_kapasitas_parkir()

















# # Bagian Maria
# def parkir_keluar(parkiran):












# # Bagian Agil
# def parkir_keluar_program(parkiran):






if __name__ == "__main__":
    main()