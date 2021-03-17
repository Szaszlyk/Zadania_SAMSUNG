def fibonacci_sequence(number_of_arguments):
    fibonacci_sequence = []
    while len(fibonacci_sequence) < number_of_arguments:
        if len(fibonacci_sequence) == 0:
            fibonacci_sequence.append(0)
        elif len(fibonacci_sequence) == 1:
            fibonacci_sequence.append(1)
        else:
            new_argument = fibonacci_sequence[len(fibonacci_sequence) - 1] + fibonacci_sequence[len(fibonacci_sequence) - 2]
            fibonacci_sequence.append(new_argument)

    print(f"fib({number_of_arguments}) # {fibonacci_sequence}")


number_of_arguments = int(input("Podaj liczbe argumentow ciagu: "))

fibonacci_sequence(number_of_arguments)
