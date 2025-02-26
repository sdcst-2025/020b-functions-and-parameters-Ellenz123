#!python3

def sum(a,b):
    #inputs
    # a : float 
    # b : float
    # return value: returns the sum of the 2 numbers
    a=float(a)
    b=float(b)
    sum=a+b
    print(f"The sum of {a} and {b} is {sum}")
    return sum



if __name__ == "__main__":
    print("This is my program")
    #this should return a value of 7
    x = sum(3,4)
    assert x == 7

    #this should return a value of 12.5
    y = sum(11,1.5)
    assert y == 12.5

    assert sum(5,2) == 7
    assert sum(1,2) == 3
    assert sum(5,-32) == -27
    assert sum(5,2.5) == 7.5
    assert round(sum(5.1,2.3),1) == 7.4
    
