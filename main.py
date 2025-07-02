# main.py
from modules import calculator, display, input_handler

def main():
    display.banner()
    
    while True:
        display.menu_utama()
        choice = input_handler.get_menu_choice(max_choice=3)
        
        total_beban_wh = 0
        
        if choice == 1:
            total_beban_wh = input_handler.hitung_beban_dari_daftar()
        elif choice == 2:
            total_beban_wh = input_handler.get_float_input("\nMasukkan total kebutuhan energi harian Anda (Watt-hour/Wh): ")
        elif choice == 3:
            break # Keluar dari loop while
            
        if total_beban_wh > 0:
            # Jika ada beban yang dihitung, minta parameter sistem
            psh, hari_otonomi, tegangan_sistem = input_handler.get_sistem_parameter()
            
            # Lakukan perhitungan
            hasil_akhir = calculator.hitung_kebutuhan_plts(total_beban_wh, psh, hari_otonomi, tegangan_sistem)
            
            # Tampilkan hasil
            display.hasil(hasil_akhir)
            
        input("Tekan Enter untuk kembali ke menu utama...")

    display.selamat_tinggal()


if __name__ == "__main__":
    main()