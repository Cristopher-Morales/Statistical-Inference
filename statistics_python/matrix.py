from mathematics import dotProduct

class Matrix():
    
    def __init__(self,rows:int,columns:int, init_value=0):
        assert (isinstance(rows, int) and isinstance(columns,int)),"rows and colums must be integers!"
        assert (rows>0 and columns>0),"rows and colums must be positive integers!"
        self.m=rows
        self.n=columns
        self.Matrix=self.Matrix = [[init_value] * self.n for _ in range(self.m)]
    
    def __setitem__(self, position, values):
        if isinstance(position,int) and 0<=position<self.m:
            assert isinstance(values,list), "a list of numbers must be provided to set a row"
            assert len(values)==self.n, "number of elements in list must be equal to the number of columns of the matrix"
            self.Matrix[position]=values
        elif isinstance(position,tuple):
            i,j=position
            assert isinstance(i,int) and 0<=i<self.m, f'{i} must be a positive integer bigger or equal than 0 and smaller than number of rows {self.m}'
            assert isinstance(j,int) and 0<=j<self.n, f'{j} must be a positive integer bigger or equal than 0 and smaller than number of columns {self.n}'
            assert isinstance(values,float) or isinstance(values, int), f'{values} must be a valid number!!'
            self.Matrix[i][j]=values
        else:
            raise ValueError(f'{position} is a invalid argument for setting a row or a matrix-element')
    
    def __getitem__(self, position):
        if isinstance(position,int):
            assert 0<=position<self.m,f'Out of index range for assessing row {position} in a matrix of {self.m}-rows'
            return self.Matrix[position]
        elif isinstance(position,tuple):
            i,j=position
            assert isinstance(i,int) and 0<=i<self.m, f'{i} must be a positive integer bigger or equal than 0 and smaller than number of rows {self.m}'
            assert isinstance(j,int) and 0<=j<self.n, f'{j} must be a positive integer bigger or equal than 0 and smaller than number of columns {self.n}'
            return self.Matrix[i][j]
        else:
            raise ValueError(f'{position} is an invalid argument for getting a row or element in a matrix')
    
    def __add__(self, other):
        assert self.m == other.m, f'number of rows must be equal. Different numbers of rows: {self.m} != {other.m}'
        assert self.n == other.n, f'number of columns must be equal. Different numbers of columns: {self.n} != {other.n}'
        C=Matrix(self.m,self.n)
        for i in range(self.m):
            for j in range(self.n):
                C[i,j]=self[i,j]+other[i,j]
        return C
    
    def __neg__(self):
        return -1*self
    
    def __sub__(self, other):
        return self+(-other)
    
    def __mul__(self, other):
        if isinstance(other,Matrix):
            assert self.n == other.m, f'number of columns of the first matrix must be equal to the number of rows of the second matrix.'
            C=Matrix(self.m,other.n)
            D=other.transpose()
            for i in range(self.m):
                for j in range(D.m):
                    C[i,j]=dotProduct(self[i],D[j])
            return C
        elif isinstance(other,(float,int)):
            C=Matrix(self.m, self.n)
            for i in range(self.m):
                C[i] = [other * value for value in self[i]]
            return C
        else:
            raise ValueError(f'invalid multiply operation with {other}')
    
    def __rmul__(self, other):
        return self * other
    
    def __str__(self):
        return f'{self.Matrix}'

    def transpose(self):
        A_t=Matrix(self.n,self.m)
        for i in range(self.m):
            for j in range(self.n):
                A_t[j,i]=self.Matrix[i][j]
        return A_t
