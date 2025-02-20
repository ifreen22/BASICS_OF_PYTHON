for i in range(0, 51):  # SAME AS INDEXING OF A STRING
    if(i%2==0):
        print(i)      # = for i in range(51)
        



for i in range(0, 100, 4):
    if(i%16==0):        #EK HEE VARIABLE KO BAAR BAAR USE KAR SAKTE HAI (i)
        continue        # also use for break
    print(i)










j=0
while(j<=1000):
    print(j)
    j += 2







l = [1, 5, 32, 1, "IFREEN", 5.9, 0, 0]
t = (2, 8, 9, 4, 6, 3, 0)
s = "Ifreen"

for z in s:
    print(z)

for x in l:
    print(x)

for y in t:
    print(y)

k=0
while(k<len(l)):
    if(type(l[k] == str)):
        continue
    print(l[k])
    k += 1



for a in 600 :
    pass         #FOR DOING AFTER (PENDING)


i=0
while(i<45):
    print(i)
    i +=1
