import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

text = open(input_file, "r")
text = ''.join([i for i in text]).replace(";", ",")
x = open(output_file,"w")
x.writelines(text)
x.close()
