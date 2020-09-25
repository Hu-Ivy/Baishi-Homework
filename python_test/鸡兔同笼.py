def rabit_chiken(number, legs):
    for n_rabit in range(1, number + 1):
        n_chicken = number - n_rabit
        if 4 * n_rabit + 2 * n_chicken == 90:
            return n_rabit, n_chicken
n_rabit, n_chicken=rabit_chiken(30,90)
print(n_rabit, n_chicken)