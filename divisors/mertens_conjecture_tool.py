import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def divisors(n):
    divisors = []
    for i in range(2, n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors


def is_prime(n):
    assert type(n) is int
    if n < 2:
        return False
    if len(divisors(n)) == 1:
        return True
    else:
        return False


def factorize(n):
    primes = [i for i in range(n+1) if is_prime(i)]
    factors = []
    for p in primes:
        if n == 1:
            break
        power = 0
        while n%p == 0:
            power += 1
            n = n/p
        if power > 0:
            factors.append((p, power))
    return factors


@st.cache
def mu(n):
    """Mertens Function.

    Args:
        n (int)

    Returns:
        int: -1 if n has odd number of prime factors
            (and each has power 1), 1 if n has even number of prime
            factors (and each has power 1), 0 if n has prime factors
            in power higher than 1.
    """
    if mu == 1:
        return 1

    factors = factorize(n)
    assert len(factors) != 0

    if any([f[1] > 1 for f in factors]):
        return 0
    elif len(factors) % 2 == 0:
        return 1
    else:
        return -1


st.header("Marten's Conjecture")

st.write('Let mu(n) be a function on integers. Its output be defined '
         'as follows: it is -1 if n has odd number of prime factors '
         '(and each has power 1), 1 if n has even number of prime factors '
         '(and each has power 1), 0 if n has prime factors in power higher '
         'than 1.'
)

st.write("Merten's conjecture (disproved) is that absolute value of "
         "sum of mu's up to mu(n) is less then or equal to sqrt(n).")

n = st.slider('n', 2, 1000)

nums = [1]
mu_sums = [1]
for i in range(2, n+1):
    nums.append(i)
    mu_sums.append(mu_sums[-1]+mu(i))

fig, ax = plt.subplots()
ax.plot(nums, mu_sums)
ax.plot([0] + nums, np.sqrt([0] + nums), color='orange')
ax.plot([0] + nums, -np.sqrt([0] + nums), color='orange')
ax.plot([0, n], [0, 0], color='black')

st.pyplot(fig)