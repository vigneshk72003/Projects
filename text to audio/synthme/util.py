PRONUNCIATION_CSV_PATH = "data/pronunciation.csv"

import csv, re

# Convert raw user input to a list of words
# TODO: convert numerical values to words
def tokenize(data):
	return re.findall(r"[\w']+|[.,!?;]", data.lower())

def get_pronunciation(word):
  with open(PRONUNCIATION_CSV_PATH, 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
      if word == row[0]:
        numbers = row[1].strip().split(' ')
        # map string to integers
        return list(map(int, numbers))
      