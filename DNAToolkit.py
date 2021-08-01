# DNA Toolkit file
from collections import Counter
from structures import *

NUCLEOTIDES = ["A", "C", "G", "T"]
REVERSE_COMPLEMENT = {'A': 'T', 'T':'A', 'G': 'C', 'C': 'G'}




def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in NUCLEOTIDES:
            return False
    return tmpseq

def countNucFrequency(seq: str):
    """Counts the frequency each nucelotide occurs in a sequence"""
    tmpfrq = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpfrq[nuc]+=1
    return tmpfrq
    # return dict(collections.Counter(seq))

def transcription(seq: str):
    '''DNA -> RNA Transcription. Replaces Thymine with Uracil'''
    return seq.replace("T", "U")

def reverse_complement(seq: str):
    '''Swapping adenine with thymine, guanine with cytosine, and reversing the result'''
    # return ''.join([REVERSE_COMPLEMENT[nuc] for nuc in seq])[::-1]

    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    """GC COntent in a DNA or RNA sequence"""
    return round( (seq.count('C') + seq.count('G')) / len(seq) * 100 )

def gc_content_subsec(seq, k=20):
    """GC COntent of DNA/RNA sub-sequence length k. k=20 be default """
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i: i + k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    res = []
    for pos in range(init_pos, len(seq) - 2, 3):
        res.append( DNA_Codons[seq[pos:pos + 3]] )
    return res
    # return[DNA_Codons[ seq[pos:pos + 3]]for pos in range(init_pos, len(seq) - 2, 3)]


def codon_usage(seq, aminoacid):
    """Returns the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range (0, len(seq) - 2, 3):
        curr_amino = seq[i: i + 3]
        if DNA_Codons[curr_amino] == aminoacid:
            tmpList.append(curr_amino)

    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict


if __name__ == '__main__':
    data = 'ATAGACTAGATAGCATCCAGAGATATCCCTTTCAGACAGGATCAGACGCGAGACCTTGG'
    # print(translate_seq(data))
    # print(str.maketrans('ATCG', 'TAGC'))
    # print(str('A'))
    # print(gc_content(data))
    print(translate_seq(data ))
    print(codon_usage(data, "L"))
  



