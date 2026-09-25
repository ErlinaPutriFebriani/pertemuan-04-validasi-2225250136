# Program Validasi dan Klasifikasi Nilai Akhir
print("Validasi dan Klasifikasi Nilai Akhir")

# 1. Membaca masukan sebagai teks dan membersihkan spasi
teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

# 2. Validasi Tipe Data dengan try-except
try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")
else:
    # 3. Validasi Rentang (0 sampai 100)
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")
    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")
    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")
    else:
        # 4. Perhitungan Nilai Akhir (0.6 * ujian + 0.4 * tugas)
        akhir = 0.6 * ujian + 0.4 * tugas
        print(f"Nilai akhir = {akhir:.2f}")
        
        # 5. Pemeriksaan Syarat Kehadiran Minimal 80%
        if hadir < 80:
            print("Status: Tidak memenuhi syarat kehadiran.")
        else:
            # 6. Menentukan Predikat dengan Rantai If-Elif-Else Menurun
            if akhir >= 85:
                predikat = "A"
            elif akhir >= 70:
                predikat = "B"
            elif akhir >= 60:
                predikat = "C"
            elif akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"
            
            # 7. Menentukan Status Kelulusan (Lulus jika A, B, atau C)
            if predikat in ("A", "B", "C"):
                status = "Lulus"
            else:
                status = "Belum lulus"
            
            # 8. Menampilkan Hasil Akhir
            print(f"Predikat: {predikat}")
            print(f"Status: {status}")