import random

class Delegator:
    def __init__ (self , id , stake):
        self.id = id
        self.stake = stake
        self.boundedValidator = None
        self.totalReward = 0

    def deligateTo(self, validator):
        self.boundedValidator = validator

    def expectedEarning(self, pool, reward):
        totalVotingPower = sum(v.votingPower for v in pool)
        validatorShare = (self.boundedValidator.votingPower / totalVotingPower) * reward
        delegatorShare = (self.stake/self.boundedValidator.votingPower) * validatorShare
        return delegatorShare

    def changeValidator(self, pool):
        if self.boundedValidator is not None:
            self.boundedValidator.removeDelegator(self)
        validator = random.choice(pool)
        self.boundedValidator = validator
        self.boundedValidator.addDelegator(self)

    def updateReward(self, pool, reward, totalReward):
        self.totalReward += reward
        expectedReward = self.expectedEarning(pool, totalReward)
        if reward < expectedReward:
            self.changeValidator(pool)