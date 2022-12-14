#!/usr/bin/env python3

# f = open('script.sh', 'w')
# f.write("#!/usr/bin/env bash\n")
# f.write("echo \"Witaj świecie Astrydy\"\n")
# f.close()

# f = open('script.sh', 'r')
# text = f.read()
# print(text)

# print(text.split())

# for line in open("script.sh"): print(line)

#Binary files
#zapisywanie danych binarnych
import struct

# packed = struct.pack('>i4sh', 7, b'spam', 8)
# print(packed)
# file = open("data.bin", "wb")
# file.write(packed)
# file.close()

data = open("data.bin", "rb").read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>i4sh', data))