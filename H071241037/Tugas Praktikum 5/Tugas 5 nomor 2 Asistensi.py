def buat_akronim(kalimat):
    # Pisahkan string menjadi daftar kata
    kata_kata = kalimat.split()
    print(kata_kata)
    # Ambil huruf pertama dari setiap kata, ubah menjadi huruf kapital
    akronim = ''.join([kata[0].upper() for kata in kata_kata])
    
    return akronim

# Contoh penggunaan
kalimat = "Dewan Perwakilan Rakyat "
akronim = buat_akronim(kalimat)
print(f"Akronim dari '{kalimat}' adalah: {akronim}")
