# File: add_line_number_to_url.py

# Open the input and output files
input_file = 'allurls'  # Input file containing URLs
output_file = 'urls_with_line_number.txt'  # Output file for modified URLs

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line_number, url in enumerate(infile, 1):  # Start line numbers from 1
        # Strip any newline character and append the line number at the end of the URL
        modified_url = f"{url.strip()}?line={line_number}"
        # Write the modified URL to the output file
        outfile.write(modified_url + '\n')

print(f"URLs with line numbers have been written to {output_file}")
