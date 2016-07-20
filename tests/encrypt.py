import os

algorithm = "aes-256-cbc"
infile = os.path.abspath("python-mem/text")
outfile = os.path.abspath("python-mem/text.crypto")

os.system("openssl {} -nosalt -nopad -in {} -out {} -pass pass:password".format(algorithm, infile, outfile))
