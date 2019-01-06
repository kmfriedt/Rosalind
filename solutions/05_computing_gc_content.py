from Rosalind.iotools import read_fasta
from Rosalind.genetools import gc_content 

def solve(dataset):
    max_name = None 
    max_content = -1 
    
    for name, seq in read_fasta(dataset):
        current_content = gc_content(seq)
        if current_content > max_content:
            max_content = current_content
            max_name = name 
    
    max_content = max_content *100 

    return f'{max_name}\n{max_content}'