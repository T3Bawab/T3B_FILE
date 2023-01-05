gg = open('headers.txt','r').read().splitlines()

for k in gg :
    c1 = k.split(':')[0]
    c2 = k.split(': ')[1]
    with open('autput.txt','a') as ggg :
        ggg.write(f"'{c1}': '{c2}',\n")
