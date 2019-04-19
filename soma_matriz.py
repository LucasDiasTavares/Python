m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]

def dimensões(m1,m2):
	line = len(m1)
	column = len(m1[0])
	line2 = len(m2)
	column2 = len(m2[0])
	if ((line == line2) and (column2 == column)): 
		return True
	else :
		return False
def soma_matrizes(m1,m2):
	if (dimensões(m1,m2)):
                for i in range(len(m1)):
                        for j in range(len(m1[0])):				
                                m1[i][j] = m1[i][j] + m2[i][j]
	return m1
        else:
                return False
if ((soma_matrizes(m1,m2)) == False):
	print('False')
else :
	print (soma_matrizes(m1,m2)[:])
