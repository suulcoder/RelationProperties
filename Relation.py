"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
Matemática Discreta - 10

	Program made by : 
		- Saúl Contreras (SuulCoder)
			18409

This program will represent a 
relation as a matrix for calculate
if the relation is a reflexive,
simetric, antisimetric or transitive.
"""
class BinaryMatrix(object):
	"""This class represents a Matrix

		Atributes:
			matrix: This atribute has to be made of
			an array of arrays, to represent each 
			row and column in the matrix. 

		Methods:
			Multiplication: This method does the product between
				the current matrix and other given as parameter
				the normal product of two matrixes and returns
				a BinaryMatrix type
			Intersection: This method does the XOR product between
				the current matrix and other given as parameter and
				returns a BinaryMatrix type.
			Precedence: a boolean function that returns if Mr1 <= Mr2
			Transposed : return the binary Matrix for the current type
			equals: return if the given matrix is equals to the type
		"""
	def __init__(self, matrix):
		self.matrix = matrix

	def Multiplication(self,newMatrix):
		result = []
		for i in self.matrix:
			row = []
			counter = 0
			for j in i:
				product  = 0;
				for currenti in i:
					product += int(currenti)*int(newMatrix[int(currenti)][counter])
				if(product!=0):												#Binary Matrix
					product = 1
				row.append(product)
				counter+=1
			result.append(row)
		toReturn = BinaryMatrix(result)
		return toReturn
					
	def Intersection(self,newMatrix):
		result = []
		rowCounter=0
		for i in self.matrix:
			columncounter=0
			row = []
			for j in i:
				row.append(int(j)*int(newMatrix[rowCounter][columncounter]))
				columncounter+=1
			result.append(row)
			rowCounter+=1
		toReturn = BinaryMatrix(result)
		return toReturn

	def Precedence(self, newMatrix):
		result = []
		rowCounter=0
		for i in self.matrix:
			columncounter=0
			row = []
			for j in i:
				if(int(j)>int(newMatrix[rowCounter][columncounter])):
					return False
				columncounter+=1
			result.append(row)
			rowCounter+=1
		return True

	def Transposed(self):
		result = []
		row = 0 
		for i in self.matrix:
			column = 0 
			newRow = []
			for j in i:
				newRow.append(self.matrix[column][row])
				column+=1
			row+=1
			result.append(newRow)
		return result

	def equals(self,newMatrix):
		result = []
		rowCounter=0
		for i in self.matrix:
			columncounter=0
			row = []
			for j in i:
				if(int(j)!=int(newMatrix[rowCounter][columncounter])):
					return False
				columncounter+=1
			result.append(row)
			rowCounter+=1
		return True	

class Relation(object):
	"""
	This class represents a relation by a matrix
	
	Atributes:
		matrix: This atribute is an object of 
			type Matrix that will represent the
			relation. 

	Public methods:
		isReflexive: boolean function
		isSymmetric: boolean function
		isAntisymmetric: boolean Function
		isTransitive: boolean Function
	"""

	def __init__(self, matrix):
		super(Relation, self).__init__()
		self.matrix = matrix

	"""Boolean function that returns if the relation is 
	reflexive using:

		In <= Mr
													"""
	def isReflexive(self):
		InColumn = []
		row = 0
		for i in self.matrix.matrix:
			currentRow = []
			column = 0
			for j in i:
				if(row==column):
					currentRow.append(1)
				else:
					currentRow.append(0)
				column+=1
			InColumn.append(currentRow)
			row+=1
		In = BinaryMatrix(InColumn)
		return(In.Precedence(self.matrix.matrix))

	"""Boolean function that returns if the function is
	simetric using:

		Mr = Mr (Transposed)
													"""
	def isSymmetric(self):
		return(self.matrix.equals(self.matrix.Transposed()))

	"""Boolean function that returns if the function is 
	antisimetric using:

		Mr (intersection) Mr(Transposed) <= In
													"""
	def isAntisymmetric(self):
		InColumn = []
		row = 0
		for i in self.matrix.matrix:
			currentRow = []
			column = 0
			for j in i:
				if(row==column):
					currentRow.append(1)
				else:
					currentRow.append(0)
				column += 1
			InColumn.append(currentRow)
			row += 1
		In = InColumn
		return((self.matrix.Intersection(self.matrix.Transposed())).Precedence(In))

	"""Boolean funciton that returns if the function is 
	transitive using:

		Mr**2 <= Mr
													"""	
	def isTransitive(self):
		return((self.matrix.Multiplication(self.matrix.matrix)).Precedence(self.matrix.matrix))

print("""

************************************************************************************
                             Get Relation propeties easy
************************************************************************************

	Just write the matrix that represents your relation

	Use "," for divide elements in a row and "|" for divide rows in the matrix


	Ex:

		If you want to write the matrix:

                    _       _
                   |         |
                   | 1  0  1 |
                   | 0  1  0 |
                   | 1  1  0 |
                   |_       _|

		You must write:

			input:      1,0,1|0,1,0|1,1,0



""")
userInput = input("Write your input:\t\t")
newMatrix = userInput.split('|')
matrix = []
for row in newMatrix:
	newRow = row.split(',')
	matrix.append(newRow)
for row in matrix:
	for element in row:
		element = int(element)
myMatrix = BinaryMatrix(matrix)
myRelation = Relation(myMatrix)
print("------------------------------------------------------")
print("   The relation satisfies the following properties\n\n")
if(myRelation.isReflexive()):
	print("\t  Reflexivity")
if(myRelation.isSymmetric()):
	print("\t  Symmetry")
if (myRelation.isAntisymmetric()):
	print("\t  Antisymmetry")
if (myRelation.isTransitive()):
	print("\t  Transitivity")
print("------------------------------------------------------")





