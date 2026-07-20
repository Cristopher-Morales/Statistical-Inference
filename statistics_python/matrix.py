from mathematics import dotProduct

class Matrix():
    
    def __init__(self,rows:int,columns:int=None, init_value=0):
        if columns is None:
            print(f'Matrix is considered to be a square matrix of dimension {rows}x{rows}')
            columns=rows
        assert (isinstance(rows, int) and isinstance(columns,int)),"rows and colums must be integers!"
        assert (rows>0 and columns>0),"rows and colums must be positive integers!"
        self.m=rows
        self.n=columns
        self.Matrix= [[init_value] * self.n for _ in range(self.m)]
    
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
            # assert 0<=position<self.m,f'Out of index range for assessing row {position} in a matrix of {self.m}-rows'
            if self.m>1:
                assert 0<=position<self.m,f'Out of index range for assessing row {position} in a matrix of {self.m}-rows'
                A_=Matrix(1,self.n)
                A_[0]=self.Matrix[position]
                return A_
            else:
                assert 0<=position<self.n, f'out of bounds for 1-row matrix with {self.n} columns ({position})'
                return self.Matrix[0][position]
        elif isinstance(position,tuple):
            i,j=position
            if not isinstance(j,slice) and not isinstance(i,slice):
                assert isinstance(i,int) and 0<=i<self.m, f'{i} must be a positive integer bigger or equal than 0 and smaller than number of rows {self.m}'
                assert isinstance(j,int) and 0<=j<self.n, f'{j} must be a positive integer bigger or equal than 0 and smaller than number of columns {self.n}'
                return self.Matrix[i][j]
            else:
                if isinstance(j,slice) and isinstance(i,slice):
                    i_start = 0 if i.start is None else i.start
                    i_stop = self.m if i.stop is None else i.stop
                    j_start = 0 if j.start is None else j.start
                    j_stop = self.n if j.stop is None else j.stop
                    assert 0<=i_start<self.m and 0<=i_stop<=self.m, f'indexes for row slice are out of bound ({i_start}:{i_stop}) '
                    assert 0<=j_start<self.m and 0<=j_start<=self.n, f'indexes for column slice are out of bound ({j_start}:{j_stop}) '
                    assert i_start<i_stop, f'start index must be smaller than end index for row slice ({i_start}<{i_stop}) '
                    assert j_start<j_stop, f'start index must be smaller than end index for row slice ({j_start}<{j_stop}) '
                    m,n=i_stop-i_start, j_stop-j_start
                    A_=Matrix(m,n)
                    for i in range(0,m):
                        for j in range(0,n):
                            A_[i,j]=self[i_start+i,j_start+j]
                    return A_
                elif isinstance(i,slice):
                    assert isinstance(j, int) and 0<=j<self.n, f'{j} must be a valid positive integer and smaller than {self.m}.'
                    i_start = 0 if i.start is None else i.start
                    i_stop = self.m if i.stop is None else i.stop
                    assert 0<=i_start<self.m and 0<=i_stop<=self.m, f'indexes for row slice are out of bound ({i_start}:{i_stop}) '
                    assert i_start<i_stop, f'start index must be smaller than end index for row slice ({i_start}<{i_stop}) '
                    m,n=i_stop-i_start, 1
                    A_=Matrix(m,n)
                    for i in range(0,m):
                        A_[i,0]=self[i_start+i,j]
                    return A_
                elif isinstance(j,slice):
                    assert isinstance(i, int) and 0<=i<self.m, f'{i} must be a valid positive integer and smaller than {self.m}.'
                    j_start = 0 if j.start is None else j.start
                    j_stop = self.n if j.stop is None else j.stop
                    assert 0<=j_start<self.n and 0<=j_stop<=self.n, f'indexes for row slice are out of bound ({j_start}:{j_stop}) '
                    assert j_start<j_stop, f'start index must be smaller than end index for row slice ({j_start}<{j_stop}) '
                    m,n=1,j_stop-j_start
                    A_=Matrix(m,n)
                    for j in range(0,n):
                        A_[0,j]=self[i,j_start+j]
                    return A_
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
                for j in range(self.n):
                    C[i,j] = other * self[i,j]
            return C
        else:
            raise ValueError(f'invalid multiply operation with {other}')
    
    def __rmul__(self, other):
        return self * other
    
    def __str__(self):
        return f'{self.Matrix}'
    
    def __repr__(self):
        return self.Matrix
    
    def __len__(self):
        assert self.m==1 or self.n==1, f'len() method only available for single row-matrix or single row-column, uses .shape() method for getting matrix dimension'
        if self.m==1:
            return self.n
        else:
            return self.m

    def __pow__(self,other:int):
        assert self.m==self.n, f'Matrix exponentiation is only defined for square matrices '
        assert(isinstance(other,int)) and other>=0,f'exponent {other} must be a non-negative integer'
        result=Matrix(self.m,self.m).identity()
        k=other
        y=self
        while (k>0):
            if k%2==0:
                y=y*y
                k//=2
            else:
                result=result*y
                k-=1
        return result

    def shape(self):
        return self.m, self.n

    def transpose(self):
        A_t=Matrix(self.n,self.m)
        for i in range(self.m):
            for j in range(self.n):
                A_t[j,i]=self.Matrix[i][j]
        return A_t
    
    def identity(self):
        I=Matrix(self.m,self.m)
        for i in range(self.m):
            I[i,i]=1.0
        return I