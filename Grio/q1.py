# I started on this, then realized it was just like the game boggle
# So did some searching and found the following, which I modified slightly
# http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#746345
# the 5 digit primes is an excerpt from http://primes.utm.edu/lists/small/10000.txt

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def solve():
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            for result in extending(letter, ((x, y),)):
                yield result

def extending(prefix, path):
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result
    
def neighbors((x, y)):
    for nx in range(max(0, x-1), min(x+2, ncols)):
        for ny in range(max(0, y-1), min(y+2, nrows)):
            yield (nx, ny)

def FindPrime(grid_str):
   global grid, nrows, ncols, words, prefixes
 
   grid = list(chunkstring(str(grid_str), 5))
   nrows, ncols = len(grid), len(grid[0])

   words = set()
   f = open('5_digit_primes.txt')
   for word in f.read().split():
      words.add(word)
   prefixes = set(word[:i] for word in words
                  for i in range(2, len(word)+1))
   
   answer = set(word for word, path in solve())
   print answer
   print 'Found ' + str(len(answer)) + ' primes of length 5.'

