
#COUNTING VOWELS

s = 'azcbobobegghakl'
print "Number of vowels:" , len(filter(lambda ch:ch.lower() in "aeiou",s))
