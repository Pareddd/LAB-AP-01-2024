def gameHartaKarun():
    penggalian = 0
    bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan jarak langkah yang ditempuh dalam meter (0 untuk berhenti): "))
            
            if langkah < 0:  
                print("Program dihentikan.")
                break
            
            if langkah == 0:  
                break
            
            penggalian += langkah  
            
            if langkah > 20:  
                bahaya = True
        
        except ValueError:  
            print("Input tidak valid. Harap masukkan bilangan bulat.")
            continue
    print(f"Total jarak: {penggalian} meter")

    if bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
        print("ada bahaya: ya")
    elif penggalian == 50:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
        print("ada bahaya: tidak")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")
        print("ada bahaya: tidak")

gameHartaKarun()
