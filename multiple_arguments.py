def varargs(arg1, *args):
    for a in args:
    	print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)
