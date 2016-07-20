import entropy
import hashlib

input_file = open("python-mem/text", "rb")
ENTROPY_THRESHOLD = 0.95
decrypted_map = {}

page_number = 1

while True:
	data = input_file.read(4096)
	if len(data) != 4096:
		break
	data_entropy = entropy.shannon_entropy(data)
	if data_entropy <= ENTROPY_THRESHOLD:
		print("Page {} is not encrypted ({})".format(page_number, data_entropy))
		hash = hashlib.md5()
		hash.update(data)
		hash_digest = hash.digest()
		if page_number in decrypted_map:
			if decrypted_map[page_number] != hash_digest:
				print("Updating page {} to {}".format(page_number, decrypted_map[page_number], hash.hexdigest()))
		else:
			print("Page {} found {}".format(page_number, hash.hexdigest()))
		decrypted_map[page_number] = hash_digest
	page_number += 1

