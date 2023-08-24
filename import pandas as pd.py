import pandas as pd

data = {
    'Match': ['Mumbai', 'Delhi', 'Chennai', 'Indore', 'Mohali', 'Delhi'],
    'Location': ['India', 'England', 'India', 'England', 'Australia', 'India'],
    'Team 01': ['Sri Lanka', 'Australia', 'South Africa', 'Sri Lanka', 'South Africa', 'Australia'],
    'Team 02': ['India', 'England', 'South Africa', 'Sri Lanka', 'South Africa', 'Australia'],
    'Timing': ['DAY', 'DAY-NIGHT', 'DAY', 'DAY-NIGHT', 'DAY-NIGHT', 'DAY']
}

df = pd.DataFrame(data)

print("Enter your choice:")
print("1. List of all the matches of a Team")
print("2. List of Matches on a Location")
print("3. List of Matches based on timing.")

choice = int(input())

if choice == 1:
    team = input("Enter team name: ")
    print(df[(df['Team 01'] == team) | (df['Team 02'] == team)])
elif choice == 2:
    location = input("Enter location: ")
    print(df[df['Location'] == location])
elif choice == 3:
    timing = input("Enter timing: ")
    print(df[df['Timing'] == timing])
else:
    print("Invalid choice!")
