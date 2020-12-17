from sys import argv

def debug_print(k,v):
  if len(argv) > 4:
    print(f'{k}:{v}')

def get_word():
  with open(argv[1]) as words:
    word1 = list()

    for i in words:
      if len(i) - 1 == int(argv[2]):
        word2 = i.strip('\n')
        word1.append(word2)
  return word1

def criteria(i):
  return i.count('_')

def sort_dict(wdict):
  lkey = (max(wdict,key = wdict.get))
  lvalue = wdict[lkey]
  sdict = dict()

  for i in range(lvalue + 1):
    blanks = list()
    
    for c in wdict:
      if wdict[c] == i:
        blanks.append(c)
    
    blanks.sort(key = criteria)
    s3 = list()

    for c in blanks:
      s2 = list()
      number = c.count('_')

      for blank in blanks:
        if blank.count('_') == number:
          s2.append(blank)
      s2.sort()
      s3 += s2

    for c in s3:
      sdict[c] = i
  return sdict

def run():
  words = get_word()
  wrong = list()
  attempts = 0
  blank = list()

  for i in range(int(argv[2])):
    blank.append('_')

  blanks = ''.join(blank)

  if len(argv) > 4:
    print(f'{len(words)} words left.')

  print(f'{blanks}')
  print(f'missed letters: ({int(argv[3]) - attempts} chances left)')

  while attempts < int(argv[3]) and blanks.count('_') != 0:
    wvalue = dict()
    wwords = dict()
    letter = input('Enter your guess: ')

    for word in words:
      blank = list()

      for i in range(int(argv[2])):
        blank.append('_')

      tblanks = blanks
      tlist = list(tblanks)
      count = 0
      position = list()

      for c in word:
        count += 1

        if c == letter:
          if len(position) == 0:
            position.append(word.index(c))
          else:
            position.append(count - 1)

      if len(position) > 0:
        for i in position:
          del tlist[i]
          tlist.insert(i,letter)
        tblanks = ''.join(tlist)

      if tblanks not in wvalue:
        wvalue[tblanks] = 1
        wwords[tblanks] = [word]
      else:
        wvalue[tblanks] += 1
        wwords[tblanks] += [word]
      
    pick = max(wvalue,key = wvalue.get)

    if pick == blanks:
      if letter not in blanks:
        if letter not in wrong:
          wrong.append(letter)
          attempts += 1

    blanks = pick
    words = wwords[pick]
    sorted_dict = sort_dict(wvalue)

    for k,v in sorted_dict.items():
      debug_print(k,v)
    if blanks.count('_') == 0:
      print(f'\nYou guessed the word: {blanks}')
      return
    if attempts == int(argv[3]):
      print(f'\nYou lost after {argv[3]} wrong guesses.')
      return
    if len(argv) > 4:
      print(f'\n{wvalue[pick]} words left.')
      print(f'{blanks}')
    else:
      print(f'\n{blanks}')
    print(f"missed letters: {' '.join(wrong)} ({int(argv[3]) - attempts} chances left)")
  return

if __name__ == '__main__':
  run()
