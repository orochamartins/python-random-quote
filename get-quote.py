import random
def primary():
  f = open("quotes.txt", "r")
  quotes = f.readlines()
  f.close()
  
  f = open("quotes.txt", "a")
  f.write(f"\nThis is line number {len(quotes) + 1}")
  f.close()

  last = len(quotes)
  randomlist = random.sample(range(0, last), 2)

  print(quotes[randomlist[0]], end = "")
  print(quotes[randomlist[1]], end = "")

if __name__== "__main__":
  primary()
