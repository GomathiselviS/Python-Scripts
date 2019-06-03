for i in range(1,9):    
    for j in range(1,i+1):
      print(f"{j}" , end=" ")
    print("\n")



h=0
for i in range(1,9):
    if h>8:
      break  
    for j in range(1,i+1):
      if h==8:
        break
      print(f"{h+1}" , end=" ")
      h=h+1
      
    print("\n")