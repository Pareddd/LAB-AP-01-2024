def hitung_langkah(n):
    langkah = 0
    langkah_list = []  
    while n != 1:
        langkah_list.append(float(n)) 
        if n % 2 == 0:
            n //= 2  
        else:
            n = 3 * n + 1  
        langkah += 1
    langkah_list.append(float(1))  
    return langkah, langkah_list

def main():
    try:
        n = int(input("Masukan angka: "))
        if n <= 0:
            print("Input tidak Valid")
            return
        
        langkah, langkah_list = hitung_langkah(n)

        print("Langkah-langkah:")
        for step in langkah_list:
            print(step)
        
        print(f"Jumlah langkah: {langkah}")

    except ValueError:
        print("Input tidak Valid")

main()
