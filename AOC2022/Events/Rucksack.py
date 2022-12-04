from re import I


class Rucksack(object):
    def __init__(self, compartments):
        self.parse(compartments)

    def parse(self, compartments):
        result = 0
        badgeResult = 0
        elfGroups = []
        index = 1
        for compartment in compartments.split("\n"):
            elfGroups.append(compartment)
            firstCompartment = slice(0, len(compartment)//2)
            secondCompartment = slice(len(compartment)//2, len(compartment))
            commonItem = ''.join(set(compartment[firstCompartment]).intersection(compartment[secondCompartment]))
            result += self.LetterPosition(commonItem)
            
            if(index == 3):
                commonBadge = ''.join(set.intersection(*map(set,elfGroups)))
                badgeResult += self.LetterPosition(commonBadge)
                elfGroups.clear()
                index = 0
            index += 1
        print("The sum of the priorities of item that are twice in the same rucksack is:", result)
        print("The sum of the priorities of badge is:", badgeResult)
        return

    def LetterPosition(self, item):
        result = 0
        if(item.isupper()):
            commonItemLower = item.lower()
            result += ord(commonItemLower) - 70
        else:
            result += ord(item) - 96
        return result




