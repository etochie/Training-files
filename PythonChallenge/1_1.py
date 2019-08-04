text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
res = []
alp = 'abcdefghijklmnopqrstuvwxyz'


def podmena(x):
    for i in alp:
        if x == 'y':
            return 'a'
        if x == 'z':
            return 'b'
        if i == x:
            return alp[alp.index(i) + 2]
        if x == ' ':
            return x
        else:
            continue


for j in 'map':
    res.append(podmena(j))

for r in res:
    print(r, end='')


