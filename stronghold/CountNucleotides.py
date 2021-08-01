
def countNucFrequency(seq: str):
    tmpfrq = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpfrq[nuc]+=1
    return tmpfrq

case = "TGGCGCGGACGCCCTTACCACGACCGCCTGACTTACGGTAAATGGTCGTGATACTTTGTCATACTGTGTTTGACGTAACGGCCTTCACACCGCGACGCTTTCCCGCTATCTTCAAACTATACATTATATCTAACCCCCGCGACCTAAAATGTATTAGCACCGACAGGGAGCGCAGTACTATCGAACGTATTGCTAAGCCCACGTCTTCACTCTAGTATTTAGAGTTATGAGATAAGCGGGCCCAGAACTTAGCACGAGCGAAAGTTCTTCTACGTTATACCAGGTATACGCGGTGCTTTCTCGCTAACAGGCGTTCGAAGAGGTTTTTCTCTCTTCACTGGACACGGAGTTCAAGCGCAGTTGGTCTACCCCTAACGCGCGCCCGACCTATGGAGAGCCGACGCCTGCTCCAACCCCGCACTGAGGACCAAAATGGCGCGTGATAGCTATGTGTCGCCCGTGCCGTACTCCTGAGTCTGAGCGTAAACATGCACCCTTGGCTCATGCCTCCATCTGGTTCGAAATGCTGTGGAAAGCGCCGGAAAGAGAACGATTTACTGGGGGCTATATCTCATTCGATGTCATATCTATAAGCGACATCACAGACCATCGATGTAAATAGCCCCGATTAAGGAAACTTGTCCACGTTGATACTTCAAGGTCTAATACTTGATACCAGCTGTCTTAACTGGGCCAAAATCCTCCAGGACGTTAACGTAACATATCCCCCCCGCCACAGGGCATTGGCGACATGAGACAGAAGCATCCGCATCCACAAGAATAGCAATGCTCACGATCACCATGATCCTCGTGGTACCCCAAGACTGAGTGGGTCCATTATCGGCAGTGTAATAAGGTCGTACCCACGTTTTTGCATGTCTTATCCGACCCTAGGATCTCCTGGCATGGGATGACGTTGAGTACACGATTCACCGTCATAACTTCATGGGAATGGAGCTGGGAAGGAGTTCACTTTTGAACA"
res = countNucFrequency(case)

print(' '.join(([str(val) for key, val in res.items()])))


