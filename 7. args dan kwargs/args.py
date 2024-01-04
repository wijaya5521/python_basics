# args

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} cm dan berat badan {berat} kg")

fungsi('wijaya',160,53)

def fungsi2(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat badan {berat} kg")

fungsi2(['wijaya',160,53])
    
## Menggunakan *args
def fungsi_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat badan {berat} kg")
    
fungsi_args('Wijaya',160,53)


## contoh *args
def tambah(*data):
    hasil = 0
    for angka in data:
        hasil += angka
    return hasil

print(tambah(1,2,3,4,5,6,7,8,9,10))