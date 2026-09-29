# Membuat program array 1 dimensi untuk aplikasi management barang
# Tugas (Project 3)

# deklarasi variable untuk nama barang, harga, jumlah maksimal kapasitas

nama_barang = []
harga_barang = []
jumlah_maks_barang = 20

# melakukan looping untuk management menu utama
while True:
    # Menampilkan menu program
    print("\n=== MENU APLIKASI MANAGEMENT BARANG ===")
    print("1. Input Data")
    print("2. Tampilkan Data")
    print("3. Cari Barang")
    print("4. Urutkan Harga")
    print("5. Hapus Data")
    print("6. Keluar")
    # Input untuk memilih menu program
    select = input("Pilih menu : ")
    # Validasi untuk menu pertama
    if select == "1":
        if len(nama_barang) < jumlah_maks_barang:
            nama = input("Input nama barang : ")

            try :
                harga = float(input("Masukan harga barang : "))
                nama_barang.append(nama)
                harga_barang.append(harga)
            except ValueError:
                print("Input tidak valid. Silahkan input kembali data : ")
        else:
            print(f"Data melebihi batas maksimal {jumlah_maks_barang}. silahkan input kembali")
        # Validasi untuk menu kedua
    elif select == '2':
        print("\n----- List All Data Barang -----")
        if len(nama_barang) == 0:
            print("Data tidak di temukan. Silahkan input data kembali")
        else:
            for i in range(len(nama_barang)):
                print(f"index [{i}] - Nama : [{nama_barang[i]}] | Harga : Rp. [{harga_barang[i]}]")
       # Validasi untuk menu ketiga
    elif select == '3':
        if len(nama_barang) > 0:
            cari = input("Masukan nama barang yang dicari : ").lower()
            find = False
            print("\n---- Hasil Pencarian -----")
            for i in range(len(nama_barang)):
                # Logika output hasil pencarian barang
                if cari in nama_barang[i].lower():
                    print(f"index [{i}] | Nama : {nama_barang[i]} | Harga : Rp. {harga_barang[i]:,.0f}")
                    find = True
            if not cari:
                print("Barang tidak di temukan")
        else:
            print("Data masih kosong. Silahkan input data terlebih dahulu")
    # Validasi untuk menu keempat
    elif select == '4':
        if len(nama_barang) > 0:
             kompress = sorted(zip(harga_barang, nama_barang))
             harga_barang, nama_barang = map(list, zip(*kompress))
             print("Data telah berhasil di urutkan berdasarkan harga terendah")
        else:
            print("Data msih terdeteksi kosong")
    # Validasi untuk menu kelima
    elif select == '5':
        if len(nama_barang):
            try:

                idx = int(input("Masukan nama data barang yang ingin di hapus : "))

                if 0 <= idx < len(nama_barang):
                    removed = nama_barang.pop(idx)
                    harga_barang.pop(idx)
                    print(f"Data Barang '{removed}' berhasil di hapus")

                else:
                    print("Indeks tidak di temukan dalam daftar")
            except ValueError:
                print("Input tidak valid ! Indeks haru menggunakan angka")
        else:
            print("Data masih belum tersedia")
       # Validasi untuk menu terakhir
    elif select == '6':
           print("Program selesai. Terimakasih")
           break
    else:
           print("pilihan anda tidak tersedia di menu !! Silahkan coba lagi")

