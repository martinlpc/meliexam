from typing import Set
from fastapi import FastAPI

app = FastAPI()

def is_mutant(dna) -> bool:
    dnaMatrix = [list(row) for row in dna] 
    matrixLen = len(dnaMatrix)
    
    # Checking rows
    for row in dnaMatrix:
        print(row)
        if check_dna_sequence(row):
            return True
    print("--^ matrix ^--")
    
    # Checking columns
    for col in range(matrixLen):
        col_seq = [dnaMatrix[row][col] for row in range(matrixLen)] # Transpose matrix (col -> row)
        print(col_seq)
        if check_dna_sequence(col_seq):
           return True
    print("--^ transposed matrix ^--")
    
    # Checking diagonals
    for i in range(matrixLen - 3):
        # Main diagonals
        diag = [dnaMatrix[i+j][j] for j in range(matrixLen - i)]
        print(diag)
        print("--^ diagonal ^--")
        if check_dna_sequence(diag):
            return True
        
        diag = [dnaMatrix[j][i+j] for j in range(matrixLen - i)]
        print(diag)
        print("--^ diagonal ^--")
        if check_dna_sequence(diag):
            return True
        
        # Secondary diagonals
        diag = [dnaMatrix[j][matrixLen - 1 - j - i] for j in range(matrixLen - i)]
        print(diag)
        print("--^ diagonal ^--")
        if check_dna_sequence(diag):
            return True
        
        diag = [dnaMatrix[i + j][matrixLen - 1 - j] for j in range(matrixLen - i)]
        print(diag)
        print("--^ diagonal ^--")
        if check_dna_sequence(diag):
            return True
        
    return False

def check_dna_sequence(sequence) -> bool:
    """Checks if there is 4 consecutive nitrogenous bases in a sequence"""
    count = 1
    for i in range(1,len(sequence)):
        if sequence[i] == sequence[i-1]:
            count += 1
            
            if count == 4: 
                return True
            
        else:
            count = 1
    
    return False

mutantDna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

result = is_mutant(mutantDna)

print(f"Mutant detected?: {result}")