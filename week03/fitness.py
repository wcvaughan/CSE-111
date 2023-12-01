from datetime import datetime

"""
Work as a team to write a Python program named fitness.py that does the following:

Asks the user to enter four values:
gender
birthdate in this format: YYYY-MM-DD
weight in U.S. pounds
height in U.S. inches
Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
Converts inches to centimeters (1 in = 2.54 cm).
Calculates age, BMI, and BMR.
Prints age, weight in kg, height in cm, BMI, and BMR

"""

bmi = 0

bmr = 0

weight_kg = 0

height_cm = 0

age = 0

def main ():
    
    gender = input('What is your birth gender? (Male or Female)')

    birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
    
    weight = float(input('Please enter your weight in pounds: '))
    
    height = float(input('Please enter your height in inches: '))

    age = age_calc(birthday_str)

    weight_kg = kg_from_lb(weight)

    height_cm = cm_from_in(height)

    bmi = body_mass_index(weight_kg, height_cm)

    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    print(f'Your body mass index is {bmi} and your basal metabolic rate is {bmr}')

    pass

def age_calc(birthday_str):

    # Convert the input string to a datetime object
    try:
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

        # Get the current date
        current_date = datetime.now()

        # Calculate the age
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
    
    return age

def kg_from_lb(weight):

    weight_kg = weight * 0.45359237
    
    return weight_kg

def cm_from_in(height):

    height_cm = height * 2.54

    return height_cm

def body_mass_index(weight_kg, height_cm):

    bmi = (10000 * weight_kg) / (height_cm ** 2)

    return bmi

def basal_metabolic_rate(gender, weight_kg, height_cm, age):

    if gender.lower() == 'male':

        bmr = 88.362 + 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age

    elif gender.lower() == 'female':
        
        bmr = 447.593 + 9.247 * weight_kg + 3.098 * height_cm - 4.330 * age

    return bmr

main()