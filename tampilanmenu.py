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
            print("Anda memilih Parkir Masuk")
            # Tambahkan logika atau fungsi (codingan)
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

if __name__ == "__main__":
    main()