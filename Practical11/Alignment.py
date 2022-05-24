import re
import os
import pandas as pd

human = open('DLX5_human.fa')
mouse = open('DLX5_mouse.fa')
random = open('RandomSeq.fa')

# os.chdir("C:/cygwin64/home/17847/IBI1_2021-22/IBI1_2021-22/Practical10")
# os.getcwd()
standard = pd.read_excel("BLOSUM.xlsx")
score1 = 0
score2 = 0
score3 = 0
a = 0
b = 0
c = 0
d = ''
table = dict(A=1, R=2, N=3, D=4, C=5, Q=6, E=7, G=8, H=9, I=10, L=11, K=12, M=13, F=14, P=15, S=16, T=17, W=18, Y=19,
             V=20, B=21, Z=22, X=23)
for human_line in human:
    if human_line.startswith('>'):
        next(mouse)
        next(random)
        continue
    else:
        d = d + human_line
        mouse_line = next(mouse)
        random_line = next(random)

        for i in range(len(human_line)):
            if human_line[i] != mouse_line[i]:
                score1 = score1 + standard.iloc[table[human_line[i]], table[mouse_line[i]]]
                a += 1
            if human_line[i] != random_line[i]:
                score2 = score2 + standard.iloc[table[human_line[i]], table[random_line[i]]]
                b += 1
            if mouse_line[i] != random_line[i]:
                score3 = score3 + standard.iloc[table[mouse_line[i]], table[random_line[i]]]
                c += 1
e = (len(d) - a) / len(d)
f = (len(d) - b) / len(d)
g = (len(d) - c) / len(d)
print('The alignment score of DLX5_human and DLX5_mouse is ' + str(
    score1) + ' and the percentage of identical amino acids is ' + str('{:.2%}'.format(e)))
print('The alignment score of DLX5_human and random sequence is ' + str(
    score2) + ' and the percentage of identical amino acids is ' + str('{:.2%}'.format(f)))
print('The alignment score of DLX5_mouse and random sequence is ' + str(
    score3) + ' and the percentage of identical amino acids is ' + str('{:.2%}'.format(g)))
