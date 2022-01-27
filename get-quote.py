import random 

def central():

  f = open("quotes.txt") # opens the quotes.txt file
  quotes = f.readlines() # reading all the lines into 'quotes' variable
  f.close() # closes the quotes.txt file

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  central()
