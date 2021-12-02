class Solution:
    def __init__(self):
        reader = open('input.txt')
        boxes = reader.read().splitlines()
        self.boxes = boxes

    def wrappingPaperNeeded(self, box):
        dimensions = box.split("x")
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])
        sideLW = length * width
        sideLH = length * height
        sideWH = width * height

        surfaceArea = 2 * (sideLW + sideLH + sideWH)
        smallestFace = sideLW
        if sideLH < smallestFace:
            smallestFace = sideLH
        if sideWH < smallestFace:
            smallestFace = sideWH

        wrappingPaper = surfaceArea + smallestFace
        return wrappingPaper

    def ribbonNeeded(self, box):
        dimensions = box.split("x")
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])

        largestSide = length
        if width > largestSide:
            largestSide = width
        if height > largestSide:
            largestSide = height

        ribbonNeeded = length * width * height + 2 * (length + width + height - largestSide)
        return ribbonNeeded

    def partOne(self):
        totalPaper = 0
        for x in self.boxes:
            totalPaper = totalPaper + self.wrappingPaperNeeded(x)
        print("The answer to Day 1 part one is " + str(totalPaper))

    def partTwo(self):
        totalRibbon = 0
        for x in self.boxes:
            totalRibbon = totalRibbon + self.ribbonNeeded(x)
        print("The answer to Day 1 part two is " + str(totalRibbon))


sol = Solution()
sol.partOne()
sol.partTwo()
