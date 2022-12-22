print(50*"=")
print("\t\tKEYBOARD NYAMAN")#judul pada pemprograman
print(50*"=")
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']# untuk list keyboard di sisi kanan
kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']#untuk list keyboard di sisi kiri


input_usr = input("Masukan Kalimat: ")# user menginputkan kalimat yang akan di analisa
jml_huruf = len(input_usr)#perintah len digunakan untuk menjumlahkan sebuah input dari user
    
for x in range ( jml_huruf):#perintah for digunakan untuk perulangan
    huruf1 = input_usr[x-1]
    huruf2 = input_usr[x]
    
    tamp = huruf1 in kiri
    cek = input_usr[x] in kiri
        
    cek_hrf = cek ^ tamp
    if not cek_hrf:
        print(cek_hrf)
        if cek:
            print(f"penjelasan : karakter yang berdempetan yakni {huruf1} dan {huruf2} berada di satu tangan (kiri)")
            break
        else:
            print(f"penjelasan : karakter yang berdempetan yakni {huruf1} dan {huruf2} berada di satu tangan (kanan)")
            break
else:   
    if cek_hrf:
        print("True")
        print("Penjelasan: Setiap karakater selalu bergantian tangan.")