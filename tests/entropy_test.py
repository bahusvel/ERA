import entropy

input_file = open("text.crypto", "rb")
data = input_file.read()

print("Shannon entropy is ", entropy.shannon_entropy(data))
