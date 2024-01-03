''' *args '''

# Memasukkan data/argumen

def fungsi(nama,tinggi,berat):
    print(f"nama : {nama}, punya tinggi : {tinggi} dan berat : {berat}")

fungsi('ucup',170,50)

def fungsi_data(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"nama : {nama}, punya tinggi : {tinggi} dan berat : {berat}")
    
fungsi_data(["otong",100,30])

# Kenalan dengan *args
def fungsi_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama : {nama}, punya tinggi : {tinggi} dan berat : {berat}")

fungsi_args("dudung",160,55)
    

    
