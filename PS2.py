import argparse
import numpy as np
def main():
    parser = argparse.ArgumentParser()
    #use traceback
    parser.add_argument(dest='-s1', help="input first input file here")
    parser.add_argument(dest='-s2', help="input second input file here")
    parser.add_argument(dest='-m', help='input the matrix to be used')
    parser.add_argument(dest='-g', help='input the gap penalty to be used')
    parser.add_argument(dest='-o', help='input the output file')
    args = parser.parse_args()
                    
    matrix = open(args.m,'r')
    matrix = matrix.read()
    print(matrix)
    ##String temp = ""
    ##String matrixLine = ""
    ##last_line = none
    ##b = np.zeroShape(24)
    ###not sure if its none or null
    ##for line in matrix:
    ##    if not last_line = none && line.length()!=25:
    ##        temp = line
    ##        int i = 0
    ##        while(i<=temp.length() -2):
    ##            for a in temp:
    ##                if type(a) != class 'int':
    ##                    row_names.append(a)
    ##                    #need a row 00
    ##                else:
    ##                    matrixLine += a
    ##                    matrixLine += ','
    ##                    i++
    ##        if type(matrixLine[1] ) != class 'int':
    ##            blosum = np.Array[matrixLine]
    ##            column_names = blosum
    ##        else:
    ##            b.append(blosum)
    ##        #think about using pandas
    ##        #install numpy
    ##for i in matrix:
    ##    if type(i) == class 'int':
    ##        if i<0:
    ##            i = 0
    ##seq1 = open(args.-s1,'r')
    ##seq1 = seq1.readlines()[1:]
    ##seq2 = open(args.-s2,'r')
    ##seq2 = seq2.readlines()[1:]
    ##int alignScore = 0
    ##int maxLength = 0
    ##if seq1.length() != seq2.length():
    ##    if seq1.length()>seq2.length():
    ##        alignScore += (seq1.length()-seq2.length())*args.-o
    ##        maxLength = seq1.length()
    ##    if seq2.length()>seq1.length():
    ##        alignScore += (seq2.length() - seq1.length()) * args.-o
    ##        maxLength = seq2.length()
    ##else:
    ##    maxLength = seq1.length
    ##
    ###negative scores set to 0 - local alignment
    ###24 columns
    ##traceInfo = {}
    ##String temp = ""
    ##traceInfo[00] = 0
    ##int i = 0
    ##column = "0"
    ##row = "0"
    ##while i<maxLength:
    ##    char colNeeded = seq1[i]
    ##    char rowNeeded = seq2[i]
    ###read csv
    ###can also use pandas
    ###redo to a dictionary
    ##
main()    

