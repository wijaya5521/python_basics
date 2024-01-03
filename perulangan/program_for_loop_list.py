# program for loop

# membuat variabel banyaknya data
banyak = int(input("Berapa banyak data yang dibuat? "))

# membuat array
nama = []
umur = []

for i in range(0,banyak) :
    print(f"\nData ke {i+1}")
    input_nama = input(f"Masukkan Nama Anda : ")
    input_umur = int(input("Berapa Umur Anda : "))

    nama.append(input_nama)
    umur.append(input_umur)

print("\n")
print("=============================")
print("Berikut ini adalah data yang telah anda buat")
print("=============================")
for i in range (0,len(nama)) :
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"\nData Ke-{i+1}")
    print(f"Nama : {data_nama}")
    print(f"Umur : {data_umur}\n")
