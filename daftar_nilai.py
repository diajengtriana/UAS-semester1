dataMhs = {}
print("==================================================================")
print("|                        DAFTAR NILAI MAHASISWA                  |")
print("==================================================================")

while True:
    print('\ntambah\t(t)\nubah\t(u)\nhapus\t(h)\ncari\t(c)\nlihat\t(l) ')
    c = input("\nsilahkan masukan pilihan : ")
    if (c.lower() == 't'):
        print('\nTambah Data Mahasiswa')
        nama= input("Masukkan Nama\t\t: ")
        nim= input("Masukkan NIM\t\t: ")
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dataMhs[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Ditambahkan!")
    elif (c.lower() == "u"):
        print('\nMengubah Data Mahasiswa')
        nama = input("Masukkan Nama: ")
        if nama in dataMhs.keys():
            nim= input("Masukkan NIM Baru\t: ")
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))
            nilaiUas= int(input("Masukkan NIlai UAS\t: "))
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
            dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
            print("\nData Berhasil Di Update!")
        else:
            print("Data tidak ditemukan!")
    elif (c.lower() == 'h'):
        nama = input("Masukkan Nama:  ")
        if nama in dataMhs.keys():
            del dataMhs[nama]
            print("Data Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada".format(nama))
    elif (c.lower() == 'c'):
        if dataMhs.items():
            nama= input("Masukkan Nama\t\t: ")
            nim= input("Masukkan NIM\t\t: ")
            print("\n                     DAFTAR NILAI MAHASISWA                      ")
            print("===================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
            print("===================================================================")
            i = 0
            for x in dataMhs.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} |  {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("===================================================================")
        else:
            print("\n                     DAFTAR NILAI MAHASISWA                      ")
            print("===================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
            print("===================================================================")
            print("|                        TIDAK ADA DATA!                          |")
            print("===================================================================")
    elif (c.lower() == 'l'):
        if dataMhs.items():
            print("\n                     DAFTAR NILAI MAHASISWA                      ")
            print("===================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
            print("===================================================================")
            i = 0
            for x in dataMhs.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} |  {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("===================================================================")
        else:
            print("\n                     DAFTAR NILAI MAHASISWA                      ")
            print("===================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
            print("===================================================================")
            print("|                        TIDAK ADA DATA!                          |")
            print("===================================================================")
    