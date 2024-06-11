import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(f"randnums {randnums}")
    append_random_numbers(randnums)
    print(f"randnums {randnums}")
    append_random_numbers(randnums,3)
    print(f"randnums {randnums}")

def append_random_numbers(numbers_list, quantity = 1):
    for i in range(0,quantity+1):
        numbers_list.append(round(random.uniform(0,100),1))

main()