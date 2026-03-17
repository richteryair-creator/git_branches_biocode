def read_fasta(filename):
    seq = ""
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq

def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    gc = (g + c) / len(seq) * 100
    return gc

sequence = read_fasta("data/sequence.fasta")
print(sequence)
print("GC content:", gc_content(sequence))

def at_content(seq):
    a = seq.count("A")
    t = seq.count("T")
    at = (a + t) / len(seq) * 100
    return at

sequence = read_fasta("data/sequence.fasta")
print(sequence)
print("AT content: " + at_content(sequence))
