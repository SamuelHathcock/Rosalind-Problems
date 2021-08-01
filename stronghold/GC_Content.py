


def FASTAfile_max_GCcontent(filePath: str):
    # Storing File Contents in a list
    FASTAfile = readFile(filePath)

    # Converting FASTA/List file data into a dictionary for Labels and Data {label: data}
    FASTAdict = FASTAfile_to_dict(FASTAfile)

    #Getting max gc_content of data and printing result to console.
    FASTA_GC_Content(FASTAdict)


def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]



def FASTAfile_to_dict(FASTAfile):
    """Converts a FASTA file to a dictionary, returns result"""
    FASTADict = {}
    for line in FASTAfile:
        if '>' in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line
    return FASTADict


def gc_content(seq):
    """GC Content in a DNA or RNA sequence"""
    return round( (seq.count('C') + seq.count('G')) / len(seq) * 100 , 6 )

def FASTA_GC_Content(seqs: dict):
    gc_max = 0.0
    max_label = ''
    for seq in seqs:
        temp = gc_content(seqs[seq])
        if temp > gc_max: 
            gc_max = temp
            max_label = seq
    print(max_label.replace('>', ''))
    print(gc_max)


if __name__ == '__main__':
    FASTAfile_max_GCcontent("test_data/rosalind_gc.txt")








    

