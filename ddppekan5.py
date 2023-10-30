#soal 1
mylist = ["B 1742", "suzuki", 1000, "biru"]

print(mylist)

#soal 2
mylist.append(200000000)
mylist.append(2)
mylist.insert(2,"suzuki")
mylist.insert(3,"kopling")
print(mylist)

#soal 3
luas= input("masukkan luas (1.persegi, 2.lingkaran, 3.segitiga): ")
match luas:
    case "1"|"persegi":
        sisi = int(input("masukkan nilai sisi : "))
        luaspersegi = sisi * sisi
        print(luaspersegi)
    case "2"|"lingkaran":   
        jarijari = int(input("masukkan nilai jari jari"))
        phi = int(input("masukkan nilai phi"))
        luaslingkaran = jarijari*phi
        print(luaslingkaran)
    case "3"|"segitiga":
        alas = int(input("masukkan nilai alas : "))
        tinggi = int(input("masukkan nilai tinggi : "))
        luassegitiga = alas*tinggi/2
        print(luassegitiga)

    case _:
        print("coba lagi")