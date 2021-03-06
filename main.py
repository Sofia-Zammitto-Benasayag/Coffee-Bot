# Define your functions
def coffee_bot():
  print("Welcome to the World's Best Coffee!")

  size = get_size()
  drink_type = get_drink_type()
  get_coffee_temp()
  get_cup_type()
  get_extra_order()
  
  print('Alright, that\'s a {} {}!'.format(size, drink_type))
  name = input('Can I get your name please? \n>')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name)) 

   

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == "a":
    return "Small"
  if res == "b":
    return "medium"
  if res == "c":
    return "large"    
  else: 
    print_message()
    return get_size()  

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")  

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")  

  if res == "a":
    return "brewed coffee"
  elif res == "b":
    return "mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type() 

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  
  if res == "a":
    return "latte"
  elif res == "b":
    return "non-fat latte"
  elif res == "c":
    return "soy latte"      
  else: 
    print_message()
    return order_latte() 

def get_coffee_temp():
   res = input("Hot or iced? \n[a] Hot \n[b] Iced \n> ") 
   if res == "a":
     return "Hot"
   elif res == "b":
     return "Iced"
   else:
     print_message()
     return get_coffee_temp()    

def get_cup_type():
  res = input("Would you like a reusuable cup or a plastic one? \n[a] Reusuable (+ $1.50) \n[b] Plastic (free) \n> ")     
  if res == "a":
    return "Reusuable"
  elif res == "b":
    return "Plastic"
  else:
    print_message()
    return get_cup_type()

def get_extra_order():
  res = input("Would you like something to go along with your beverage? \n[a] Additional drink \n[b] A snack \n[c] No, I'm good \n> ")
  if res == "a":
    return coffee_bot()
  elif res == "b":
    return 
  elif res == "c":
    return 
  else:
    print_message()
    return get_extra_order()  
    
  



   

# Call coffee_bot()!
coffee_bot()
