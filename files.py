import os
import os.path

with open('output.txt', 'w') as f:

    for current_dir, dirs, files in os.walk("./main"):
        temp = ''
        dirs.sort()
        if files:
            for file in files:
                if file[-3:] == '.py':
                    if current_dir != temp:
                        f.write('%s\n' % current_dir[2:])
                    temp = current_dir
