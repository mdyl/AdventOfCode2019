import math 

def getRocketModules(filename):
	fileInput = open(filename,"r")
	modules = []

	for module in fileInput:
		modules.append(module.rstrip())

	return modules

def determineModuleFuel(moduleMass):
	fuel = math.floor(moduleMass/3) - 2

	return fuel

def calculateModulesFuel(modules):
	totalFuel = 0

	for module in modules:
		totalFuel += determineModuleFuel(int(module))

	return totalFuel

def calculateTotalFuel(modules):
	totalFuel = 0

	for module in modules:
		fuel = determineModuleFuel(int(module))

		totalFuel += fuel

		while determineModuleFuel(fuel) > 0:
			totalFuel += determineModuleFuel(fuel)
			fuel = determineModuleFuel(fuel)

	return totalFuel


print("Part 1: " + str(calculateModulesFuel(getRocketModules("input.txt"))))

print("Part 2: " + str(calculateTotalFuel(getRocketModules("input.txt"))))