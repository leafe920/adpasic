f = open('rawfile/rawfile.txt', 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    eachl = line.split(' ')
    print(eachl[0])
