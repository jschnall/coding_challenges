# Tested on the two code challenge text files
#
# Assumptions:
#
# -No particular time constraint was mentioned, but it did say the file could be quite large.
# I presume there is enough space to store each of the words and their frequency
# in a table, otherwise multiple passes, or writing to a file on disk may be necessary
#
# -It is not well defined what constitutes a "word".  I strip punctuation except for 
# apostrophes (we're, they'd, singers', etc.)
# Numbers are not counted as words.
# Hyphenated words count as two separate words

import operator
import re

def mostFreq(file):
   table = {}
   f = open(file)
   for line in f:
      words = re.findall(r"[^\W\d]+'?[^\W\d]?", line)
      for word in words:
         value = table.get(word)
         if value is None:
            table[word] = 1
	 else:
            table[word] = value + 1

   sorted_items = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
   for x in xrange(10):
      print sorted_items[x][0] + ' ' + str(sorted_items[x][1])
