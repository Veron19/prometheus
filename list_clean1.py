import sys
import math
#clean_list =[5,1,2,5,6,5,6,1.1,2]
#c[1]="sun"
#c.append(3.6)
clean_list = int(sys.argv[1])
d =[]
for i in clean_list:
    #if i != 5:  #не равно 5
    if i not in d:
        d.append(i)

print ('clean_list= '+str(clean_list))
print ('d= '+str(d))
