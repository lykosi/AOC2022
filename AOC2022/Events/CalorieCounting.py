#https://adventofcode.com/2022/day/1
class CalorieCounting(object):
    def __init__(self, food):
        self.parse(food)
    
    def parse(self, food):
        caloriesMax = 0 #Maximum calories carried by an elf
        caloriesTop3 = [] #TOP 3 calories carried by elfs
        elfs = food.split("\n\n") #Split calories carried between elfs
        for elf in elfs:
            calories = elf.split("\n") #Split calories carried by an elf
            calories = sum([int(calorie) for calorie in calories]) #We sum it all

            if(calories > caloriesMax): #If the current is greater than the recorded, the current take place
                caloriesMax = calories 

            caloriesTop3.append(calories) #We add the current elf to the top 3
            for calorie in caloriesTop3:
                #If the top 3 is completed but the current elf is greater than the min of the top 3
                #The current elf take place
                if(len(caloriesTop3) >= 4 and calorie > min(caloriesTop3)):
                    caloriesTop3.remove(min(caloriesTop3))
            
        print("The most calories carried by an elf is:", caloriesMax)
        print("The top 3 calories carrier is:", caloriesTop3)
        print("The sum of those 3 is:", sum(caloriesTop3))
        return






