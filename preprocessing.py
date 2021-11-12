file_name = "partsupp.tbl"

output_name = "partsupp-final.tbl"

input_file = open(file_name,'r')
output_file = open(output_name,'w')
for line in input_file:
    output_file.write(line[0:-2]+"\n")

input_file.close()

output_file.close()
