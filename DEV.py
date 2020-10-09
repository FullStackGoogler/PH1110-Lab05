#Lab #5 Python Code, ezzhou

#Mass of Cart (kg)
mCart1 = 500
mCart2 = 499.94
mDEV = 0.0001 #assuming cart was measured with a triple beam balance

#Collision Type
collision = "Elastic"

#Initial Velocity of Cart1 (m/s)
Vi1 = 0
Vi1DEV = 0.002
#Initial Velocity of Cart2 (m/s)
Vi2 = 0.358
Vi2DEV = 0.003

#Final Velocity of Cart1 (m/s)
Vf1 = 0.282
Vf1DEV = 0.020
#Final Velocity of Cart2 (m/s)
Vf2 = -0.024
Vf2DEV = 0.008

#Initial Momentum of Cart 1 (kgm/s)
Pi1 = round(Vi1 * mCart1, 3)
Pi1DEV = round(Pi1 * (mDEV/mCart1), 3)
#Initial Momentum of Cart 2 (kgm/s)
Pi2 = round(Vi2 * mCart2, 3)
Pi2DEV = round(Pi2 * (Vi2DEV/Vi2 + mDEV/mCart2), 3)

#Final Momentum of Cart 1 (kgm/s)
Pf1 = round(Vf1 * mCart1, 3)
Pf1DEV = round(Pf1 * (Vf1DEV/Vf1 + mDEV/mCart1), 3)
#Final Momentum of Cart 2 (kgm/s)
Pf2 = round(Vf2 * mCart2, 3)
Pf2DEV = round(Pf2 * (Vf2DEV/Vf2 + mDEV/mCart2), 3)

#Initial Kinetic Energy of Cart 1 (J) --------------------------> Double Check if KEDEV should be V^2 or just V
KEi1 = round(0.5 * mCart1 * (Vi1 ** 2), 3)
KEi1DEV = round(KEi1 * (mDEV/mCart1), 3)
#Initial Kinetic Energy of Cart 2 (J)
KEi2 = round(0.5 * mCart2 * (Vi2 ** 2), 3)
KEi2DEV = round(KEi2 * (mDEV/mCart2 + Vi2DEV/Vi2), 3)

#Final Kinetic Energy of Cart 1 (J)
KEf1 = round(0.5 * mCart1 * (Vf1 ** 2), 3)
KEf1DEV = round(KEf1 * (mDEV/mCart1 + Vf1DEV/Vf1), 3)
#Final Kinetic Energy of Cart 2 (J)
KEf2 = round(0.5 * mCart2 * (Vf2 ** 2), 3)
KEf2DEV = round(KEf2 * (mDEV/mCart2 + Vf2DEV/Vf2), 3)

#

#Print Results
print(collision, "collision data:")
print("Initial Momentum of Cart 1 was:", Pi1, "kgm/s, +/-", Pi1DEV, "kgm/s.")
print("Initial Momentum of Cart 2 was:", Pi2, "kgm/s, +/-", Pi2DEV, "kgm/s.")
print("Final Momentum of Cart 1 was  :", Pf1, "kgm/s, +/-", Pf1DEV, "kgm/s.")
print("Final Momentum of Cart 2 was  :", Pf2, "kgm/s, +/-", Pf2DEV, "kgm/s.")
print()
print("Initial Kinetic Energy of Cart 1 was:", KEi1, "J, +/-", KEi1DEV, "J.")
print("Initial Kinetic Energy of Cart 2 was:", KEi2, "J, +/-", KEi2DEV, "J.")
print("Final Kinetic Energy of Cart 1 was  :", KEf1, "J, +/-", KEf1DEV, "J.")
print("Final Kinetic Energy of Cart 2 was  :", KEf2, "J, +/-", KEf2DEV, "J.")
print()
print("The change in Momentum was:", 
