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

def THREES_ONLY(top, bottom):
	#Useful for Seven Ryoshu
	if top == 3:
		(top, bottom, use) = (None, bottom, top)
	elif bottom == 3:
		(top, bottom, use) = (None, top, bottom)
	else: # No 3's detected, cycling both
		(top, bottom, use) = (None, None, max(top, bottom))
	return top, bottom, use

def TWOS_ONLY(top, bottom):
	#Possibly useful for Shi Ishmael
	if top == 2:
		(top, bottom, use) = (None, bottom, top)
	elif bottom == 2:
		(top, bottom, use) = (None, top, bottom)
	else: # No 2's detected, cycling both
		(top, bottom, use) = (None, None, max(top, bottom))
	return top, bottom, use

def THROW_OUT_ONES(top, bottom):
	#Default
	if (top, bottom) != (1, 1):
		(top, bottom, use) = (None, min(top, bottom), max(top, bottom))
	else: # Double-ones, cycling both
		assert (top == bottom)
		assert (top == 1)
		(top, bottom, use) = (None, None, max(top, bottom))
	return top, bottom, use	


def simulation(trials = 10000, cycleLogic = THREES_ONLY, cycleLogicName = " with only threes"):
	totals = [0, 0, 0]
	currentBag = list(SKILL_BAG)
	bottom = None
	top = None
	for i in range(0, trials):
		if bottom == None:
			[top, bottom], currentBag = drawBag(currentBag, 2)
		else: #Top is probably none here
			[top], currentBag = drawBag(currentBag, 1)
		top, bottom, use = cycleLogic(top, bottom)
		totals[use - 1] += 1
	print("Out of %s trials%s, Skill 1 was used %s times, Skill 2 was used %s times, and Skill 3 was used %s times" % 
				(trials, cycleLogicName, totals[0], totals[1], totals[2]))

simulation(100000, THREES_ONLY, " with as many Skill 3s as possible")
simulation(100000, TWOS_ONLY, " with as many Skill 2s as possible")
simulation(100000, THROW_OUT_ONES, " with as many Skill 2s and 3s as possible")
