def f1(n) : 
    fact = 1
    while (n != 0) : 
        fact = fact * n 
        n = n - 1
    return fact 
  
def isKrishnamurthy(n) : 
    sum = 0
    temp = n 
    while (temp != 0) : 
  
        
        rem = temp%10
        sum = sum + f1(rem) 
  
        temp = temp // 10
          
    return (sum == n) 
  
n = int(input(" Enter Any Number "))
if (isKrishnamurthy(n)) : 
    print("YES") 
else : 
    print("NO") 