# program for sorting ascending order

a = [10,6,27,5,24,4,9,2,1,8]
l = len(a) - 1

for i in range(l):
    for x in range(l):
         if a[x]> a[x+1]:
            t = a[x]
            a[x]= a[x+1]
            a[x+1]=t

    print(a)