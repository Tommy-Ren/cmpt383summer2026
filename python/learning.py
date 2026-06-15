import time

def abc_puzzle():
    solutions = [(a, b, c) for a in range(1, 10)
                           for b in range(1, 10)
                           if a != b
                           for c in range(1, 10)
                           if a != b and b != c and a != c
                           if a*100 + b*1 + c < c*100 + b *10 + a*1
                           if len(set(str((a * 100 + b * 10 + c) + (c * 100 + b * 10 + a)))) == 1]

    print(solutions)
    print(f"Number of solutions: {len(solutions)}")

def walrus_operator():
    def get_score(s):
        return sum(ord(c) for c in s)

    all_names = ['Bob', 'Alice', 'Charlie', 'Bev']

    high_scores = [(n, score)
                   for n in all_names
                   if (score := get_score(n)) % 5 != 0  # walrus operator used here
                   ]
    print(high_scores)

def using_zip():
    lst1 = [1, 2, 3, 4]
    lst2 = [5, 6, 7]

    # zip return a zip object, not a list
    merge_pairs = list(zip(lst1, lst2))
    sum_list = [x + y for x, y in zip(lst1, lst2)]
    merge_list =  [x + y for x in lst1
                         for y in lst2]
    print(merge_pairs)
    print(sum_list)
    print(merge_list)

def adjacent_element():
    s = [10, 20, 30, 40]
    # s[1:] = [20, 30, 40]

    pairs = list(zip(s, s[1:]))
    print(pairs)

def all_usage():
    print(all([0]))
    print(all([1]))
    print(all([0, 1]))
    print(all([1, 1]))
    print(all(list("abc")))

def unpacking_operator():
    def f(a, b, c):
        return a + b + c
    print(f(1, 2, 3))
    # the "*" means
    print(f(*[1, 2, 3]))

def transpose():
    matrix = [[1, 2], [3, 4], [5, 6]]
    transposed = [list(row) for row in zip(*matrix)]
    print(transposed)

def enumerate_function():
    lst = ['a', 'b', 'c']
    for a, b in enumerate(lst):
        print(a, b)

def iterators():
    class Letters:
        def __init__(self, s):
            self.s = s
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.s):
                self.index += 1
                return self.s[self.index - 1]
            else:
                raise StopIteration

    letters = Letters("cat")
    print(next(letters))  # 'c'
    print(next(letters))  # 'a'
    print(next(letters))  # 't'
    # print(next(letters))
    # any object that has an __iter__ method is iterable

def reversed_function():
    class My_reversed:
        def __init__(self, lst):
            self.lst = lst
            self.index = len(lst) - 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= 0:
                self.index -= 1
                return self.lst[self.index + 1]
            else:
                raise StopIteration

        def __reversed__(self):
            return self.lst

    my_reversed = My_reversed([1, 2, 3, 4])
    for i in my_reversed:
        print(i)

    for i in reversed(my_reversed):
        print(i)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def next_prime(n):
    """Returns the next prime number after n."""
    while True:
        n += 1
        if is_prime(n):
            return n

def prime_example():
    # Primes use next_prime linking all primes
    class Primes:
        def __init__(self):
            self.value = 1

        def __iter__(self):
            return self

        def __next__(self):
            self.value = next_prime(self.value)
            return self.value
    class Primes_less_than:
        def __init__(self, max):
            self.max = max
            self.primes = Primes()

        def __iter__(self):
            return self

        def __next__(self):
            p = next(self.primes)
            if p < self.max:
                return p
            else:
                raise StopIteration
    def primes_less_than(n):
        return [p for p in Primes_less_than(n)]

def generator_function():
    # simple_steps() is what we called generator function
    # yield is like return, it returns a value and then remembers what line of code it is on and the values of variables
    # When __next__ is called, the function continues from the line after the last yield
    def enumerate_gen(lst):
        index = 0
        while index < len(lst):
            yield index, lst[index]
            index += 1

    for a, b in enumerate_gen(["a", "b", "c", "d"]):
        print(a, b)
    def reversed_gen(lst):
        index = len(lst) - 1
        while index >= 0:
            yield lst[index]
            index -= 1
    for d in reversed_gen([1, 2, 3, 4]):
        print(d)

    # generator uses lazy evaluation, so no need to worry run infinitely.
    def prime_gen():
        n = 2
        while True:
            yield n
            n = next_prime(n)
    primes = prime_gen()
    prime = next(primes)
    while prime < 100:
        print(prime)
        prime = next(primes)

def closure_example():
    # closure is an object that acts like a function, but also has an environment of variables that persist after the
    # function returns
    def adder(n):
        def adder2(x):
            return x + n
        return adder2
    add3 = adder(3)
    print(add3(4))  # 7
    add5 = adder(5)
    print(add5(4))  # 9
    print(add3(add5(2)))  # 10

    def counter_obj():
        n = 0
        def tik():
            nonlocal n
            n += 1
            return n
        return tik

    counter = counter_obj()
    print(counter())  # 1
    print(counter())  # 2
    print(counter())  # 3

def decorators_example():

    def make_timed_function(f):
        # decorator is a function that takes another function, wraps some extra code around it (to extend its behavior)
        # and returns the new "decorated" function
        def timed_function(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()
            print(f"{f.__name__} taken: {end_time - start_time} seconds")
            return result
        return timed_function

    def make_hi_bye(f):
        def hi_bye(*args, **kwargs):
            print(f'{f.__name__} say hi')
            result = f(*args, **kwargs)
            print(f'{f.__name__} say bye')
            return result
        return hi_bye

    # Python read bottom-up but Execution Top-Down
    @make_timed_function
    @make_hi_bye
    def do_laundry(who, duration):
        print(f"{who} is doing laundry ... ")
        time.sleep(duration)
        print(f"{who}'s laundry is done")

    # use decorator
    do_laundry("Tommy", 1)

    # not use decorator
    # timed_do_laundry = make_timed_function(do_laundry)
    # timed_do_laundry()

def multi_parameters_example():
    def universal_catcher(*args, **kwargs):
        print(f"args caught: {args}")
        print(f"kwargs caught: {kwargs}")
    # Passing 3 positional arguments and 2 keyword arguments
    universal_catcher("Apple", "Banana", "Cherry", color="Red", size="Large")

def context_managers():
    return

def match_statement():
    return

# abc_puzzle()
# walrus_operator()
# using_zip()
# adjacent_element()
# all_usage()
# unpacking_operator()
# transpose()
enumerate_function()
# iterators()
# reversed_function()
# prime_example()
# generator_function()
# closure_example()
# decorators_example()
# multi_parameters_example()

# NOT IN QUIZ
# context_managers()
# match_statement()
