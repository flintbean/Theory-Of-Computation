import re  # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
import codecs

if __name__ == '__main__':
    # Exit if command line args entered incorrectly
    if len(sys.argv) != 2:
        print("usage: extract_links.py [input_file]")
        sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML file
f = codecs.open(filename, 'r', 'utf-8')

# TODO Set up regex
htmlReg = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

matches = []
# TODO Find links using regex, save in list called 'matches'
for line in f:
    line = line.rstrip()
    matchList = re.findall(htmlReg, line)
    if len(matchList) > 0:
        matches.append(matchList)
        print(matches)


# Check matches, print results
# TODO Read in links from answers.txt (hint...this is a CSV file),
# save in list called 'answer_data'

with open('answers.txt', newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',')
    for row in csv_data:
        answer_data = row

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len(matches) != len(answer_data):
    result = "Your regex found %i matches. There should be %i matches" % (
        len(matches), len(answer_data))
else:
    for i in range(len(answer_data)):
        if(matches[i] != answer_data[i]):
            result = "Mismatched link. Got %s but expected %s" % (
                matches[i], answer_data[i])
            break
print(result)
