# Lambda Function

# fungsi biasa
def kuadrat(angka):
    return angka**2

print(f"Hasil fungsi kuadarat = {kuadrat(4)}")

# lambda function
# output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f"Hasil fungsi kuadarat = {kuadrat(5)}")


pangkat = lambda num,pow:num**pow
print(f"Hasil pangkat = {pangkat(5,3)}")

# contoh lambda function

# sorting list biasa
data_list = ["wijaya","rey","yuji"]
data_list.sort()
print(f"Sorted list = {data_list}")

# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"Sorted list by panjang = {data_list}")

# sorting pakai lambda
data_list = ["wijaya","rey","yuji"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by panjang = {data_list}")
