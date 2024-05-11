import random
harf = "abcdefglmnfhiplsdw"
sayi = "123456789"
sembol = "@#$/%&₺"
lower = "abcdefglmsne9"
upper ="ABCDESWFGHRKPMANW"

total = harf + sayi + sembol + lower + upper
print(total)

password = random.choices(total, k=21)
print(password)

password = "".join(password)
print(password)

