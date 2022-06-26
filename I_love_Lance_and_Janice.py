"""
1)

I Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! 
Worse, you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". 
You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, 
it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] 
is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) 
is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", 
when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the 
commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.
"""
"""
encrypted = list(input())
decrypted = []

a_z_list = list(map(chr, range(97, 123)))
z_a_list = a_z_list[::-1]

for ch in encrypted:
    if(ch in a_z_list):
        decrypted.append(z_a_list[a_z_list.index(ch)])
    else:
        decrypted.append(ch)

print(''.join(decrypted))

"""

note = list(input())

for i in range(len(note)):
    ascii_code = ord(note[i])
    if(ascii_code>=97 and ascii_code<=122):
        note[i] = chr(122-ascii_code%97)
    
print(''.join(note))