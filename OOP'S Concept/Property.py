class Arithmatic:
    def __init__(self,value):
        self._value=value #protected attribute

    def getValue(self):
        print('To retrive the value of \'_value\'')
        return self._value
    def setValue(self,value):
        print('Setting value to ' +value)#New Value/Updated
        self._value=value
    def detValue(self,value):
        print('Deleting value to ' +value)#New Value/Updated
        del self._value
    Value = property(getValue,setValue,detValue)

A1=Arithmatic(12)
print(A1.Value)
A1.Value='Suresh'
del A1.value
