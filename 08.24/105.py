# СДЕЛАТЬ: приведите код в порядок: оформите согласно рекомендациям и примерам горизонтальные и вертикальные отступы, правильно расположите строки документации

num_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

num_dict_inv = {k : v for v , k in num_dict.items()}


def decimal( num: int,
                        *,
                        bus_num: int = 16) -> str:
                        """Преобразует десятичное число в 16-ную систему исчисления """
                        
                        private = num // bus_num
                        remainder = num % bus_num
                        
                        num = num_dict.get(remainder, remainder)
                        
                        while private > 0:
                            
                            remainder =  private % bus_num
                            private =  private // bus_num
                            num = num_dict.get(remainder, str(remainder)) + str(num)
                            
                        return num 
                            
def hexadecima(num: str,
                              *,
                              bus_num: int = 16) -> int:
                              """Преобразует  обратно в десятичную систему исчисления """
                
                              num_back = str(num)[::-1]
                              sum  = 0
                              for i in range(len(num_back)):
                                  if num_back[i].title() in num_dict_inv:
                                      if  0 <=  num_dict_inv[num_back[i].title()] <= bus_num:
                                          sum += num_dict_inv[num_back[i].title()] * bus_num ** i
                                      else:
                                          raise ValueError('Число не принадлежит системе исчисления')
                                  elif num_back[i].isdecimal():
                                      if 0 <= int(num_back[i]) <= 16:
                                          sum += int(num_back[i]) * bus_num ** i
                                      else:
                                          raise ValueError('Число не принадлежит системе исчисления')
                                  else:
                                      raise ValueError('Символ не принадлежит системе исчисления')
                                       
                              return sum

def result_invent(num: int,
                         from_bus_num: int,
                         in_bus_num: int) -> int|str:
                         return decimal(hexadecima(num = num , bus_num =  from_bus_num),bus_num = in_bus_num)
                          
                          


num = input('Введите число в исходной системе счисления: ')
from_bus_num = int(input('Введите исходную систему счисления (2-16): '))
in_bus_num = int(input('Введите целевую систему счисления (2-16): '))

if 2 <= from_bus_num <= 16 and 2 <= in_bus_num <= 16:
    print(result_invent(num, from_bus_num, in_bus_num))
else:
    raise ValueError('Неправильная система счисления!')
    
    
    
    
# stdin:
# Введите число в исходной системе счисления: 5a698d
# Введите исходную систему счисления (2-16): 2
# Введите целевую систему счисления (2-16): 16
# Traceback (most recent call last):
  # File "C:\Users\Владимир\Documents\GitHub\Laksh\08.24\105.py", line 62, in <module>
    # print(result_invent(num, from_bus_num, in_bus_num))
  # File "C:\Users\Владимир\Documents\GitHub\Laksh\08.24\105.py", line 52, in result_invent
    # return decimal(hexadecima(num = num , bus_num =  from_bus_num),bus_num = in_bus_num)
  # File "C:\Users\Владимир\Documents\GitHub\Laksh\08.24\105.py", line 36, in hexadecima
    # raise ValueError('Число не принадлежит системе исчисления')
# ValueError: Число не принадлежит системе исчисления


# Введите число в исходной системе счисления: 1a45a
# Введите исходную систему счисления (2-16): 14
# Введите целевую систему счисления (2-16): 15
# 14B80