#!/usr/bin/python2.7 -tt

import sys

def Hello(name):
  if name == 'Alice' or name == 'Steve':
    name = name + '???'
  else:
    name = name + ' yay!'
  print 'Hello', name

def Cat(filename):
  f = open(filename, 'rU')
  text = f.read();
  print text
  f.close()

#Define a main() function that prints a little greeting.
def main():
  Cat(sys.argv[1])
 

# this is the standard boilerplate that call the main() function.
if __name__ == '__main__':
  main()
