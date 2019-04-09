original = raw_input("Whats your name: ")
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"