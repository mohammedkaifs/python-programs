def remove_and_split(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()

this = "   kaif is a good   "
n= remove_and_split(this,"kaif")
print(n)


# def multiplication(n):
    