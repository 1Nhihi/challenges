find = [816696039, 862511530, 897431439, 341060728, 173157153, 31974957, 491987052, 513290022, 463763452, 949994705, 910803499, 303483511, 378099927, 773435663, 305463445, 656532801, 655150297, 28357806, 69914739, 213536453, 962912446, 458779691, 598643891, 94970179, 732507398, 792930123, 216371336, 680163935, 397010125, 693248832, 926462193, 419350956, 594922380, 944019434, 93600641, 116339550, 373995190, 558908218, 700841647, 703877327, 665247438, 690373754, 35138387, 389900716, 625740467, 682452898, 894528752, 603308386, 442640217, 15961938, 573068354]

def Addition(a, b):
	return (a + b)% 0x3B9ACA07

def Multiplication(a1, a2):    		
    return (a1 * a2) % 0x3B9ACA07

def sub_555555555374(a1,a2):
	a3 = 1
	while a2:
		if a2 &1:
			a3 = Multiplication(a3, a1) % 0x3B9ACA07
		a1 = Multiplication(a1,a1) % 0x3B9ACA07
		a2 >>=1
	return a3

# brute force num1 và num2
# a = ord('a')

# for i in range( 0xff):
# 	for j in range( 0xff):

# 		v6  = 0
# 		v3 = Addition(v6, a)
# 		v4 = Multiplication(v3, i)
# 		v6 = sub_555555555374(v4 , j)
# 		if v6 == 816696039:
# 			print(v6, i, j)


flag = ''
enc = 0
num1 = 237
num2 = 41

for i in find:
	for s in range(0x20, 0x7f):
		v3 = Addition(enc, s)
		v4 = Multiplication(v3, num1)
		v6 = sub_555555555374(v4 , num2)
		if v6 == i:
			flag += chr(s)
			enc = v6

print(flag)