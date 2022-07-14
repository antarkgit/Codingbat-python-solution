def sleep_in(weekday, vacation):
  '''if weekday == False and vacation == False:
    return True 
  if weekday == True and vacation == False:
    return False                                             
  if weekday == False and vacation == True:
    return True
  return True
  '''
  return not weekday or vacation



def monkey_trouble(a_smile, b_smile):
  '''if (a_smile == True and b_smile == True):
    return True
  if (a_smile == False and b_smile == False):
    return True
  if (a_smile == True and b_smile == False):
    return False
  return False'''
  return a_smile == b_smile



def sum_double(a, b):
  '''if (a==b):
    return 2*(a+b)
  return a + b
'''
  return a+b if a != b else 2*(a+b)



def diff21(n):
  '''if (n <= 21):
    return abs(21 - n)
  return 2* abs(21 - n)
'''
  return 21-n if n < 22 else 2*(n-21)



def parrot_trouble(talking, hour):
  #return (talking and (hour < 7 or hour > 20))
  return talking and hour not in range(7,21)



def makes10(a, b):
  '''if (a == 10 or b ==10 or a+b==10):
    return True
  return False'''
  return a+b == 10 or a == 10 or b == 10



def near_hundred(n):
  '''if abs(n - 100) <= 10 or abs(n - 200) <= 10 :
    return True
  return False
'''
  return abs(n-100) < 11 or abs(n-200) < 11 



def pos_neg(a, b, negative):
  '''if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))'''
  return (a < 0) ^ (b < 0) if not negative else (a < 0) and (b < 0)



def not_string(str):
  '''if len(str) >= 3 and str[:3]=="not":
   return(str)
  return("not " + str)'''
  return str if str[:3] == "not" else "not " + str



def missing_char(str, n):
  '''n>=0 and n <= (len(str)-1)
  front = str[:n]
  back = str[n+1:]
  return front + back'''
  return str[:n] + str[n+1:]



def front_back(str):
  '''def front_back(str):
  if len(str) <= 1:
    return str
   mid = str[1:len(str)-1] 
  return str[len(str)-1] + mid + str[0]'''
  return str if len(str) < 2 else str[-1] + str[1:-1] + str[0]



def front3(str):
  ''' if len(str) > 3:
    return(str[:3]+str[:3]+str[:3])
  
  if (len(str) <= 3):
    return(str + str + str)
'''
  return str[:(3 if len(str)>3 else len(str))]*3
