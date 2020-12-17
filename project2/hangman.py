from sys import argv

def get_words(filename):
  words = []

  with open(filename) as fin:
    for line in fin:
      words.append(line.strip())
  return words

def word_bank1(words):
  for word in words:
    if len(word) == int(argv[2]):
      word1 = word
  return word1






def debug_print(s):
  if len(argv) > 4:
    print(s)

def run():
  return

if __name__ == '__main__':
  run()
