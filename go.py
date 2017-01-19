#number of bidders set
numBidders = int(raw_input("How many bidders are there? "))
#seller sets asking price/opening bid
openingBid = int(raw_input("Set the opening bid: "))
bidIncrement = int(raw_input("Set minimum bid increment: "))
#def TelecomAuction(openingBid):
openingBidString = str('${:,.0f}'.format((openingBid)))
bidIncrementString = str('${:,.0f}'.format((bidIncrement)))
print "The opening bid is " + openingBidString + ' and the minimum bid increment is ' + bidIncrementString + '.'
#TelecomAuction(openingBid)
#bidding begins
print "Please submit your first round of bids."
#create intial list of bids, define bidders
listOfBidderNames = []
listOfBids = [] 
while numBidders > 0:
	bidderName = str(raw_input("What is your name? "))
	bidderBid = int(raw_input("What is your first bid? "))
	while bidderBid < openingBid:
			print "Your first bid must be higher than the opening bid."
			bidderBid = int(raw_input("What is your first bid? "))
	listOfBids.append(bidderBid)
	listOfBidderNames.append(bidderName)
	numBidders = numBidders - 1
intialBidList = zip(listOfBidderNames, listOfBids)
#show first round of bids
print ""
print ""
for (x,y) in intialBidList:
	print x + " bid $" + str(y)
#ask for next bids
print ""
print "Based on the last round of bids, please place your next bid."
print "If you do not wish to continue, bid 0:"
print ""
remainingBidders = len(listOfBidderNames)
nextBidList = zip(listOfBidderNames, listOfBids)
while remainingBidders > 1:
	previousBids = list(listOfBids)
	for (x,y) in nextBidList:
		bidderNumber = listOfBidderNames.index(x)
		remainingBidders = len(filter(lambda x: x != 0, listOfBids))
		if y != 0:
			nextBidderBid = int(raw_input("{}, what is your next bid? ".format(x)))
			if nextBidderBid != 0:
				while nextBidderBid < max(previousBids) + 1 :
					print "Your bid must be " + bidIncrementString + " higher than last round's highest bid."
					nextBidderBid = int(raw_input("{}, what is your next bid? ".format(x)))
			listOfBids.remove(y)
			#previousBids.insert(bidderNumber, nextBidderBid)
			listOfBids.insert(bidderNumber, nextBidderBid)
	nextBidList = zip(listOfBidderNames, listOfBids)
	print ""
	print "Thank you for your bids. The results are as follows:"
	print ""
	for (x,y) in nextBidList:
		if y == 0:
			print x + " dropped out."
		else:
			print x + " bid $" + str(y) + "."
	#ask for next bids
	if remainingBidders > 1:
		print ""
		print "Based on the last round of bids, please place your next bid."
		print "If you do not wish to continue, bid 0:"
		print ""
#if everyone but one drops out
allBids = filter(lambda x: x != 0, listOfBids)
if allBids == []:
	print ""
	print "Everyone has dropped out. The highest bidder from the last round wins."
	winnerBid = max(previousBids)
	winnerBidIndex = previousBids.index(winnerBid)
	winnerName = listOfBidderNames[winnerBidIndex]
	print winnerName + " won the auction for $" + str(winnerBid)
else: 
	winnerBid = allBids.pop()
	winnerBidIndex = listOfBids.index(winnerBid)
	winnerName = listOfBidderNames[winnerBidIndex]
	print ""
	print "The auction has ended. " + winnerName + " won the auction for $" + str(winnerBid)

