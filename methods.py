myDict = {
    "fast":"in quick manner",
    "Kaif":"a coder",
    "marks":{1,2,3},
    "anotherdict":{'Kaif':'player'},
    1:2
}

print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values()) #prints the values of the dictionary
print(myDict.items()) #prints the key,value for all the in  dictionary
print(myDict)

updateDict={
    "naruto":"Friend",
    "Kaif":"a programmer"
}
myDict.update(updateDict) #update the dictionary with the key value pairs from updateidct
print(myDict)


#difference between .get and mydict syntax
print(myDict.get("Kaif2")) #returns none as kaif2 is not present in dictionary
                        
#returns error as kaif2 is not present in dictionary
print(myDict["Kaif2"]
