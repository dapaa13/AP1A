from numpy import array

baris = 4
kolom = 5
matriks = array([array([0]*5)]*4)

for brs in range(baris):
    for kol in range(kolom):
        print(f"elemen baris = {brs} kolom = {kol}")
        matriks[brs][kol] = int(input())

print(matriks)