# 1
guess_me = 7
if(guess_me > 7):
    print("to high")
elif(guess_me < 7):
    print("to low")
else:
    print("just right")

# 2
start = 1
while(start < 9):
    print(start)
    if(start==guess_me):
        print("found it")
        start+=1
    elif(start < guess_me):
        print("too low")
        start+=1
        continue
    else:
        print("oops")
        break

# 3
spisok = [3, 2, 1, 0]
for i in spisok:
    print(i)

# 4
def my_list(your_list):
    return your_list

your_list = ['Harry', 'Ron', 'Hermione']
print(my_list(your_list))

# 5
class OopsException(Exception):
    pass

try:
    m = 10
    i = 5
    while(i >= 0):
        s = m/i
        print(s)
        i -= 1
        if(i==0):
            raise OopsException()

except OopsException:
    print('Caught an oops, i = ', i)

# 6
import math as m
def koren(a):
    k = lambda a: m.sqrt(a)
    return k(a)

print(koren(9))