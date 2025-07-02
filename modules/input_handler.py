# modules/input_handler.py
import json

def get_float_input(prompt: str) -> float:
    """Meminta input angka dari pengguna dengan validasi."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("⚠️  Error: Masukkan harus angka positif lebih dari nol.")
        except ValueError:
            print("⚠️  Error: Input tidak valid. Harap masukkan angka.")

def get_menu_choice(max_choice: int) -> int:
    """Menampilkan menu dan meminta pilihan pengguna."""
    while True:
        try:
            choice = int(input(">> Pilihan Anda: "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"⚠️  Pilihan tidak valid. Harap masukkan angka antara 1 dan {max_choice}.")
        except ValueError:
            print("⚠️  Input tidak valid. Harap masukkan angka.")

def hitung_beban_dari_daftar():
    """Menghitung total beban Wh berdasarkan pilihan peralatan dari file JSON."""
    try:
        with open('data/appliance_wattage.json', 'r') as f:
            appliances = json.load(f)
    except FileNotFoundError:
        print("Error: File 'data/appliance_wattage.json' tidak ditemukan.")
        return 0

    total_wh = 0
    print("\n--- Pilih Peralatan dari Daftar ---")
    
    while True:
        for i, alat in enumerate(appliances):
            print(f"  {i+1}. {alat['nama']} ({alat['watt']} Watt)")
        
        print("\nKetik nomor alat untuk menambah, atau ketik 's' untuk selesai.")
        choice = input(">> Masukkan nomor alat: ")

        if choice.lower() == 's':
            break
        
        try:
            alat_idx = int(choice) - 1
            if 0 <= alat_idx < len(appliances):
                jam_pakai = get_float_input(f"   Berapa jam pemakaian untuk '{appliances[alat_idx]['nama']}' per hari? ")
                beban_alat = appliances[alat_idx]['watt'] * jam_pakai
                total_wh += beban_alat
                print(f"   -> Beban ditambahkan: {beban_alat:.2f} Wh. Total sekarang: {total_wh:.2f} Wh\n")
            else:
                print("⚠️  Nomor alat tidak valid.")
        except ValueError:
            print("⚠️  Input tidak valid. Harap masukkan nomor.")
            
    return total_wh

def get_sistem_parameter():
    """Meminta parameter sistem PLTS dari pengguna."""
    print("\n--- Masukkan Parameter Sistem PLTS ---")
    psh = get_float_input("1. Perkiraan Peak Sun Hour (PSH) di lokasi Anda (jam)? ")
    hari_otonomi = get_float_input("2. Berapa hari otonomi baterai yang diinginkan? ")
    tegangan_sistem = get_float_input("3. Tegangan sistem yang akan digunakan (12, 24, atau 48 V)? ")
    
    return psh, hari_otonomi, tegangan_sistem