import os
os.system("cls")

# Inisiasi
nama = []
nomor = []
program = True

while(program) :
    
    # Daftar Menu
    print("-"*20)
    print("PROGRAM KONTAK")
    print("-"*20)
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Ubah Kontak")
    print("4. Hapus Kontak")
    print("0. Keluar")

    # Input Pilih Menu
    pilihMenu = int(input("Masukkan Pilihan Anda : "))
    
    # Daftar Kontak
    if(pilihMenu == 1) :
        if(len(nama) == 0) :
            print("Kontak Belum Tersedia")
            False
        for i in range(0,len(nama)) :
            dataNama = nama[i]
            dataNomor = nomor[i]
            
            print("\n")
            print("Daftar Kontak")
            print("-"*15 + "\n")
            print(f"Kontak {i+1}")
            print(f"Nama : {dataNama}")
            print(f"Nomor : {dataNomor}")
      
    # Tambah Kontak
    elif(pilihMenu == 2) :
        inputNama = input("Masukkan Nama : ")
        inputNomor = input("Masukkan Nomor : ")
        
        nama.append(inputNama)
        nomor.append(inputNomor)
        
    # Ubah Kontak
    elif(pilihMenu == 3) :
        pilihKontak = input("Masukkan nama kontak yang ingin diubah! : ")
        indexKontak = nama.index(pilihKontak)
        if(indexKontak>=0):
            ubahData = int(input("Pilih data yang ingin diubah : \n1. nama   2. nomor  3. nama dan nomor\n"))
            if(ubahData == 1):
                inputNama = input("Masukkan Nama Yang Baru : ")
                nama[indexKontak] = inputNama
            elif(ubahData == 2): 
                inputNomor = input("Masukkan Nomor Yang Baru : ")
                nomor[indexKontak] = inputNomor
            elif(ubahData == 3):
                inputNama = input("Masukkan Nama Yang Baru : ")
                inputNomor = input("Masukkan Nomor Yang Baru : ")    
                nama[indexKontak] = inputNama
                nomor[indexKontak] = inputNomor
            
    # Hapus Kontak
    elif(pilihMenu == 4) :
        pilihKontak = input("Masukkan nama kontak yang ingin dihapus! : ")
        indexKontak = nama.index(pilihKontak)
        
        nama.remove(nama[indexKontak])
        nomor.remove(nomor[indexKontak])
        
        print(f"Kontak dengan Nama : {nama[indexKontak]} telah dihapus")
        
    elif(pilihMenu == 0) :
        break
    
    else :
        print("Mohon untuk memilih pilihan yang tersedia")
        continue
    
    # Melanjutkan Atau Tidak
    print("\n")
    pilih = int(input("Apakah ingin lanjut atau tidak? 1. Ya     2. Tidak : "))
    if(pilih == 1) :
        True
    elif(pilih == 2) :
        print("Program Selesai...")
        program = False
    else :
        print("Mohon Pilih Jawaban Yang Tersedia")
        program = False
        
    os.system("cls")
        
        