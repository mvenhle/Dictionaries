# A python program script to generate and print a diction that contains a number between 1 and n. In the form (x,x*x).


n=int(input("Input a number"))
d = dict()
for x in range(1, n + 1):
    d[x]= x * x

print(d)