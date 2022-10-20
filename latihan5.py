# Deskriptif
# membuat variabel nama barang = kosmetik
# membuat variabel harga barang = 100000
# membuat variabel persen barang = 
# input nama barang 
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input("masukan nama barang :")
    harga_barang = int(input("masukan harga barang : "))
    persen = int(input("masukan persen barang : "))
    barang_terjual = int(input("masukan jumlah barang yang terjual : "))

    keuntungan_persen = harga_barang * persen / 100
    harga_jual = harga_barang + keuntungan_persen

    #menghitung modal
    modal = harga_barang * barang_terjual
    #menghitung modal keseluruhan
    modal_keseluruhan =modal_keseluruhan + modal

    #menghitung laba
    laba = keuntungan_persen * barang_terjual

    print("barang", nama_barang)
    print("harga barang", harga_barang)
    print("keuntungan per barang", keuntungan_persen)
    print("dijual dengan harga", harga_jual)
    print("terjual", barang_terjual)
    print("modal", modal)
    print("laba", laba)


    
    apakah_lanjut = input ("apakah anda ingin melanjutkan?Y untuk Ya N untuk No : ")
    if(apakah_lanjut !="Y"):
        break
print("------------")
print("modal keseluruhan",modal_keseluruhan)
print("laba keseluruhan",laba_keseluruhan)
