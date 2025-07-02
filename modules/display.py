# modules/display.py

def banner():
    print("===================================================")
    print("☀️        PLTS Pro Calculator v1.0         ☀️")
    print("    Sebuah Kalkulator Terstruktur Modular    ")
    print("===================================================")

def menu_utama():
    print("\n[MENU UTAMA]")
    print("1. Hitung Kebutuhan PLTS (Beban dari Daftar Alat)")
    print("2. Hitung Kebutuhan PLTS (Beban Manual Wh)")
    print("3. Keluar")

def hasil(hasil_kalkulasi):
    """Menampilkan hasil kalkulasi dengan format yang rapi."""
    if not hasil_kalkulasi:
        print("\n⚠️  Gagal melakukan perhitungan. Periksa kembali input Anda.")
        return
        
    print("\n----------------- HASIL PERHITUNGAN -----------------")
    print("Berikut adalah estimasi kebutuhan sistem PLTS Anda:")
    
    print("\n[PANEL SURYA]")
    print(f"Kapasitas Total Panel Surya: {hasil_kalkulasi['panel_wp']} Wp")
    
    print("\n[BATERAI]")
    print(f"Kapasitas Total Baterai: {hasil_kalkulasi['baterai_ah']} Ah pada sistem {hasil_kalkulasi['tegangan_sistem']}V")
    print(f"   (Untuk otonomi selama {hasil_kalkulasi['hari_otonomi']} hari)")

    print("\n[SOLAR CHARGE CONTROLLER]")
    print(f"Ukuran Minimum SCC: {hasil_kalkulasi['scc_a']} A")
    print("   -> Pilih ukuran yang tersedia di pasaran di atas angka ini.")
    print("---------------------------------------------------\n")

def selamat_tinggal():
    print("\nTerima kasih telah menggunakan PLTS Pro Calculator!")