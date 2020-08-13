import time 
c0 = int(input("Hallo, enter number: "))
c2 = 0 ##Counter
c1 = c0 % 2 ###Do first check either the number is even or odd
while c0 != 1.0: ##Check weather there is work still to do.
     if c1 == 0:
        c0 = c0 // 2
        print(c0)
        c1 = c0 % 2
        c2 = c2 + 1
        time.sleep(1)
     elif c1 == 1:
        c0 = c0 * 3 + 1
        print(c0)
        c1 = c0 % 2
        c2 = c2 + 1
        time.sleep(1)
     
else:
    print("Done")
    print("Number of steps: ", c2)
        
            
