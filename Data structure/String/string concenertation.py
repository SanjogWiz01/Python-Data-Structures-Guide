s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  #string concatenation
print(s1 * 3)  #string repetition
print("lo" in s1)  #substring check
print("z" not in s1)  #substring absence check
print(len(s1))  #length of the string
print(s1.upper())  #convert to uppercase
print(s2.lower())  #convert to lowercase
print(s1.capitalize())  #capitalize first letter
print(s1.find("e"))  #find index of substring
print(s1.count("l"))  #count occurrences of substring
print('\n')
print(s1[1:4])  #slicing
print(s2[-3:])  #negative indexing slicing

print(s1.strip())  #remove leading/trailing whitespace
print(s1.replace("l", "x"))  #replace substring
print(s1.split("e"))  #split string by substring
print(s1.startswith("He"))  #check if string starts with substring

print(s2.endswith("ld"))  #check if string ends with substring
print(s1.isalpha())  #check if all characters are alphabetic
print(s1.isdigit())  #check if all characters are digits
print(s1.isalnum())  #check if all characters are alphanumeric
print(s1.swapcase())  #swap case of characters
print(s1.center(20, '*'))  #center string with padding
print(s1.encode())  #encode string to bytes
print(s1.format())  #string formatting
print(s1.title())  #title case
print(s1.zfill(10))  #pad string with zeros
print(s1.partition("l"))  #partition string at substring
print(s1.rfind("l"))  #find last occurrence of substring
print(s1.rsplit("l"))  #split string from the right
print(s1.lstrip())  #remove leading whitespace
print(s1.rstrip())  #remove trailing whitespace
print(s1.translate(str.maketrans("Helo", "Jxxy")))
print(s1.islower())  #check if all characters are lowercase
print(s1.isupper())  #check if all characters are uppercase
print(s1.isspace())  #check if all characters are whitespace
print(s1.encode('utf-8'))  #encode string to utf-8 bytes
print(s1.expandtabs(4))  #expand tabs to spaces
print(s1.removeprefix("He"))  #remove prefix
print(s1.removesuffix("lo"))  #remove suffix
print(s1.casefold())  #case insensitive comparison
print(s1.isprintable())  #check if all characters are printable
print(s1.maketrans("Helo", "Jxxy"))  #create translation table
print(s1.partition("l"))  #partition string at first occurrence
print(s1.rpartition("l"))  #partition string at last occurrence
print(s1.encode('ascii', 'ignore'))  #encode to ascii, ignore errors
print(s1.isidentifier())  #check if string is a valid identifier
print(s1.isnumeric())  #check if all characters are numeric
print(s1.isdecimal())  #check if all characters are decimal
print(s1.join(["A", "B", "C"]))  #join iterable with string
print(s1.removeprefix("He"))  #remove prefix
print(s1.removesuffix("lo"))  #remove suffix
print(s1.casefold())  #case insensitive comparison
print(s1.isprintable())  #check if all characters are printable
print(s1.maketrans("Helo", "Jxxy"))  #create translation table
print(s1.partition("l"))  #partition string at first occurrence
print(s1.rpartition("l"))  #partition string at last occurrence
print(s1.encode('ascii', 'ignore'))  #encode to ascii, ignore errors
print(s1.isidentifier())  #check if string is a valid identifier
print(s1.isnumeric())  #check if all characters are numeric
print(s1.isdecimal())  #check if all characters are decimal
print(s1.join(["A", "B", "C"]))  #join iterable with string
print(s1.removeprefix("He"))  #remove prefix