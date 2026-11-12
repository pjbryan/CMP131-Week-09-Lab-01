# PJ Bryan
# CMP-131-80230
# Week 09
# Lab 01
# Assignment 09
# 11/06/2026



# Kinetic energy function
def kineticEnergy(mass, velocity):
  return 1/2 * mass * velocity**2

# Main Function
def main():
  # Program table and dividers
  divider1 = "*******************"
  divider2 = "---------------------------"
  print ("KINETIC ENERGY", divider1)

  mass = float(input("Enter the object's mass in kilograms: "))
  velocity = float(input("Enter the object's velocity in meters per second: "))

  # Call the function and display the result
  joules = kineticEnergy(mass, velocity)

  print (divider2)
  print ("SUMMARY")
  print ("The object's mass in kilograms:", mass)
  print ("The object's velocity in meters per second:", velocity)
  print (f"The calculated kinetic energy: {joules:,.2f}")

# Calling the main function
main()
