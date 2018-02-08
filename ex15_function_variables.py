def cheese_and_crackers (cheese_count, boxes_of_crackers):
	print "you've %d cheese!" %cheese_count
	print "you've %d boxes of crackers." %boxes_of_crackers

print "we can just give the function nos directly:"
cheese_and_crackers(20, 30)

print "or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can do the math inside too:"
cheese_and_crackers(10+20, 5+6)

print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+10, amount_of_crackers+20)