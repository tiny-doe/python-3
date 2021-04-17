#hello, you have hired me to make 2 functions generate the username and password for your company's employees
#i hope you're paying me well for this quality work you corpo

#username generator function
def username_generator(first_name, last_name):
  if len(first_name) >= 3 and len(last_name) >= 4:
    username = first_name[:3] + last_name[:4]
  elif len(first_name) < 3:
    username = first_name + last_name[:4]
  elif len(last_name) < 4:
    username = first_name[:3] + last_name
  else:
    username = first_name + last_name
  return username
#testing
print(username_generator("Zoe", "Steinbean"))

#password generator function
def password_generator(username):
  password = ""
  for letter in range(0, len(username)):
    password += username[letter - 1]
  return password
#testing
print(password_generator("ZoeStei"))
