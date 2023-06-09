from committee import Committee

class Protocol:
    def __init__(self, committeeSize, validators, delegators, rounds, setup, reward):
        self.committeeSize = committeeSize
        self.validators = validators
        self.delegators = delegators
        self.rounds = rounds
        self.blockchain = []
        self.setup = setup
        self.reward = reward

    def selectCommittee(self):
        committee = Committee(self.committeeSize, self.setup)
        self.setup.selectCommittee(committee, self.validators)
        return committee

    def calculateRewards(self, committee):
        committee.calculateRewards(self.reward)

    def updateDelegations(self, committee):
        for delegator in self.delegators:
            if delegator.boundedValidator not in committee.validators:
                delegator.changeValidator(self.validators)

    def run(self):
        #committee = self.selectCommittee()
        #self.updateDelegations(committee)
        for i in range(self.rounds):
            committee = self.selectCommittee()
            self.updateDelegations(committee)
            newBlock = committee.round()
            if newBlock is not None:
                self.blockchain.append(newBlock)
                self.calculateRewards(committee)





