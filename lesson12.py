#listt = [21, 54, 65, 856, 345]
#x = listt[0]
#for i in listt:
#	if i > x:
#		x = i
#print(x)

########################
#x = listt[0]
#for i in listt:
#	if i < x:
#		x = i
#print(x)
########################
#x = 0
#for i in listt:
#	x += i
#print(x)
#######################
#x = 0
#for i in listt:
#	x += i
#	y = x / len(listt)
#print(y)
#######################
#x = 1
#for i in listt:
#	x *= i
#print(x)
#######################
#listt2 = [43, 65, 2374, 324, 30]
#for i in listt:
#	for j in listt2:
#		if i == j:
#			print('yes')
#######################
#for i in listt:
#	for j in listt2:
#		if i == j:
#			print(j) 			
#######################
#listt = [21, 50, 65, 856, 345]
#listt2 = [20, 50, 75, 852, 344]
#for i in listt:
#	for j in listt2:
#		if i % j == 0:
#			print(i)
#######################
import random
mast = ['sirt', 'qyap', 'xach' 'xar']
qar = ['9', '10', 'J', 'Q', 'K', 'T']
kalod = []
for i in mast:
	for j in qar:
		result = i + j
		kalod.append(result)
random.shuffle(kalod)
print(kalod)

artur = []
armen = []

for i in range(5):
	x = kalod.pop()
	armen.append(x)
	y = kalod.pop()
	artur.append(x)
trump = kalod.pop()
armen.sort()
artur.sort()
choice = input('Do you want take this trump? ') == 'yes'
if choice:
	armen.append(trump)
	for i in range(2):
		x = kalod.pop()
		armen.append(x)
	for j in range(3):
		y = kalod.pop()
		artur.append(y)
armen.sort()
artur.sort()

	print('Armen', armen)
	print('Artur', artur)