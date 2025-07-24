import time

i = 1
while i<4:
    i += 1
    simbol_unik = set("~`?/{}[]\"':;>.<,!@#$%^&*()_-+=\\|" )


    skor = 0
    print("\n")
    print("========== Selamat Datang ==========")
    print("====== Di program Pengecekan ======")
    print("============= password =============")
    print("\n\n")
    pw = input("masukkan password: ")
    if len(pw) <=5:
        print("panjang password minimal 6 karakter")
        skor += 1
        time.sleep(2)
    if not any(c.isupper() for c in pw):
        print("harus ada huruf kapital")
        skor += 1
        time.sleep(2)
    if not any(C.islower() for C in pw):
        print("harus ada huruf kecil")
        skor += 1
        time.sleep(2)
    if not any(a.isdigit() for a in pw):
        print("harus ada angka")
        skor += 1
        time.sleep(2)
    if not any(s in simbol_unik for s in pw):
        print ("harus ada simbol unik")
        skor += 1
        time.sleep(2)
    print("\n\n")

#buggggg skor nya jalan terus
    if skor <= 2:
        print("your password too weak!")
        time.sleep(2)
    if skor == 3:
        print("your password strength is medium")
        time.sleep(2)
    if skor >= 4:
        print("your password is strong")
        time.sleep(2)
    time.sleep(3)

#this code will be develop in the future
#program for sleep,  this just for debug if program can exit from while loop
print("\n\n")
time.sleep(5)
print("keluar dari while")
