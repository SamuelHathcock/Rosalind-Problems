# DNA Toolkit testing file
from DNAToolkit import *
from utilities import colored

data = "ACCGGGGGGGTCTGCTAGTGTGTCGCTTACGTAGACCGGCTTATAAAAAAA"

print(colored(f'\nSequence: {data}\n'))
print(colored(f'Sequence Length: {len(data)}\n'))
print(colored(f'Nucleotide Frequency: {countNucFrequency(data)}\n'))

print(colored(f'DNA/RNA Transcription: {transcription(data)}\n'))

print(colored(f'Reverse Complement {reverse_complement(data)}\n'))

print(colored(f'GC Content: {gc_content(data)}%\n'))

print(colored(f'GC Content in subsection k=5: {gc_content_subsec(data, k=5)}\n'))

