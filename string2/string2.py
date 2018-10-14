def double_char(str):
  s=""
  for i in str:
    s+=i*2
  return s
  
def count_hi(str):
  return str.count("hi")
  
def cat_dog(str):
  return str.count("cat")==str.count("dog")
  
def count_code(str):
  c=0
  for i in range (0,len(str)-3):
    if str[i]=='c'and str[i+1]=='o' and str[i+3]=='e':
      c+=1
  return c
  
def end_other(a, b):
  a=a.lower()
  b=b.lower()
  return a.find(b,len(b)*-1)!=-1 or b.find(a,len(a)*-1)!=-1
  
def xyz_there(str):
  for i in range (0,len(str)-2):
    if str[i]=='.' and (str.find('xyz',i+1,i+1)>i or str.find('xyz')<i):
      return True
    elif str.find('.',i)==-1 and str.find('xyz')!=-1:
      return True
  return False
  
