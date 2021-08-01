'''
Given two strings s and t of equal length, the Hamming distance
between s and t, denoted dH(s,t), is the number of 
corresponding symbols that differ in s and t. 
'''

def hamming_distance(s: str, t: str):
    count = 0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            count+=1
    return count
    
s = "CCCTACATTCGACACCGGAGGAGGTGTGGGTACGGCGTTGCGATTTGTGATTTAATGCGATTTTAAACGAGGCTTTGCCCAACTATGGCATTAAAACTCCTCTGCGAACAACATGAATGCGTCATGCCTAGCGATGGCTTATCGAAATCGTTTAGTAGTCCGAGGCGACTGGTTTTAAACAAGTAGGATTTAGCTAAGTCATGGTCAGGGGGATGCTACCGTGTCCAGGTCAAGCGGGGGGGATATCGGACTGACGTGCTAGGCAATGTGTGACAAAACTGACGTTTATTTGCGGTACATGATCCCTAGTACTGGGTCGCAAGTGGATCTGGATCCACCTTGGATAATTTGATATAACGTACTTGTGCCAAAAGTTCGACTTCATGGGTGATTCTGAACCGACGAGACAAAGTGAGACGTAACAACACGACACGCAGCCGCGGGACCTGTGAACATTCTTCCAACATTGTGATTGATACGCGGCAGCTGTCGGGTTCGGGGAGCCATGGAGCCTGTCCCGTCATACTAACCAATAATCCAGCTCGAGCTGGTGCATATCAGTCTAACCAACTCGTTCGAGCCTGAGGGGACGATGCGAACCTAGTGAATGCTCCTTGTGGGGAGCAGGGCGGGATACCATGACGGTGTGTCCATGGAGTCGGACGGCGCCATGCACTCCTACGGTCCGATTAAACAAGTCATCGGTGAGTCTGTGTCGTTAATTGGGGCCGACCGCCAGGTAATGGTGATGTCTCTATTGCTGTCAATCCGTAGCGTGTTAAGGTAAGCCTATGTCTCGAGCAAAGTGCCTAGACAAGGCAGTGATTAAACATACCACCACAAGATTTATCGTTCTCCGCGGCGGTAGTGTTTTGTTACCACGGCCGGCTCCGGTTGTACGGCTGTAATACAGGGGGTGTTTCTTGTCGCAGACGAGTAGGTCAGGACTCCGGGGGAATCTCTTGCCCTTACCAAAGAA"
t = "CGCGCAATTAGAGCCGGGGGGACATGTGGAAGGGCACTTTGGCTGTGAGATGGTTGACCAGCCTCGATCGGGCGGTGGCCCTTTATATGACTCCCTCCTCGCCCGGAGACACATGAATTCGGCCTGCCTAGAGAGGGACGAACGTAGTGGCGAAGTACTTCCTGCCGAAACTACTTAAACTATGAGCACTTCAAGCAGTCGACGAGATTCCGGTGCTTTCGACTATACGTCCCGCAGCCACGATAGTGTACACACTCTCGATACTATCTTCGATACGACAGACCTATTGTATCGTTGAACGCACCCGAGTCTCGCGGTCAAATTGAACCTAGGTCTTCCCTTGAAAATCATTTTTACTCTACCTTGGCTTAAAAGGCGACTTCATCGGTAAATTGAGACAGGGAGGACAAGTGGTCGGCTGAGTGCAGGCCAAAAACCTCGGGCGCCTGTCTAGTGACTTCGCAAGCAGGCCTTAGTTACCAGTATCCTCCCCCCCCTCCTCGAGCTTACACCGGGCCTCGCCTAAAAACCAAAAGTTCACGACCAGGTACTTCATCTAGTATAAGCGAAATCGTTCGATCCCTAGAATCCGATTCATATCTACCGGCTGACCGACTTTGAGTGATGGCGTGTTACTCAAGCCACCGGCTCAAACGTGCAGTTCTACGCAAAACCATTTAGCGGTCTGAAGGCGCTACTTAGCGCCACCGCTGTGTCGGCCTGTACCGGCAACCTCGTGCTACGGATGCTTTGCCTATTTCGACCACGCTCTCTCGCGTACCGTGCAGGCTCTTTGTCAAGATAGAAGCATGTTCGATGCTGCCAAGAACCAGTTCACCGAGAGATTTATCGTCCGCCACCTTGAACGTCTCGCCATACCGTGGCCTGCCCCCGCTACATTTCCCTAAGATTGGCGGTGGTGATCGTCGCGGGAGCGTAGGACACAGCATCAGGGCGAAACCATGCCATAGGGATTCAG"

print(hamming_distance(s, t))