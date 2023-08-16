"""
This module contains functions that reads the file, identifies the sequences
and calculates their lengths, and generates a report summarizing the sequence lengths.
"""

def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        current_seq = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_seq = line[1:]
                sequences[current_seq] = ''
            else:
                sequences[current_seq] += line
    return sequences

def calculate_sequence_lengths(sequences):
    lengths = {}
    for seq_id, sequence in sequences.items():
        lengths[seq_id] = len(sequence)
    return lengths

def generate_length_report(sequence_lengths):
    total_sequences = len(sequence_lengths)
    min_length = min(sequence_lengths.values())
    max_length = max(sequence_lengths.values())
    avg_length = sum(sequence_lengths.values()) / total_sequences

    print("Genomic Data Length Report")
    print("--------------------------")
    print(f"Total Sequences: {total_sequences}")
    print(f"Minimum Length: {min_length}")
    print(f"Maximum Length: {max_length}")
    print(f"Average Length: {avg_length:.2f}")
    print("\nLength Histogram:")
    for seq_id, length in sequence_lengths.items():
        print(f"{seq_id}: {'*' * (length // 10)}")

if __name__ == "__main__":
    fasta_file = "./randomly_generated_sequence.fasta"
    sequences = parse_fasta(fasta_file)
    sequence_lengths = calculate_sequence_lengths(sequences)
    generate_length_report(sequence_lengths)