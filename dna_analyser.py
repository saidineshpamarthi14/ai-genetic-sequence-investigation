
def analyse_dna(sequence):
    sequence = sequence.upper().strip()

    valid_bases = {"A", "T", "G", "C"}

    if not sequence:
        print("Error: DNA sequence is empty.")
        return

    if not set(sequence).issubset(valid_bases):
        print("Error: Invalid DNA characters.")
        return

    total = len(sequence)

    print("DNA Sequence:", sequence)
    print("Sequence Length:", total)

    for base in "ATGC":
        count = sequence.count(base)
        percentage = (count / total) * 100

        print(f"{base}: {count} occurrences ({percentage:.2f}%)")


if __name__ == "__main__":
    sample_sequence = "ATGCGTACCTGAACTG"
    analyse_dna(sample_sequence)
