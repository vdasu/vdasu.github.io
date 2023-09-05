import math

def log_decay(const, t, iter):
    return t / math.log(const + iter)

R = 50
L = 0.02 #1.0
T = R * L

delta = 0.02

def accept_prob(delta, t):
    return 1 / math.exp(delta / t)

t1 = log_decay(2, T, 1)
a1 = accept_prob(0.02, t1)

print(t1, a1)