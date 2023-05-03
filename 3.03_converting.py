def fahrenheit_to_celsuis(temperature):
    return(temperature-32)*5/9

def kilometers_to_meters(kilometers):
    return(kilometers)*1000

def meters_to_yards(meters):
    return(meters)*1.09

def yards_to_feet(yards):
    return(yards)*3

def feet_to_inches(feet):
    return(feet)*12

print(kilometers_to_meters(37))
print(feet_to_inches(yards_to_feet(50)))
print(yards_to_feet(meters_to_yards(12)))
print(feet_to_inches(yards_to_feet(25)))
print(yards_to_feet(meters_to_yards(kilometers_to_meters(18))))
print(feet_to_inches(yards_to_feet(meters_to_yards(87))))