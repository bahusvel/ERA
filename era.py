import entropy
import hashlib

input_file = open("python-mem/text.crypto", "rb")
output_file = open("output.mem", "wb")
ENTROPY_THRESHOLD = 0.95
decrypted_map = {}
entropy_map = {}

page_number = 1


def insert_page(output_file, page_number, data):
	output_file.seek(page_number * 4096)
	output_file.write(data)


def upsert_page(page_number, data):
	hash = hashlib.md5()
	hash.update(data)
	hash_digest = hash.digest()
	if page_number in decrypted_map and decrypted_map[page_number] != hash_digest:
		# page is not new and has changed
		print("Updating page {} to {}".format(page_number, decrypted_map[page_number], hash.hexdigest()))
		insert_page(output_file, page_number, data)
		decrypted_map[page_number] = hash_digest
	else:
		# page is new
		print("Page {} found {}".format(page_number, hash.hexdigest()))
		insert_page(output_file, page_number, data)
		decrypted_map[page_number] = hash_digest


while True:
	data = input_file.read(4096)
	if len(data) != 4096:
		break
	data_entropy = entropy.shannon_entropy(data)

	if data_entropy <= ENTROPY_THRESHOLD:
		# page is below entropy threshold so it is most likely decrypted
		print("Page {} is not encrypted ({})".format(page_number, data_entropy))
		upsert_page(page_number, data)

	elif page_number in entropy_map and data_entropy < entropy_map[page_number]:
		# page entropy value has decreased, THIS IS QUESTIONABLE but should be better anyway
		print("Entropy for page {} decreased from {} to {}".format(page_number, entropy_map[page_number], data_entropy))
		upsert_page(page_number, data)

	elif page_number not in decrypted_map:
		# if the page is not decrypted yet update it anyway, to avoid false negatives
		insert_page(output_file, page_number, data)
	entropy_map[page_number] = data_entropy
	page_number += 1

output_file.close()
