def fibonacci_sequence(n):
    sequence = [0,1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
print(fibonacci_sequence(num_terms))
