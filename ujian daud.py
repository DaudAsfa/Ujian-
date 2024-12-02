Nama = "Muhammad Daud Asfa"
Kelas = "1IA16"
NPM = "50424802"

print("Hallo! Saya Admin {Nama} Dari Kelas {Kelas} Dengan NPM {NPM}")

game = ["Genshin Impact, Honor of Kings, League of Legends, Honkai Impact, Mobile Legends"]

Genshin_Impact = 10000
Honor_of_Kings = 10000
League_of_Legends = 10000
Honkai_Impact = 10000
Mobile_Legends = 10000

def main():
    while: 
        print("""
             ================================================
                    Selamat Datang di Menu EzStoreKuy
             ================================================
                              Daftar Pilihan
            1. Daftar Game
            2. Top-Up
            3. Mencetak Bukti Transaksi
            4. Cek Stok
            5. Exit
            =================================================
            """)
        
    input_user = input("Masukkan Angka 1-5= ")

    if input_user == "1" :
        print("Berikut game yang tersedia = {game}")

    elif input_user == "2" :
        print("Berikut game yang tersedia = {game}")
        topup = input("Masukkan Game yang Anda Ingin Top-Up: ")
        if topup == "Genshin Impact":
            topup_genshin = input("Masukkan Nominalnya: ")
        
        elif topup == "Honor of Kings":
            topup_hok = input("Masukkan Nominalnya: ")

        elif topup == "League of Legends":
            topup_hok = input("Masukkan Nominalnya: ")

        elif topup == "Honkai Impact":
            topup_hi = input("Masukkan Nominalnya: ")

        elif topup == "Mobile Legends":
            topup_hok = input("Masukkan Nominalnya: ")

        else:
            print("Maaf, Kategori Tidak Ditemukan.")

     elif input_user == "3" :

     elif input_user == "4" :
            print("Game Apa Yang Ingin Anda Cek?: ")
