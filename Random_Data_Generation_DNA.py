"""
FASTA format file generated with same lengths of DNA sequences."""


import random

def generate_random_sequences(length):
    bases = "ACGT"
    return ''.join(random.choice(bases) for _ in range(length))

def save_sequences_to_fasta(sequences, file_path):
    with open(file_path, "w") as file:
        for i, sequence in enumerate(sequences, start=1):
            file.write(f">Seuqnece{i}\n")
            file.write(f"{sequence}\n")


num_sequences = 50
sequence_length = 100

random_sequences = [generate_random_sequences(sequence_length) for _ in range(num_sequences)]
fasta_file_path = "generated_sequences.fasta"

save_sequences_to_fasta(random_sequences, fasta_file_path)
print(f"{num_sequences} random DNA sequences have been saved to '{fasta_file_path}'.")