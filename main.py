#functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  print(size)

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  return res 

# calls
coffee_bot()