import sys

file = open("wasteland.txt", mode="rt", encoding="utf-8")
try:
    for line in file:
        sys.stdout.write(line)
finally:
    file.close()

# with block

with open("wasteland.txt", mode="rt", encoding="utf-8") as f:
    for line in f:
        sys.stdout.write(line.strip())
