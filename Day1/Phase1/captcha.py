#!/usr/bin/python3

fh = open("input.txt", mode='r')
f_in = fh.read()
fh.close()

f_in = f_in.strip()

nseq = []

for i in f_in.split(' '):
    nseq.append(int(i))

mcnt = 0
scnt = 0

for i in range(len(nseq)):
    scnt = scnt + 1

    if nseq[i] < nseq[i-1]:
        scnt = 1

    if nseq[i] % 2 == 0 and nseq[i-1] % 2 == 0:
        scnt = 1

    if nseq[i] % 2 != 0 and nseq[i-1] % 2 != 0:
        scnt = 1

    if scnt > mcnt:
        mcnt = scnt

    print(nseq[i])

print("Max Length:", mcnt)