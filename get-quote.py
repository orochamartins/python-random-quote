import random
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 17
  randomlist = random.sample(range(0, last), 2)

  print(quotes[randomlist[0]], end = "" )
  print(quotes[randomlist[1]])

if __name__== "__main__":
  primary()
