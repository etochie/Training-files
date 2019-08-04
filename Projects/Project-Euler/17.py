words_for_nums = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
}


def nums_to_words(num, dic):
    tmp = ''
    t = str(num)
    if dic.get(num):
        return dic[num]
    elif num < 20:
        return dic[int(t[1])] + 'teen'
    elif num < 100:
        tmp = num - int(t[1])
        return dic[tmp] + dic[int(t[1])]
    elif num < 1000:
        if t[1:3] == '00':
            return dic[int(t[0])] + 'hundred'
        else:
            return dic[int(t[0])] + 'hundredand' + nums_to_words(int(t[1:3]), words_for_nums)
    elif num == 1000:
        return 'onethousand'


s = 0
for i in range(1, 1001):
    s += len(nums_to_words(i, words_for_nums))
print(s)

print(nums_to_words(342, words_for_nums))



