file_obj = open("files.txt", "wt")
print("This is a temp file", file=file_obj)
file_obj.write("Second line")
file_obj.close()

try:
    fout = open('files.txt', 'xt')
    fout.write('added')
except FileExistsError:
    print('files.txt already exists!')

file_obj = open('files.txt', 'rt')
while True:
    line = file_obj.readline();
    if not line:
        break;
    print("Line: ", line)
file_obj.close()

file_obj = open('files.txt', 'rt')
lines = file_obj.readlines();
print("Lines: ", lines)
file_obj.close()
for line in lines:
    print("Line...", line)