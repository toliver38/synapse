
'''
Constructors for the various cells.
( used for dmon config automation)
'''
import synapse.neuron as s_neuron
import synapse.cryotank as s_cryotank

def neuron(dirn, conf=None):
    return s_neuron.Neuron(dirn, conf=conf)

def cryo(dirn, conf=None):
    return s_cryotank.CryoCell(dirn, conf=conf)

#def axon(dirn, conf=None):
#def cortex(dirn, conf=None):
