# Question:- You are climbing a staircase. It takes n steps to reach the top. Each time you can either take 1 or 2 steps. In how many distinct ways csn you climb the top

def climbing(n):
    if n == 1:
        return n
    if n == 2:
        return 2

    two_back = 1
    one_back = 2

    for i in range(2, n):
        next_num = two_back + one_back
        two_back = one_back
        one_back = next_num

    return one_back

print(climbing(20))

# What we are doing is that we are adding the number of stairs to a new variable and then constantly updating the previous variable to do this in a continuous manner
