import sys,re,os,io

def clearBlankLine(file1,file2):
    for line in file1.readlines():
        if line == '\n':
            line = line.strip("\n")
        file2.write(line)

if __name__ == '__main__':

    fn = sys.argv[1]
    fn2 = sys.argv[2]

    fnum = int(fn2)

    fd = open(fn, 'r')
    fb = open(r'first.txt','w')

    count = len(open(fn,'rU').readlines())
    print count
    while 1:
        line = fd.readline()
        if not line:
            break
        if (len(line))>(fnum * 3):
            s0 = line[:(fnum*3)]
            fb.write(s0)
            fb.write('\n')
        else:
            continue

    fb.close()

    fb1 = open('first.txt', 'r')
    fb2 = open('last.txt', 'w')

    clearBlankLine(fb1,fb2)

    fb1.close()
    fb2.close()