with open('textfile.txt', 'w') as file:
    file.write('\n'.join(iter(input, '')))
    file = open('textfile.txt', 'a')
file.write(' world!')
file.close()
