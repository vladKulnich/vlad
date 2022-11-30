import  numpy as np 
import matplotlib.pyplot as plt 
 
x = np.linspace(-2, 8,10)
print(x)
y=np.cos(x)+6*x
plt.plot(x,y,'y:',label='y=cosx+6x')
plt.xlabel('x')  
plt.ylabel('y')
plt.grid(True)
plt.title('Графік функції ')  
plt.legend()  
plt.show() 
plt.savefig('графік.png', dpi=400)