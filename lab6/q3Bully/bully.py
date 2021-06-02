import sys

if len(sys.argv) != 3:
    print("Incorrect usage: Expects 2 arguments")
    sys.exit()

noOfNodes = int(sys.argv[1])
initiatorNode = int(sys.argv[2])

def bully_algorithm():
    print('Node: '+ str(initiatorNode)+ ' notices the coordinator: '+ str(noOfNodes)+' has failed')

    biggerNodes = []
    allNodes = []

    for i in range(initiatorNode+1, noOfNodes):
    	print('sent ELECTION message to: '+ str(i))

    for i in range(initiatorNode+1, noOfNodes):
	    print(str(i)+' sent OK message to '+ str(initiatorNode))
	    biggerNodes.append(i)
	    allNodes.append(i)
	
    for i in allNodes:
	    if len(biggerNodes) != 1:
	    	i = biggerNodes[0]
	    for j in range(i+1, noOfNodes):
	    	print(str(i)+' sent ELECTION message to '+str(j))
	    for j in range(i+1, noOfNodes):
	    	print(str(j)+' sent OK message to '+str(i))
	    if len(biggerNodes) != 1:
	    	biggerNodes.remove(i)
	    newCoordinatorNode = biggerNodes[0]

    for i in range(0, newCoordinatorNode):
    	print(str(newCoordinatorNode)+' sent COORDINATOR message to '+str(i))

if __name__ == '__main__':
	bully_algorithm()
