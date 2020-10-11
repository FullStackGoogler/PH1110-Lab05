#Lab #5 Python Code, ezzhou
#Calculated assuming movement to the right of the track is positive, and left negative.

#Mass of Cart (kg)
mCart1 = #mass of cart 1
mCart2 = #mass of cart 2
mDEV = 0.0001 #assuming cart was measured with a triple beam balance

#Collision Type
collision = #collision type (Elastic or Inelastic)

#Initial Velocity of Cart1 (m/s)
Vi1 = #mean value
Vi1DEV = #standard deviation value
#Initial Velocity of Cart2 (m/s)
Vi2 = #mean value
Vi2DEV = #standard deviation value

#Final Velocity of Cart1 (m/s)
Vf1 = #mean value
Vf1DEV = #standard deviation value
#Final Velocity of Cart2 (m/s)
Vf2 = -#mean value, negative because motion sensor on opposite side
Vf2DEV = #standard deviation value

#Initial Momentum of Cart 1 (kgm/s)
Pi1 = round(Vi1 * mCart1, 3)
Pi1DEV = round(Pi1 * (mDEV/mCart1), 3) #Vi1 is 0, left out to avoid an DIV/0 error
#Initial Momentum of Cart 2 (kgm/s)
Pi2 = round(Vi2 * mCart2, 3)
Pi2DEV = round(Pi2 * (Vi2DEV/Vi2 + mDEV/mCart2), 3)

#Final Momentum of Cart 1 (kgm/s)
Pf1 = round(Vf1 * mCart1, 3)
Pf1DEV = round(Pf1 * (Vf1DEV/Vf1 + mDEV/mCart1), 3)
#Final Momentum of Cart 2 (kgm/s)
Pf2 = round(Vf2 * mCart2, 3)
Pf2DEV = round(Pf2 * (Vf2DEV/Vf2 + mDEV/mCart2), 3)

#Initial Kinetic Energy of Cart 1 (J)
KEi1 = round(0.5 * mCart1 * (Vi1 ** 2), 3)
KEi1DEV = round(KEi1 * (mDEV/mCart1), 3) #Vi1 is 0, left out to avoid an DIV/0 error
#Initial Kinetic Energy of Cart 2 (J)
KEi2 = round(0.5 * mCart2 * (Vi2 ** 2), 3)
KEi2DEV = round(KEi2 * (mDEV/mCart2 + Vi2DEV/(Vi2 ** 2)), 3)

#Final Kinetic Energy of Cart 1 (J)
KEf1 = round(0.5 * mCart1 * (Vf1 ** 2), 3)
KEf1DEV = round(KEf1 * (mDEV/mCart1 + Vf1DEV/Vf1), 3)
#Final Kinetic Energy of Cart 2 (J)
KEf2 = round(0.5 * mCart2 * (Vf2 ** 2), 3)
KEf2DEV = round(KEf2 * (mDEV/mCart2 + Vf2DEV/(Vf2 ** 2)), 3)

#Change in Momentum (kgm/s)
dP = round((Pf1+ Pf2) - (Pi1 + Pi2), 3)
dPDEV = round(Pi1DEV + Pi2DEV + Pf1DEV + Pf2DEV, 3)

#Change in Kinetic Energy (J)
dKE = round((KEf1 + KEf2) - (KEi1 + KEi2), 3)
dKEDEV = round(KEi1DEV + KEi2DEV + KEf1DEV + KEf2DEV, 3)

#Print Results
print(collision, "collision data:")
print("Initial Momentum of Cart 1 was:", Pi1, "kgm/s, ±", Pi1DEV, "kgm/s.")
print("Initial Momentum of Cart 2 was:", Pi2, "kgm/s, ±", Pi2DEV, "kgm/s.")
print("Final Momentum of Cart 1 was  :", Pf1, "kgm/s, ±", Pf1DEV, "kgm/s.")
print("Final Momentum of Cart 2 was  :", Pf2, "kgm/s, ±", Pf2DEV, "kgm/s.")
print()
print("Initial Kinetic Energy of Cart 1 was:", KEi1, "J, ±", KEi1DEV, "J.")
print("Initial Kinetic Energy of Cart 2 was:", KEi2, "J, ±", KEi2DEV, "J.")
print("Final Kinetic Energy of Cart 1 was  :", KEf1, "J, ±", KEf1DEV, "J.")
print("Final Kinetic Energy of Cart 2 was  :", KEf2, "J, ±", KEf2DEV, "J.")
print()
print("The change in Momentum was:", dP, "kgm/s, ±", dPDEV, "kgm/s.")
print()
print("The change in Kinetic Energy was:", dKE, "J, ±", dKEDEV, "J.")
