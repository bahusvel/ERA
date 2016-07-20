
input_file = open("python-mem/text", "rb")
output_file = open("text.page","wb")

input_file.seek(0x118000)
output_file.write(input_file.read(4096))

input_file.close()
output_file.close()