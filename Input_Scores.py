data_matkul = []

nama_mahasiswa = input('Nama Mahasiswa: ')
nim_mahasiswa = input('NIM Mahasiswa: ')

def konversi_nilai(nilai_matkul):
    if 85 <= nilai_matkul <= 100:
        return "A"
    elif 70 <= nilai_matkul <= 84:
        return "B"
    elif 60 <= nilai_matkul <= 69:
        return "C"
    elif 50 <= nilai_matkul <= 59:
        return "D"
    elif 0 <= nilai_matkul <= 49:
        return "E"
    else:
        return "Nilai Tidak Valid!"

def bobot_nilai(nilai_huruf):
    if nilai_huruf == 'A':
        return 4.0
    elif nilai_huruf == 'B':
        return 3.0
    elif nilai_huruf == 'C':
        return 2.0
    elif nilai_huruf == 'D':
        return 1.0
    else:
        return 0.0

while True:
    kode_matkul = input('Kode Mata Kuliah: ')
    nama_matkul = input('Nama Mata Kuliah: ')
    sks_matkul = int(input('SKS Mata Kuliah: '))
    nilai_matkul = int(input('Nilai Matakuliah: '))

    nilai_huruf = konversi_nilai(nilai_matkul)

    matkul = {
        "kode": kode_matkul,
        "nama": nama_matkul,
        "sks": sks_matkul,
        "nilai_angka": nilai_matkul,
        "nilai_huruf": nilai_huruf
    }

    data_matkul.append(matkul)

    lanjut = input('Apakah tambah matakuliah lagi? (y/n): ').lower()
    if lanjut != "y":
        break

total_sks = 0
total_nilai = 0
total_bobot = 0

for matkul in data_matkul:
    sks = matkul["sks"]
    huruf = matkul["nilai_huruf"]
    nilai = matkul["nilai_angka"]
    bobot = bobot_nilai(huruf)

    total_sks += sks
    total_nilai += nilai
    total_bobot += bobot * sks

ipk = total_bobot / total_sks

print('===============================')
print(f'Nama Mahasiswa : {nama_mahasiswa}')
print(f'NIM            : {nim_mahasiswa}')
print(f'Total SKS      : {total_sks}')
print(f'Total Nilai    : {total_nilai}')
print(f'IPK Anda       : {ipk:.2f}')
print('===============================')


import csv

nama_file = f'{nama_mahasiswa}-{nim_mahasiswa}.csv'

with open(nama_file, mode='w', newline='') as file:
    fieldnames = ["kode", "matakuliah", "sks", "nilai_angka", "nilai_huruf"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for matkul in data_matkul:
        writer.writerow(matkul)

print(f'Data berhasil disimpan ke file: {nama_file}')
