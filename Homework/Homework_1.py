# Question 2
# a
def shift(lst,k):
    for num in range(k):
        lst.append(lst[0])
        lst.pop(0)
    return lst

# b
def shift_2(lst,k,direction='left'):
    if direction == 'left':
        for num in range(k):
            lst.append(lst[0])
            lst.pop(0)
    elif direction == 'right':
        for num in range(k):
            lst.insert(0,lst[-1])
            lst.pop()
    return lst

# Question 3
# a
def sum_of_sq(n):
    sum = 0
    for num in range(1,n):
        sum += num**2
    return sum

# b
def sum_of_sq_advanced(n):
    return sum([num**2 for num in range(1,n)]

# c
def sum_of_sq_odd(n):
    sum = 0
    for num in range(1,n):
        if num%2 == 1:
            sum += num**2
    return sum

# d
def sum_of_sq_odd_advanced(n):
    return sum([num**2 for num in range(1,n) if num%2==1])
