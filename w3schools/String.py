a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.lower()) #  returns the string in lower case
print(a.upper())
print(a.replace("H", "J")) #replaces a string with another string
print(a.split(",")) # returns ['Hello', ' World!']

#combine strings and numbers
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print(len(txt))

