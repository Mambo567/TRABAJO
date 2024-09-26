def multiples(integer,limit):
    times = limit/integer
    i = times/times
    num_list = []
    while i <= times:
        add_value = integer * i
        num_list.append(add_value)
        i = i + 1 

    print(num_list)
    
multiples(2,12)

