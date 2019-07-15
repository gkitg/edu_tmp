import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        # for i in range(2, current_prime):
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
print(prime(1))
# cProfile.run('prime(10)')       # 0
# cProfile.run('prime(100)')      # 0.001
# cProfile.run('prime(1000)')     # 0.278
# cProfile.run('prime(2500)')     # 1.920
# cProfile.run('prime(5000)')     # 8.216
# cProfile.run('prime(10000)')


# 100 loops, best of 3: 20.4 usec per loop      10
# 100 loops, best of 3: 459 usec per loop       100
# 100 loops, best of 3: 9.37 msec per loop      1000
# 100 loops, best of 3: 203 msec per loop       10000
