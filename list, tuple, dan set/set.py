# tipe data set

# list => []
# tuple => ()
# set => {}

# set   -> Data Harus Unik (tida menerima data duplikat)
#       -> Urutan tidak berlaku sehingga tidak bisa ambil index
#       -> hanya bisa menambah dan menghapus (add,remove)

nama = {"Eko", "Joko", "Eko"}
nama.add("Candra")
nama.remove("Eko")

for data in nama:
    print(data)