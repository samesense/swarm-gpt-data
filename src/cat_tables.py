import os
import sys
import pathlib
            
def write_file(afile, fout):
    with open(afile) as f:
        f.readline()
        for line in f:
            print(line.strip(), file=fout)

def write_header(afile, fout):
    with open(afile) as f:
        for line in f:
            print(line.strip(), file=fout)

adir, out = sys.argv[1:]
adir = pathlib.Path(adir)
i = 0
with open(out, 'w') as fout:
    for afile in os.listdir(adir):
        i += 1
        if i == 1:
            write_header(adir / afile, fout)
        else:
            write_file(adir / afile, fout)

