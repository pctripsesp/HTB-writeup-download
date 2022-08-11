## SET THIS VALUES
first = 439
last = 469
file = 'download.sh'

print('Log in please...')

with open (file, 'w') as download_file:
    download_file.write('#!/bin/bash\necho "Loggin please"\nsleep 15\nfirefox https://www.hackthebox.com/login\n\n')

writeups = '' 

for i in range(first, last+1):
    
    writeups += ' https://www.hackthebox.com/home/machines/writeup/'+str(i)

    if (i % 10 == 0):
        with open(file, 'a') as download_file:
            download_file.write('\nfirefox'+ writeups +'&\nsleep 20\n')
        
        writeups = ''

with open(file, 'a') as download_file:
    download_file.write('\nfirefox'+ writeups +'&\nsleep 20\n')
