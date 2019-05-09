from __future__ import print_function
import sys

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

exclude = {
'about',
'above',
'be',
'up',
'you',
'your',
}

include = {
'association',
'uml',
'diagram',
'diagrams',
}

words = []
wordmap = {}

def fix(word):
  word = word.lower()
  while len(word) != 0 and not word[0].isalpha():
    word = word[1:]
  while len(word) != 0 and not word[-1].isalpha():
    word = word[:-1]
  return word

def solve(i):
  with open('tmp/' + str(i) + ".txt", 'r', errors='ignore') as f:
    for line in f:
      for word in line.split():
        word = fix(word)
        if not word.isalpha(): continue
        if len(word) < 2: continue
        if word in exclude: continue
        words.append(word)
        if word not in wordmap:
          wordmap[word] = []
        wordmap[word].append(i)

for i in range(1, 201):
  solve(i)

words = list(set(words))
words = sorted(words)

for i in words:
  if i not in include and len(sorted(list(set(wordmap[i])))) > 20:
    eprint(i)
    continue
  print(i, end=": ")
  print(sorted(list(set(wordmap[i]))))
