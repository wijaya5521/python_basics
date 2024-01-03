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

