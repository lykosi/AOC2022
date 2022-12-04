class CampCleanup(object):
    def __init__(self, assignments):
        self.parse(assignments)

    def parse(self, assignments):
        resultBetween = 0
        resultOverlap = 0
        for assignment in assignments.split("\n"):
            assignment = assignment.split(',')

            firstAssignment = list(map(int, assignment[0].split('-')))
            secondAssignment = list(map(int, assignment[1].split('-')))

            isBetweenSecondAssignment = self.isBetween(firstAssignment, secondAssignment)
            isBetweenFirstAssignment = self.isBetween(secondAssignment, firstAssignment)
            if(isBetweenSecondAssignment or isBetweenFirstAssignment):
                resultBetween += 1

            doOverlapSecondAssignment = self.doOverlap(firstAssignment, secondAssignment)
            doOverlapFirstAssignment = self.doOverlap(secondAssignment, firstAssignment)
            if(doOverlapSecondAssignment or doOverlapFirstAssignment):
                resultOverlap += 1

        print("The result of already affected sector is:", resultBetween)
        print("The result of overlaping sector is:", resultOverlap)
        return

    def isBetween(self, baseAssignment, verifiedAssignment):
        if(baseAssignment[0] <= verifiedAssignment[0] <= baseAssignment[1] and baseAssignment[0] <= verifiedAssignment[1] <= baseAssignment[1]):
            return True
        else:
            return False
        
    def doOverlap(self, baseAssignment, verifiedAssignment):
        if(baseAssignment[0] <= verifiedAssignment[0] <= baseAssignment[1] or baseAssignment[0] <= verifiedAssignment[1] <= baseAssignment[1]):
            return True
        else:
            return False







