import entropy

input_file = open("../python-mem/text.crypto", "rb")
count = 1
while True:
	data = input_file.read(4096)
	if len(data) != 4096:
		break
	print("Page {}:{}".format(count, entropy.shannon_entropy(data)))
	count += 1


