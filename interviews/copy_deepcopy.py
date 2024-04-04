
import copy


x = [1,2,34,[1,2,3]]
y = copy.deepcopy(x)
x[0] = 900
x[3][0] = 10
#print(id(x),id(y),sep='\n')
print(x,y,sep='\n')
print('id of x[0] and  y[0]:',id(x[3]),id(y[3]),sep='\n')