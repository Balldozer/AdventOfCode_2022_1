#Star 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
#Star 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

kcal_per_elf = {}
kcal = 0

with open("text.txt", "r") as file:             #Open text.txt file with the number of kcal the elves are carrying

        for x in range(1,9999):                 #Iterate through the total of kcal per elf

            for y in range(1, 9999):            #Iterate through the list of kcal per snack
                line = file.readline()          #Read file line per line and store value in "line"
                line = line.strip()             #Strip eventual spaces

                if line != "":                  #Count the kcal if line is not blank
                    kcal += int(line)
                else:                           #Store the kcal in dictionary and skip the line if line is blank
                    kcal_per_elf[x] = kcal
                    kcal = 0
                    break

top1_elf = max(kcal_per_elf.values())           #Get max value of dictionary

del kcal_per_elf[max(kcal_per_elf, key=kcal_per_elf.get)]       #Delete max value of dictionary
top2_elf = max(kcal_per_elf.values())                           #The top 2 elf has now the highest value in dictionary

del kcal_per_elf[max(kcal_per_elf, key=kcal_per_elf.get)]       #Delete max value of dictionary
top3_elf = max(kcal_per_elf.values())                           #The top 3 elf has now the highest value in dictionary

top3_total = top1_elf + top2_elf + top3_elf                     #Count sum of top 3 elves

print(top1_elf)                                    #Answer Star 1
print(top3_total)                                  #Answer Star 2