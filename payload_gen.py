import os
import time

print('Log in please...')

file = 'd.sh'
with open (file, 'w') as download_file:
    download_file.write('#!/bin/bash\necho "Loggin please"\nsleep 15\nfirefox https://www.hackthebox.com/login\n\n')
writeups = '' 
for i in range(283, 469):
    
    writeups += ' https://www.hackthebox.com/home/machines/writeup/'+str(i)

    #os.system('chromium --no-sandbox '+ writeups +'&')
    
    if (i % 10 == 0):
        with open('d.sh', 'a') as download_file:
            download_file.write('\nfirefox'+ writeups +'&\nsleep 20\n')
        
        writeups = ''
