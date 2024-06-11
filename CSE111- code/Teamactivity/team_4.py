import random
import textwrap

with open("Teamactivity/quotes.txt", "rt") as infile:
    
    string = infile.read()
    quotes = string.splitlines()

    num = int(input("How many quotes would you like? "))

    while num != 0:
        quote = random.choice(quotes)
        prin = textwrap.wrap(quote, 70)

        print()
        for line in prin:
            print(line)

        num -= 1