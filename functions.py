#function with no return 
def display(name , age , profession , grade):
    print(f'my name is {name} and age is {age}. i am {profession} in {grade}')

display('shahid',33,'student','BSCS')

#function with return 
def display(name , age , profession , grade):
    return(f'my name is {name} and age is {age}. i am {profession} in {grade}')

data=display('shahid',33,'student','BSCS')
print(data)