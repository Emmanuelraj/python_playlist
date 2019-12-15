#for Loop
ninjas=['Joe','Doe','Ryu'];


# for ninja in ninjas:
    # print(ninja);

for ninja in ninjas[0:3]:
    print(ninja);



# fibonacci series 0,1,1,2,3
n =int(input('Enter the fib nums:'));

fib=[0,1];
#for loop from index of (2,n)
for i in range(2,n):
  fib.append(fib[i-1]+fib[i-2]);

print(fib);

# reverse List

print(len(fib));
