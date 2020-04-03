file_obj = open("files.txt", "wt")
print("This is a temp file ", file=file_obj)
file_obj.write("Second line")
file_obj.close()

try:
    fout = open('files.txt', 'xt')
    fout.write('added')
except FileExistsError:
    print('files.txt already exists!')