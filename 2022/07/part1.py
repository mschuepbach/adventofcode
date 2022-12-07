f = open("2022/07/input", "r")
lines = f.readlines()


class Directory:
    def __init__(self) -> None:
        self.name = ""
        self.parent: Directory = None
        self.subdirs = {}
        self.files = {}
        self.size = 0

def calcsize(dir: Directory) -> int:
    sum = 0
    for filesize in dir.files.values():
        sum += filesize
    for subdir in dir.subdirs.values():
        sum += calcsize(subdir)
    dir.size = sum
    return sum

def printdir(dir: Directory, level = 0):
    indentation = ' ' * 2 * level
    print(f"{indentation}- {dir.name} (dir, size={dir.size})")
    for file, size in dir.files.items():
        print(f"{indentation}  - {file} (file, size={size})")
    for subdir in dir.subdirs.values():
        printdir(subdir, level + 1)

def filterdir(dir: Directory):
    sum = 0
    if dir.size <= 100_000:
        sum += dir.size
    for subdir in dir.subdirs.values():
        sum += filterdir(subdir)
    return sum

root = Directory()
root.name = "/"
currentdir = root

for line in lines:
    if line.startswith("dir "):
        dirname = line[4:-1]
        newdir = Directory()
        newdir.name = dirname
        newdir.parent = currentdir
        currentdir.subdirs[dirname] = newdir
    elif line.startswith("$ cd "):
        newdir = line[5:-1]
        if newdir == "/":
            continue
        elif newdir == "..":
            currentdir = currentdir.parent
        else:
            currentdir = currentdir.subdirs[newdir]
    elif line.startswith("$ ls"):
        continue
    else:
        data = line.split(" ")
        filename = data[1][:-1]
        size = int(data[0])
        currentdir.files[filename] = size

calcsize(root)
printdir(root)
result = filterdir(root)
print(result)
