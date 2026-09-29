# Membuat program array 1 dimensi untuk data nilai mahasiswa
# Tugas pertemuan  (Project 1)

nama_mahasiswa = []
nilai_mahasiswa = []
nilai_maks = 10

while True:

    # Menampilkan menu program
    print("\n=== MENU DATA NILAI MAHASISWA ===")
    print("1. Input Data")
    print("2. Tampilkan Data")
    print("3. Nilai Tertinggi & Terendah")
    print("4. Rata-rata")
    print("5. Ubah Data")
    print("6. Hapus Data")
    print("7. Keluar")

    select = input("Pilih menu : ")
    # logika untuk menu 1 
    if select == "1":
        if len(nama_mahasiswa) < nilai_maks:
            nama = input("Input nama mahasiswa : ")

            try :
                nilai = float(input("Masukan nilai mahasiswa : "))
                # logika untuk menambahkan nama mahasiswa
                nama_mahasiswa.append(nama)
                # logika untuk menambahkan nilai
                nilai_mahasiswa.append(nilai)
            except ValueError:
                print("Input tidak valid. Silahkan input kembali data : ")
        else:
            print(f"Data melebihi batas maksimal {nilai_maks}. silahkan input kembali")
    # logika untuk menu 2
    elif select == '2':
        # validasi untuk pengecekan data yang sudah di input
        if len(nama_mahasiswa) == 0:
            print("Data tidak di temukan. Silahkan input data kembali")
        else:
            # Logika untuk menampilkan nama dan nilai mahasiswa jika data valid
            for i in range(len(nama_mahasiswa)):
                print(f"index [{i}] - Nama : [{nama_mahasiswa[i]}] | Nilai : [{nilai_mahasiswa[i]}]")

    elif select == '3':
        # Logika perhitungan nilai tertinggi dan terendah
        if len(nama_mahasiswa) > 0:
            print(f"Nilai Tertinggi : {max(nilai_mahasiswa)}")
            print(f"nilia Terendah :  {min(nilai_mahasiswa)}")
        else:
            print("Data tidak ditemukan, silahkan input ulang data")

    elif select == '4':
        # Logika untuk pengitungan nilai rata-rata mahasiswa
        if len(nama_mahasiswa) > 0:
            rata_rata = sum(nilai_mahasiswa) / len(nama_mahasiswa)
            print(f"rata-rata nilai : {rata_rata:.2f}")
        else:
            print("Data tidak ditemukan, silahkan input ulang data")

    elif select == '5':
        if len(nama_mahasiswa):
            try:
                # Logika untuk melakukan perubahan pada data mahasiswa
                idx = int(input("Masukan indeks data yang aka di ubah : "))

                if 0 <= idx < len(nama_mahasiswa):
                    print(f"Data saat ini - Nama : {nama_mahasiswa[idx]} | Nilai : {nilai_mahasiswa[idx]}")

                    nilai_baru = float(input(f"Masukan nilai baru untuk data {nama_mahasiswa[idx]}"))

                    nilai_mahasiswa[idx] = nilai_baru

                    print("data berhasil di ubah")

                else:
                    print("Data array tidak dapat di temukan! Silahkan cek kembali idks data, kemudian input ulang")
            except ValueError:
                print("Input tidak valid ! Indeks haru menggunakan angka")
        else:
            print("Data masih kosong")

    elif select == '6':
        if len(nama_mahasiswa):
            try:
                # logika untuk melakukan penghapusan data mahasiswa
                idx = int(input("Masukan indeks data yang akan di hapus : "))

                if 0 <= idx < len(nama_mahasiswa):

                    name_dihapus = nama_mahasiswa[idx]

                    nama_mahasiswa.pop(idx)
                    nilai_mahasiswa.pop(idx)


                    print(f"data mahasiswa {nama_mahasiswa} berhasil di hapus")

                else:
                    print("Data array tidak dapat di temukan! Silahkan cek kembali idks data, kemudian input ulang")
            except ValueError:
                print("Input tidak valid ! Indeks haru menggunakan angka")
        else:
            print("Data masih kosong")

    # Logika untuk mengakhiri sesi aplikasi
    elif select == '7':
        print("Program selesai. Terimakasih")
        break
    else:
        print("pilihan anda tidak tersedia di menu !! Silahkan coba lagi")

