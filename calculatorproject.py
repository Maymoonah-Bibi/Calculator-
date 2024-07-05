#  making calculators by taking inputs from user 
def calculator(a,b,operator):
    if operator== "+":
        addition =a+b
        print( "Sum of a and b is : ",addition )
    elif operator== "-":
        difference =a-b
        print( "Difference of a and b is : ",difference )
    elif operator== "*":
        product =a*b
        print( "Product of a and b is : ",product )
    elif operator== "/":
        division =a/b
        print( "Divisionof a and b is : ",division  )
    else :
        print("this is invalid operator ")

 # hwre we have taken inputs from user for numbers 
a= float( input ("enter number for a :"))
b= float( input ("enter number for b :"))

# here we have taken inputs for each operator from user 
operator=input ("write any one operator from (sum , difference, product, division:")
calculator(a,b,operator)



