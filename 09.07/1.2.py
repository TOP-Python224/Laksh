import random 
from math import *
letters = {'a', 'b', 'c'}
str_letters = ''
for i in letters:
    str_letters += str(i)



def all_perms(elements):
    """Генерирует перестановки для переданного множества элементов."""
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]                

        
        
generator_perm = all_perms(str_letters)
print(*list(sorted(generator_perm)))


# stdout:
# abc acb bac bca cab cba

# Алгортим взят из интернет источника https://overcoder.net/q/3498/%D0%BA%D0%B0%D0%BA-%D1%81%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2%D1%81%D0%B5-%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%B2-python
    
    
    
    