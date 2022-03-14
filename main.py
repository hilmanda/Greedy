__author__ = "Hilmanda Panji Orienski"

import numpy as np
from string import ascii_uppercase
import time

title = input("Input nama File tanpa ekstensi: ")
directory ="input/" #default directory, ganti ketika directory file berubah, folder input dan file python harus dalam directory yang sama, kosongkan jika tidak dalam folder
data = np.loadtxt(directory + title + ".txt", dtype="f", delimiter=" ")

waktu_awal = time.time()
keys = list(ascii_uppercase)
keys = keys[:len(data)]

data=data.tolist() #parsing array ke list
dict_data = {keys[j]:{keys[i]:round(data[j][i],2) for i in range(len(data))}  for j in range(len(data))} #parsing list ke dictionary

#mencari jarak tempuh rata2
def find_average(data):
    total = 0
    n = 0
    # ambil matriks segitiga atas untuk mencari jarak tempuh rata2
    for kolom in data :
        for baris in range(data.index(kolom),len(kolom)):
            total+=kolom[baris]
            n+=1
    rata2 = total/n

    return round(rata2,2)

#cari lokasi yang cocok untuk membangun gedung damkar menggunakan algoritma greedy
def greedy_scp(max_length):
    dict_cover_kota : dict = {i:{} for i in keys} # buat dictionary 2d dengan keys alphabet dan value empty dictionary
    
    # lgoritma greedy, mencari lokasi yang tercover jika penempatan gedung di key1
    for key1 in keys:
        print(f"Lokasi {keys.index(key1)+1}: Kota {key1}")
        print("Lokasi yang di cover: ",end="")
        for key2 in keys:
            if dict_data[key1][key2] <= max_length :
                dict_cover_kota[key1].update({ key2:dict_data[key1][key2]}) # simpan data area yang tecover rata2
                
        print(list(dict_cover_kota[key1].keys()))
        print()

    #algoritma greedy, mencari lokasi yang dapat mengcover area terbanyak
    max_covered = (max(dict_cover_kota.values(), key = len))
    list_max_covered : dict = {}
    save_jarak : dict = {}
    for key in keys :
        if len(dict_cover_kota[key]) == len(max_covered) :
            list_max_covered[key] = []
            list_max_covered[key]=dict_cover_kota[key]
            save_jarak[key] = round(sum(list_max_covered[key].values()),2)

    #mencari yang paling pendek jarak antar kota nya dari hasil greedy di atas
    best_result = min(save_jarak.values())
    for kota, jarak in save_jarak.items():
        if jarak == best_result:
            best_result = kota
    print()
    print("Kota yang paling banyak mengcover area:",list(list_max_covered.keys()))
    print()
    print("Kota yang paling bagus untuk membangun gedung damkar:",best_result)

def main():
    max_length = find_average(data)
    print("Area Covered by Damkar :",max_length)
    greedy_scp(max_length)
    print()
    waktu_akhir = time.time() - waktu_awal
    print("Waktu eksekusi:",waktu_akhir)
    print()
    print("Spek laptop : AMD Ryzen 3-5300U (4 Cores, 8 Threads, 2.6GHz, up to 3.8GHz), RAM 8GB, SSD M.2 Nvme 512GB")

if __name__ == '__main__' :
    main()