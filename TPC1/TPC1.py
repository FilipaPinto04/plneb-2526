#Exercício 1.given a string “s”, reverse it.
def reverse_string(s):
    return s[::-1]

print(f' Exercício 1 : {reverse_string("Python")}')

#Exercício 2. given a string “s”, returns how many “a” and “A” characters are present in it.
def count_A(s):
    return s.count('a') + s.count('A')

print(f' Exercício 2 : {count_A("A Filipa foi para Braga.")}') 

#Exercício 3. given a string “s”, returns the number of vowels there are present in it.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(f' Exercício 3 : {count_vowels("Engenharia")}')

#Exercício 4. given a string “s”, convert it into lowercase.
def lowercase(s):
    return s.lower()

print(f' Exercício 4 : {lowercase("EngeNHarIa")}')

#Exercício 5. given a string “s”,  convert it into uppercase.
def uppercase(s):
    return s.upper()

print(f' Exercício 5 : {uppercase("Engenharia")}')

#Exercício 6. Verifica se uma string é capicua
def capicua(s):
    return s == s[::-1]

print(f' Exercício 6 : "radar" -  {capicua("radar")}')
print(f' Exercício 6 : "carro" -  {capicua("carro")}')

#Exercício 7. Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2.)
def balanced(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

print(f' Exercício 7 : "ola", "escola" - {balanced("ola", "escola")}')
print(f' Exercício 7 : "adeus", "escola" - {balanced("xyz", "escola")}')

#Exercício 8. Calcula o número de ocorrências de s1 em s2
def occurrences(s1, s2):
    return s2.count(s1)

print(f' Exercício 8 : "ss" em "mississippi": {occurrences("ss", "mississippi")}')

#Exercício 9. Verifica se s1 é anagrama de s2. 
# ○ "listen" e "silent": Deve imprimir True
# ○ "hello", "world": Deve imprimir False
def anagram(s1, s2):
    sa = s1.replace(" ", "").lower()
    sb = s2.replace(" ", "").lower()
    
    return sorted(sa) == sorted(sb)

print(f' Exercício 9 : ("listen", "silent") {anagram("listen", "silent")}')
print(f' Exercício 9 : ("hello", "world") {anagram("hello", "world")}')
