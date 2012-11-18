#!/usr/bin/python
import os, sys,math

class Player:
	def __init__(self):
		print 'new player created'
	
	def play(self, world):
		currentFitness  = world.Q - world.B*(pow(world.n - world.M,2))
		futureFitness = world.Q - world.B*(float(pow(world.n +1 - world.M,2)))
		coopFitness = currentFitness - world.c
		individualFitness = world.Q - world.B*(float(pow(1 - world.M,2)))

		p = 1-(world.c/(currentFitness-futureFitness))
		print '\tfitness with ' + str(world.n) + ' players: ' + str(currentFitness) + ' adding 1 player: ' + str(futureFitness) + ' coop: ' + str(coopFitness) + ' single individual fitness: ' + str(individualFitness) + '  probability of cooperation: ' + str(p)

class World:
	Q = 0.0
	B = 0.0
	M = 0
	c = 0.0
	maxPlayers = 0
	players = []
	n = 0

	def __init__(self, Q, M, c, maxPlayers):
		self.Q = Q
		self.B = Q/pow(M,2)
		self.M = M
		self.n = 0
		self.c = c
		self.maxPlayers = maxPlayers 
		print 'World created with Q: ' + str(Q) + ' B: ' + str(self.B) + ' M: ' + str(M)

	def step(self):
		print 'step with num. players:' + str(self.n)
		for i in range(len(self.players)):
			self.players[i].play(self)
		self.players.append(Player())
		self.n = len(self.players)


	def game(self):
		for i in range(self.maxPlayers+1):
			self.step()

def main():
	world = World(1.0, 5, 0.3, 10)
	world.game()

if __name__ == "__main__":
    main()
	
