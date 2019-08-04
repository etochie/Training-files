phone = input('Phone(1-4): ')
words = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for wr in phone:
    output += words.get(wr, 'NONE') + (' ')
print(output)
