# Membuat program array 2 dimensi untuk data nilai mahasiswa
# Project 2 - Struktur Data

print("=== PROGRAM DATA NILAI MAHASISWA DENGAN ARRAY 2 DIMENSI ")


# 1.Logika input jumlah mahasiswa (Maksimal 10)

jml_mahasiswa = 0
while True:
    try:
        jml_mahasiswa = int(input("Masukan jumlah mahasiswa dengan maksimal (10) : "))
        if 1 <= jml_mahasiswa <= 10:
            break
        print("Jumlah mahasiswa harus minimal 1 dan maksimal 10!!!")
    except ValueError:
        print("Input data harus berupa angka!!")

# 2. Logika Input jumlah mata kuliah (Maksimal 5)
jml_matkul = 0
while True:
    try:
        jml_matkul = int(input("Masukan jumlah mata kuiah dengan maksimal (5) : "))
        if 1 <= jml_matkul <= 5:
            break
        print("Jumlah mata kuliah minimal 1 dan maksimal 5!!")
    except ValueError:
        print("input data harus berupa angka!!")

# logika untuk meminta input dari user secara dinamis 

nama_matkul = []
print("\n---- Nama Mata Kuliah ----")
for i in range(jml_matkul):
    nama = input(f"Masukan nama mata kuliah ke-{i+1} : ")
    nama_matkul.append(nama)

# Array 1D untuk nama mahasiswa
nama_mahasiswa = []

# Array 2D untuk nilai mahasiswa
nilai_mahasiswa = []

# 3 & 4. Input nama mahasiswa & Input nilai setiap mata kuliah
for i in range(jml_mahasiswa):
    print(f"\n---- Data Mahasiswa ke ke-{i+1} ----")

    nama = input("Nama Mahasiswa : ")
    nama_mahasiswa.append(nama)

    nilai_per_mhs = [] # Array 1D ini menyimpan nilai-nilai untuk SATU mahasiswa

    for j in range(jml_matkul):
        while True:
            try:
                nilai = float(input(f"Nilai {nama_matkul[j]}: "))
                nilai_per_mhs.append(nilai) # Menambahkan ke list nilai_per_mhs 
                break
            except ValueError:
                print("Nilai harus berupa angka!!")

    nilai_mahasiswa.append(nilai_per_mhs)

# logika input nilai majasiswa dan outputnya adalah sebuah tabel
print("\n=== DATA NILAI MASISWA ===")

# Membuat Header Tabel
header = f"| No | {'Nama' :<12} |" 
for mk in nama_matkul:
    header += f" {mk} |"
header += " Rata-rata |"

print("-" * len(header))
print(header)
print("-" * len(header))

# 6. Logika perhitungan nila rata-rata  mahasiswa dan tampilkan ke tabel 
for i in range(jml_mahasiswa):
    # Menghitung rata-rata dari baris array 2D
    rata_rata = sum(nilai_mahasiswa[i]) / jml_matkul

    # Logika untuk memformat isi baris agar sejajar dengan header
    baris = f"| {i+1:2} | {nama_mahasiswa[i]:<12} |"

    for j in range(jml_matkul):
# Logika untuk menyamakan lebar kolom dengan nama matkulnya
     baris += f"{nilai_mahasiswa[i][j]:<{len(nama_matkul[j])}} |"
    baris += f" {rata_rata:<9.1f} |"
    print(baris)

print("-" * len(header))

# 7. Logika untuk menampilkan nilai tertinggi & terendah tiap mata kuliah 
print("\nNiliai tertinggi tiap mata kuliah : ")
for j in range(jml_matkul):
    # Logika mencari nilai max di dalam sebuah kolom dari Array 2D
    # Kita akan melakukan baris (i) untuk setiap kolom (j) yang tetap
    nilai_kolom = [nilai_mahasiswa[i][j] for i in range(jml_mahasiswa)]
    print(f"- {nama_matkul[j]:<15} : {max(nilai_kolom)}")

print("\nNilai terendah tiap mata kuliah :")
for j in range(jml_matkul):
    # Logika mencari nilai min di dalam sebuah kolom dari Array
    nilai_kolom = [nilai_mahasiswa[i][j] for i in range(jml_mahasiswa)]
    print(f"- {nama_matkul[j]:<15} : {min(nilai_kolom)}")