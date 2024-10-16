def Palindrome(kata):
    kata = kata.lower()
    
    kata = kata.replace(" ", "")
    
    if kata == kata[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

Palindrome("Kasur ini rusak")
Palindrome("Aku Sayang kamu")
