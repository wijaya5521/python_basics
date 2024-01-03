'''fungsi biasa'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} cm dan berat badan {berat} kg")

fungsi('wijaya',160,53)

''' fungsi kwargs '''
def fungsi_kwargs(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} punya tinggi {tinggi} cm dan berat badan {berat} kg")
    
fungsi_kwargs(nama='Wijaya',tinggi=160,berat=53)

'''contoh kwargs'''
def math(*data, **pilihan):
    hasil = 0
    if(pilihan['option']=='tambah'):
        for angka in data:
         hasil += angka
    if(pilihan['option']=='kurang'):
        for angka in data:
         hasil -= angka
        
    return hasil

print(math(1,2,3,4,5,option='tambah'))
print(math(1,2,3,4,5,option='kurang'))
