import matplotlib.pyplot as plt
import random
import math
import time

sign = lambda x: -1 if x < 0 else 1

def get_random_array(n, min=1, max = 50):
    ans = []
    for i in range(n):
        ans.append(random.randint(min, max))
    return ans

def randfloat(a, b, d=10):
    return random.randint(a*d, b*d)/d
    
def find_zero(t, a, b, eps = 1e-6):
    while True:
        m = (a + b) / 2
        if abs(t(m)) < eps:
            break
        if t(a) > 0 and t(b) > 0:
            break
        elif sign(t(a)) != sign(t(m)):
            b = m
        else:
            a = m 
    return m
    



    a = get_random_array(60)
print(f'a: {a}')
plt.hist(a, bins=10, orientation="vertical") # or horisotal








fig, ax = plt.subplots(1, 1) 
while True: 
    x = [randfloat(-10, 10) for i in range(16*4)]
    sin_y = [math.sin(t) for t in x]
    ax.stackplot(x, sin_y)
    for i in range(len(x)-1):
        ax.plot([x[i], x[i+1]], [sin_y[i], sin_y[i+1]], color="orange")
    plt.plot(x, sin_y)
    plt.show()