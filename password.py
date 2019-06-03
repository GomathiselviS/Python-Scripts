from random import randint,sample
min_len = 8
max_len = 24
charlist_lower =[chr(i) for i in range(ord('a'),ord('z')+1)]
print(f"{charlist_lower}")
charlist_upper =[chr(i) for i in range(ord('A'),ord('Z')+1)]
print(f"{charlist_upper}")
numberlist=[i for i in range(0,10)]
specialcharlist=['!','@','#','$','%','_','-']
charlist = charlist_upper+charlist_lower+numberlist+specialcharlist
print(f"{charlist}")
password_len = randint(8,24)
print (password_len)

gen_password=sample(charlist,password_len)
print(gen_password)
gen_pword=str(''.join(map(str,gen_password)))
print(gen_pword)

u=0
l=0
n=0
s=0
for c in gen_pword:
  if c.isupper():
    u=u+1
  elif c.islower():
    l=l+1
  elif c.isdigit():
    n=n+1
  else:
    s=s+1
print(f"u:{u}, l:{l}, n:{n}, s:{s}")
if u==0 or l==0 or n==0 or s==0 :
  print("Password Policy Mismatch")
else :
  print("Strong Password")
