#!/usr/bin/python
import os, sys,math, random

class Player:
	def __init__(self, p):
		print 'new player created'
		self.p = p
		self.fitness = 0.0
	
	def play(self, world):
		currentFitness  = world.Q - world.B*(pow(world.getNumPlayers() - world.M,2))
		futureFitness = world.Q - world.B*(float(pow(world.getNumPlayers() +1 - world.M,2)))
		coopFitness = currentFitness - world.c
		individualFitness = world.Q - world.B*(float(pow(1 - world.M,2)))

		#p = 1.0-(world.c/(currentFitness-futureFitness))
		print '\tfitness with ' + str(world.getNumPlayers()) + ' players: ' + str(currentFitness) + ' adding 1 player: ' + str(futureFitness) + ' coop: ' + str(coopFitness) + ' single individual fitness: ' + str(individualFitness) + '  probability of cooperation: ' + str(self.p)
		# reject new individual
		if random.random() < self.p:
			self.fitness = self.fitness + coopFitness
			return 1
		# don't act 
		else:
			self.fitness = self.fitness + currentFitness
			return 0

class World:
	def __init__(self, p, Q, M, c, maxPlayers):
		self.Q = Q
		self.B = Q/pow((maxPlayers-M),2)
		self.M = M
		self.c = c
		self.p = p
		self.maxPlayers = maxPlayers 
		self.players = []
		self.players.append(Player(self.p))
		print 'world created with Q: ' + str(Q) + ' B: ' + str(self.B) + ' M: ' + str(M) + ' and p: ' + str(p)

	def getNumPlayers(self):
		return len(self.players)

	def step(self):
		print 'step with current num. players:' + str(self.getNumPlayers())
		reject = 0
		for i in self.players:
			if i.play(self) == 1:
				if reject == 0:
					reject = 1
		if reject == 0:
			self.players.append(Player(self.p))
			self.n = len(self.players)


	def game(self):
		for i in range(self.maxPlayers):
			self.step()

	def meanFitness(self):
		fitness = 0.0
		for i in self.players:
			fitness = fitness + i.fitness
		# maxPlayers - 1 because the first player was crested in the constructor
		return fitness/len(self.players)

def main():
	random.seed()

	print 'dummy;p;mean fitness;final players'
	for i in range(0,101):
		p = float(i)/100.0
		world = World(p, 1.0, 0, 0.0, 10)
		world.game()
		print 'world with p: ' + str(p) + ' finished with: ' + str(len(world.players)) + ' players and fitness: ' + str(world.meanFitness())
		print 'dummy;'+str(p)+';'+str(world.meanFitness())+';'+str(len(world.players))

if __name__ == "__main__":
    main()
	
