
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

def hangmanp1(words):
  wrongletters = ""
  tries = int(argv[3])
  hword = "_"*int(argv[2])
  word1 = word_bank1(words)

  while tries > 0 and  word1 != hword:
    print(hword)
    print(f'missed letters: {wrongletters} ({tries} chances left)')

    attempt = input("Enter your guess: ")

    if attempt in word1:
      lword = list(hword)

      for i in range(len(word1)):
        if attempt == word1[i]:
          lword.insert(i,attempt)
          lword.pop(i + 1)
      hword = ""
      
      for i in lword:
        hword += i
    
    wrongletters = wrongletters + attempt + " "
    tries -= 1

  if word1 == hword:
    print(f'You guessed the word: {word1}.')
  else:
    print(f'You lost after {argv[3]} wrong chances.')
      
  




from sys import argv
def debug_print(s):
  if len(argv) > 4:
    print(s)

def run():
  return

if __name__ == '__main__':
  run()
