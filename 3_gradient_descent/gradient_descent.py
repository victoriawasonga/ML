'''
MEAN SQUARE ERROR(MSE), GRADIENT DECENT, COST FUNCTION AND LEARNING RATE



when you have x and y(training data ) and in ml you tend to find the equation (predictive function) 
so that you can use it to predict future values

so our goal is to derive the equation which is a best fit line that goes though the data point 
however you can have so many lines that goes through the data points 

so how do we know which is the best fit 

so one way you draw random line then from actual data point you subract the predicted and get the square 
then you sum and devide by n (length) this is  MEAN SQUARE ERROR which is a type of COST FUNCTION 

there are other COST FUNCTIONS avalilable 

GRADIENT DECENT helps us get the best fit given training data sets 
with mimimum umber of interations and time 

to know the best size of the steps we use the derivtives (slopes)

learning rate is used in conjunction with the derivative to move 
'''
import numpy as np

def gradient_descent(x,y):
    m_curr=b_curr=0
    iteration=1000
    n=len(x)
    learning_rate=0.001

    for i in range(iteration):
        y_predicted=m_curr*x+b_curr
        cost=(1/n)*sum(val**2 for val in (y-y_predicted))
        m_derivative=(2/n)*sum(x*(y-y_predicted))
        b_derivative=(2/n)*sum(y-y_predicted)

        m_curr=m_curr-learning_rate*m_derivative
        b_curr=b_curr-learning_rate*b_derivative

        print("m {},b {}, interations {}, cost {}".format(m_curr,b_curr,i,cost))
    pass
x_new=np.array([1,2,3,4,5])
y_new=np.array([6,7,9,11,13])
gradient_descent(x_new,y_new)