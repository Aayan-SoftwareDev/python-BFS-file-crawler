from collections import deque
from os import listdir
from os.path import isfile, join

def algorithm(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    print(f"{search_queue} ##")
    while search_queue:
        dir = search_queue.popleft()
        print(f"{dir} ##")
        for file in sorted(listdir(dir)):
            print(f"{file} ##")
            fullpath = join(dir, file)
            print(f"{fullpath} ##")
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)
