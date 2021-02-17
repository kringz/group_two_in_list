# given a list "lst", pair each item in the list with each item in the list

lst = ["welcome to the party"]
a = lst[0].split()

y = 0 # count the n item in the list
for i in a:
    x = 0 # count the n + 1 item in the list
    for i in a:
        first = a[y]
        other = a[x]
        print(first + other)
        x += 1
    y +=1

    
