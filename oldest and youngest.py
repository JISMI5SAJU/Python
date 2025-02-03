# Input the ages of three people from the user

age1 = int(input("Enter age of the first person: "))
age2 = int(input("Enter age of the second person: "))
age3 = int(input("Enter age of the third person: "))

# Determine the oldest and youngest among them

if age1 >= age2 and age1 >= age3:
   oldest = age1
   if age2 <= age3:
       youngest = age2
   else:
       youngest = age3
elif age2 >= age1 and age2 >= age3:
   oldest = age2
   if age1 <= age3:
       youngest = age1
   else:
       youngest = age3
else:
   oldest = age3
   if age1 <= age2:
       youngest = age1
   else:
       youngest = age2

# Display the results

print(f"The oldest person is {oldest} years old.")
print(f"The youngest person is {youngest} years old.")
