import re
def sisfo(pass1):
    if len(pass1) != 45:
        return "False"
    a = r"^[A-Z-a-z02468]{40}"
    b = r"[13579\s]{5}$"
    c = a + b
    if re.match(c, pass1):
        return "True"
    else:
        return "False"
karakter = input("Masukkan disini: ")
print(sisfo(karakter)) 
