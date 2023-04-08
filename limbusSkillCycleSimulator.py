import random

SKILL_BAG = (1, 1, 1, 2, 2, 3)

def drawBag(bag, drawCount, baseBag = SKILL_BAG):
	if len(bag) <= drawCount:
		results = bag
		results, newbag = drawBag(list(baseBag), drawCount - len(bag))
		return results + bag, newbag
	else:
		random.shuffle(bag) # can't be bothered to read random's documentation so we're just gonna shuffle and pick
		results = [bag[-i] for i in range (1, drawCount + 1)]
		bag = bag[0:-drawCount]
		return results, bag

def cycleLogicTemplate(takeCondition):
	def func(top, bottom):
		if takeCondition(top):
			return (None, bottom, top)
		elif takeCondition(bottom):
			return (None, top, bottom)
		else:
			return (None, None, top)
	return func		

THREES_ONLY = cycleLogicTemplate(lambda x: x == 3) #If there's a 3, take it. Useful for Seven Ryoshu
TWOS_ONLY = cycleLogicTemplate(lambda x: x == 2) #If there's a 2, take it. Useful for Shi Ishmael/Hong Lu.
THROW_OUT_ONES = cycleLogicTemplate(lambda x: x != 1) #If there's anything that isn't a 1, take it. Default behavior.

def simulation(trials = 10000, cycleLogic = THREES_ONLY, cycleLogicName = " with only threes"):
	totals = [0, 0, 0]
	currentBag = list(SKILL_BAG)
	bottom = None
	top = None
	for i in range(0, trials):
		if bottom == None:
			[top, bottom], currentBag = drawBag(currentBag, 2)
		else: #If bottom is none, top is none because old skills fall to the bottom
			[top], currentBag = drawBag(currentBag, 1)
		top, bottom, use = cycleLogic(top, bottom)
		totals[use - 1] += 1
	print("Out of %s trials%s, Skill 1 was used %s times, Skill 2 was used %s times, and Skill 3 was used %s times" % 
				(trials, cycleLogicName, totals[0], totals[1], totals[2]))

simulation(1000000, THREES_ONLY, " with as many Skill 3s as possible")
simulation(1000000, TWOS_ONLY, " with as many Skill 2s as possible")
simulation(1000000, THROW_OUT_ONES, " with as many Skill 2s and 3s as possible")
