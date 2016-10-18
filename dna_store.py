import sys
import queue



class HuffmanNode(object):
	def __init__(self, child1 = None, child2 = None, child3 = None):
		self.child1 = child1
		self.child2 = child2
		self.child3 = child3 
	def children(self):
    	return( (self.child1, self.child2, self.child3) )

if (sys.argv[1]=[-d]):

	filename=sys.argv[2]
	text=[]
	with open(filename) as f:
    	text=list(f) 
 

	list_letters=[]
	list_frequencies=[]
	for word in text :
		for ch in word :
			if ch not in list_letters:
				list_letters.append(ch)
				list_frequencies.append(word.count(ch))

'''ταξινομούμε τις δύο λίστες με επιλογή'''
	k=0
	for i in range(len(list_letters)-1):
		m=i
		j=m+1 
		for j in range(len(list_letters)):
			if (list_frequencies[m]>list_frequencies[j]):
				k=list_letters[m]
				list_letters[m]=list_letters[j]
				list_letters[j]=k
				k=list_frequencies[m]
				list_frequencies[m]=list_frequencies[j]
				list_frequencies[j]=k

'''δημιουργούμε ένα λεξικό με τους χαρακτήρες και τις συχνότητες τους'''

	pq= {list_letters[i]:list_frequencies[i]}
	count=0
	for i in range(len(list_letters)):
		pq.put((list_frequencies[i],list_letters[i]))
		count=count+1
	if(count%2==0):
		pq.put((len(list_letters),'keno'))


	while pq.qsize()> 2:
    	ch1= pq.get()
    	ch2= pq.get() 
    	ch3= pq.get() 
    	node = HuffmanNode(ch1,ch2,ch3) 
    	print(ch1[0])
    	print(ch2[0])
    	print(ch3[0])
    	freq=ch1[0]+ch2[0]+ch3[0]
    	pq.put((freq,node))   

'''το κομμάτι που ακολουθεί αφορά την διαδικασία μετά την ολοκλήρωση του δέντρου'''

	previous='A'
	for i in range(len(trits_coding)):
		if (previous=='A'):
			if (trits_coding[i]=='0'):
				trits_coding[i]='C'
			else if (trits_coding[i]=='1'):
				trits_coding[i]='G'
			else if (trits_coding[i]=='2'):
				trits_coding[i]='T'
    	else if (previous=='C'):
    		if (trits_coding[i]=='0'):
				trits_coding[i]='G'
			else if (trits_coding[i]=='1'):
				trits_coding[i]='T'
			else if (trits_coding[i]=='2'):
				trits_coding[i]='A'
		else if (previous=='G'):
    		if (trits_coding[i]=='0'):
				trits_coding[i]='T'
			else if (trits_coding[i]=='1'):
				trits_coding[i]='A'
			else if (trits_coding[i]=='2'):
				trits_coding[i]='C'
		else if (previous=='T'):
    		if (trits_coding[i]=='0'):
				trits_coding[i]='A'
			else if (trits_coding[i]=='1'):
				trits_coding[i]='C'
			else if (trits_coding[i]=='2'):
				trits_coding[i]='G'
		previous=trits_coding[i]




	for i in range(len(trits_coding)):
		print trits_coding[i]





	