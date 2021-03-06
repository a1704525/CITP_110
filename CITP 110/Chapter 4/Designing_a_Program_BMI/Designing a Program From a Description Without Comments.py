#-------------------------------------------------------------------------------
#Program:       Designing a Program From a Desciption - BMI
#Programmer:    Gary Heisler
#Date:          9/1/2010
#               7/1/2011 - Revised for Python 3
#Abstract:      This program calculates the body mass index (BMI) for a user
#               and determines if the BMI indicates the user is underweight, 
#               overweight, or of optimal weight. 
#-------------------------------------------------------------------------------

#Define the main function
def main():
    print('This program calculates your BMI using your weight and height')
    
    weight = float(input('What is your weight (in pounds)? '))
    height = float(input('What is your height (in inches)? '))
    
    calculate_BMI(weight, height)
    
#Define the calculate_BMI function
def calculate_BMI(weight, height):
    
    BMI = weight * 703 / height ** 2
    print('Your BMI is ', format(BMI, '.2f'))
    
    if BMI < 18.5:
        print('You are underweight')
    elif BMI > 25:
        print('You are overweight')
    else:
        print('Your weight is optimal')
        
#call the main function
main()