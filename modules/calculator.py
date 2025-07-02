# modules/calculator.py
import math

# Konstanta untuk perhitungan yang bisa disesuaikan
FAKTOR_LOSS_SISTEM = 1.3
DoD_BATERAI = 0.5 
FAKTOR_KEAMANAN_SCC = 1.25

def hitung_kebutuhan_plts(total_beban_wh, psh, hari_otonomi, tegangan_sistem):
    """
    Melakukan kalkulasi kebutuhan komponen PLTS berdasarkan input.
    Mengembalikan hasil dalam bentuk dictionary.
    """
    if psh <= 0 or tegangan_sistem <= 0:
        return None

    # Menghitung kapasitas Panel Surya (Wp)
    kapasitas_panel_wp = (total_beban_wh / psh) * FAKTOR_LOSS_SISTEM

    # Menghitung kapasitas Baterai (Ah)
    kapasitas_baterai_ah = (total_beban_wh * hari_otonomi) / (DoD_BATERAI * tegangan_sistem)

    # Menghitung ukuran Solar Charge Controller (A)
    ukuran_scc_a = (kapasitas_panel_wp / tegangan_sistem) * FAKTOR_KEAMANAN_SCC

    hasil = {
        "panel_wp": math.ceil(kapasitas_panel_wp),
        "baterai_ah": math.ceil(kapasitas_baterai_ah),
        "scc_a": math.ceil(ukuran_scc_a),
        "tegangan_sistem": int(tegangan_sistem),
        "hari_otonomi": int(hari_otonomi)
    }
    
    return hasil