#https://docs.python.org/3.4/library/stdtypes.html?highlight=set#set

def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)
    
print (is_isogram("Dermatoglyphics"))
print (is_isogram("aba"))
print (is_isogram("moOse"))
print (is_isogram(""))
