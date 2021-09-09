def do_twice(f,v):
    f(v)
    f(v)

#this part tests output
def print_twice(text): 
    print(text) 
    print(text) 

do_twice(print_twice,"this is it")

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

#this part tests output
do_four(print_twice,'Is this it?')
