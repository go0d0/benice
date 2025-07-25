import time #liblary untuk time.sleep()

i = 1
while i<2:
    i += 1#increment loop
    simbol_unik = set("~`?/{}[]\"':;>.<,!@#$%^&*()_-+=\\|" ) # manual simbol

#nilai awal skor adalah 5, tiap kondisi if true akan berkurang 1, jika false nilai akan tetap.
    skor =5 
    print("\n")
    print("========== Selamat Datang ==========")
    print("====== Di program Pengecekan ======")
    print("============= password =============")
    print("\n\n")
    pw = input("masukkan password: ")
    if len(pw) <=5:
        print("panjang password minimal 6 karakter")
        skor -= 1 
        time.sleep(2)
    if not any(c.isupper() for c in pw): #ada huruf besar?
        print("harus ada huruf kapital")
        skor -= 1
        time.sleep(2)
    if not any(C.islower() for C in pw): # ada huruf kecil?
        print("harus ada huruf kecil")
        skor -= 1
        time.sleep(2)
    if not any(a.isdigit() for a in pw): #apakah ada angka?
        print("harus ada angka")
        skor -= 1
        time.sleep(2)
    if not any(s in simbol_unik for s in pw): #ada simbol unik?
        print ("harus ada simbol unik")
        skor -= 1
        time.sleep(2)
    print("\n\n")


#pengecekan kondisi dan memberikan status informasi apakah 
#password lemah,medium,kuat, berdasarkan skor dari kondisi sebelumnya 
    if skor <= 2:
        print(f"skor password anda : {skor}, your password too weak!")
        time.sleep(2)
    if skor == 3:
        print(f"skor password anda: {skor}, your password strength is medium")
        time.sleep(2)
    if skor >= 4:
        print(f"skor password anda : {skor}, your password is strong")
        time.sleep(2)
    time.sleep(3)

print("\n\n")
time.sleep(5) #sleep 5 detik
print("Terimakasih sudah menggunakan program pengecekan password ini.")
print("tetap waspada celah keamanan disekitar anda, kejahatan tidak tidur.")
