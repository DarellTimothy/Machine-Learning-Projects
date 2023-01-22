#NIM/Nama : 16022344/Darell Timothy Tarigan
#Tanggal : 30 September 2022
#Deskripsi : Problem 1


N = int(input("Masukkan Nilai N : "))
A = int(input("Masukkan Nilai A : "))
B = int(input("Masukkan Nilai B : "))
C = int(input("Masukkan Nilai C : "))

for i in range(1,N+1) :
    if i%A == 0 and i%B == 0 and i%C == 0 :
        print("SiapBangJago")
    elif i%A == 0 and i%B == 0 :
        print("SiapBang")
    elif i%A == 0 and i%C == 0 :
        print("SiapJago")
    elif i%B == 0 and i%C == 0 :
        print("BangJago")
    elif i%C == 0 :
        print("Jago")    
    elif i%B == 0 :
        print("Bang")
    elif i%A == 0 :
        print("Siap")
    else :
        print(i)   
