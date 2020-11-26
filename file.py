# f = open("test.txt")    # sama dengan mode 'r' atau 'rt'
# f = open("test.txt", 'w') # mode tulis
# f = open("ly.png", 'r+b') # membaca dan menulis dalam mode biner

with open("test.txt", 'w') as f:
    f.write("The new first line\n")
    f.write("The new second line\n")
    f.write("The new third line\n")