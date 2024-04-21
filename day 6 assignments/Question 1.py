class Painting:
    def calculatePaintingCost(self):
        pass
class FlatPainting(Painting):
    def __init__(self, noOfRooms):
        self.noOfRooms = noOfRooms
    def calculatePaintingCost(self):
        return self.noOfRooms * 10000
class BuildingPainting(Painting):
    def __init__(self, noOfFlats):
        self.noOfFlats = noOfFlats
    def calculatePaintingCost(self):
        return self.noOfFlats * 25000
flat_painting = FlatPainting(5)
flat_cost = flat_painting.calculatePaintingCost()
print("Flat Painting Cost:", flat_cost)
building_painting = BuildingPainting(2)
building_cost = building_painting.calculatePaintingCost()
print("Building Painting Cost:", building_cost)