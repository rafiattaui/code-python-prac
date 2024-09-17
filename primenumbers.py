k= int(input("Number: "))
m = True

if k <= 1:
    print("Not prime")

for i in range(2,k):
    if k % i == 0:
        print("Not prime")
        m = False
        break
if m:
    print("Prime")





