"""
FASTA format file generated with DNA sequences of random lengths.
"""

import random

def generate_random_sequence(length):
    bases = "ACGT"
    return ''.join(random.choice(bases) for _ in range(length))

def generate_random_fasta_file(num_sequences, max_length, file_path):
    with open(file_path, "w") as file:
        for i in range(num_sequences):
            sequence_length = random.randint(50, max_length)
            sequence = generate_random_sequence(sequence_length)

            file.write(f'>Sequence{i+1}\n')
            file.write(f'{sequence}\n')

num_sequences = 50
max_sequence_length = 100

fasta_file_path = "randomly_generated_sequence.fasta"
generate_random_fasta_file(num_sequences, max_sequence_length, fasta_file_path)

print(f"{num_sequences} random DNA sequences with random lengths have been saved to {fasta_file_path}.")