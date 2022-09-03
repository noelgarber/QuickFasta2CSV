#Convert FASTA to a simple 2-value CSV with headers and sequences

import pandas as pd

filename = input("Enter the filename to convert:  ")

output_lists = []
append_needed = False

with open(filename, "r") as file: 
	for line in file.readlines(): 
		line = line.rstrip("\n")
		print(line)
		if len(line) == 0: 
			continue
		if line[0] == ">": 
			if append_needed: 
				output_lists.append(header_sequence_list)
				header_sequence_list = []
			last_header = line[1:]
			header_sequence_list = [last_header, ""]
		else: 
			current_sequence = header_sequence_list[1]
			new_sequence = current_sequence + line
			header_sequence_list[1] = new_sequence
			append_needed = True

output_lines = []

for item in output_lists: 
	current_line = item[0] + "," + item[1] + "\n"
	output_lines.append(current_line)

export_filename = filename.split(".")
export_filename = export_filename[0] + ".csv"

with open(export_filename, "w") as output_file: 
	output_file.writelines(output_lines)