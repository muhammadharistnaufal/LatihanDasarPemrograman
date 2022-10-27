print("===========Program Nilai=============")

nilai = int(input("masukan nilai anda : "))

if nilai >= 100:
    grade = "Nilai yang dimasukan berlebihan dan tidak ada dalam data"
    predikat = "Tidak ada dalam data"
elif nilai >= 90:
    grade = "A"
    predikat = "Dengan pujian"
elif nilai >= 80:
    grade = "B"
    predikat = "Sangat Memuaskan"
elif nilai >= 70:
    grade = "C"
    predikat = "Memuaskan"
elif nilai >= 60:
    grade = "D"
    predikat = "Tidak Memuaskan"
elif nilai <= 0:
    grade = "Nilai yang dimasukan tidak ada dalam data"
    predikat = "Tidak ada dalam data"
else:
    grade = "E"
    predikat = "Tidak Lulus"
    
print("Grade:  %s" %grade)
print("Predikat: %s " %predikat)                    
        