def read_fasta(filename):
    seq = ""
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq


def at_content(seq):
    a = seq.count("A")
    t = seq.count("T")
    at = (a + t) / len(seq) * 100
    return at

sequence = read_fasta("data/sequence.fasta")
print(sequence)
print("AT content: " + at_content(sequence))