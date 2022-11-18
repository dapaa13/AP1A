#main()
#luas segitiga 
def luas_segitiga(a, t):
    return a * t / 2.0
def main():
    alas = int(input('Masukkan alas segitiga : '))
    tinggi = int(input('Masuikkan tinggi segitiga : '))
    luas = luas_segitiga(alas, tinggi)
    print('Luas segitiga adalah : ', luas,'cm')
main()