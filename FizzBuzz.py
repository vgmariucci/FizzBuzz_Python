
def FizzBuzz():

    for i in range(1,100):
        
        if(i % 3 == 0 and not(i % 15 == 0)): 
            
            print("Fizz: ", i)
        
        if (i % 5 == 0 and not(i % 15 == 0)): 
            
            print("Buzz: ", i)
            

        if(i % 15 == 0): 
            
            print("FizzBuzz: ", i)
        
        if(not(((i % 3 == 0 and not(i % 15 == 0))) or (i % 5 == 0 and not(i % 15 == 0)) or (i % 15 == 0))):
            
            print("Count:",i)
    

FizzBuzz()