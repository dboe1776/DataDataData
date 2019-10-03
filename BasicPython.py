# Daniel Boe
# March 19, 2019
# High level introduction to basic engineering computing with python

import numpy as np
import matplotlib.pyplot as plt

# Create a list (vector or array in MATLAB)
A = [1,2,3,4,5,6]

'''Python does not natively have multidimentional arrays (i.e. a matrix)
rather, it just uses lists of lists which is just a list contained inside a list'''

# Create a list of Lists
B = [A,A]

'''This works well for storing variables and such, but for most engineering applications,
it is much preferred to use a numpy.array object instead of a list. These behave
almost identically to the arrays/vectors you are (hopefully) used to in MATLAB. 
Additionally, numpy arrays have many powerful built-in attributes and functions
that allow for faster and much more convenient computational operations'''
# Create a numpy.array
A_np = np.array([1,2,3,4,5,6])

'''Now running this, we get an actual matrix that we would be more accustomed to'''
B_np = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
# note that this would work too
B_np = np.array([A_np,A_np]) # Create 2D numpy array from two Numpy arrays
# as would this:
B_np = np.array([A,A]) # Create a 2D numpy array from two lists


'''To illustrate the benefits of using a numpy array over the list, let's say we want to
generate a list in which each element is one half of the previous one.
That is, the n element is defined by 1/2^n'''

a=np.arange(0,11,1)
1/2**a

'''using an np.array, we can easily make this array by first creating an index array and then
operating on it.  Note that the second line consists of a scaler being divided by another scaler
that is being raised to a power where the power is an array. Numpy automatically infers that we want
an array as the output and just performs this operation element wise.  This is one of the key
features of the numpy module, it allows us to essentially treat an n-dimensional 
array as a single scaler where operations are extended element-wise 
to each value of the array.'''


'''If we try the same thing with a list, we get a TypeError'''
# a=list(np.arange(0,11,1))
# 1/2**a


'''Next let's take a look at some basic numerical analysis/plotting stuff. 
First, let's create an array of x values to input into a function with the end
goal being generating a plot of f(x)'''

x_vals = np.linspace(0,10,1000)			# Generate an array with 1000 equally spaced elements from 0-10

''' also, we could use the np.arange function which creates the array by defining
 a step size rather than a number of points'''

x_vals = np.arange(0,10,0.01) # Generate an array with elements from 0-10 spaced 0.01 apart


'''Next, we want to create an array of y values, but first let's look at how functions
are defined in python'''
def func(x):
    
    y = np.sin(x)*np.exp(-x)
    
    return y

"Now we can call the function that we just created py passing it the array of x values"
y_vals = func(x_vals)

"alternately, we could have also just have done:"
y_vals = np.sin(x_vals)*np.exp(-x_vals)

plt.figure(1)
"Creating a simple plot now, is very easy"
plt.plot(x_vals, y_vals, linewidth = 3, color = 'green')
plt.grid()
plt.title('Example of Plotting a Single Trace')
plt.show()


"Next, lets look at _for_ loops by plotting multiple lines on a new figure"
y_vals2 = np.cos(x_vals)*np.exp(-x_vals)
y_vals3 = np.cos(x_vals)*np.sin(x_vals)
y_vals4 = x_vals**2*np.exp(-x_vals)


'''Next, we store all of the y_vals into a list, and create a list of labels that"
"we will eventually use to label each plot and create a legend'''
Traces = [y_vals, y_vals2, y_vals3, y_vals4]
labels = ['y_1','y_2', 'y_3', 'y_4']

# Create a new figure 
plt.figure(2)

'''For loops are a little different in python; rather than create an index, we just
iterate through each element of a list or array'''
i = 0
for trace in Traces:
    plt.plot(x_vals, trace, linewidth = 3, label = labels[i])
    i = i+1
    
    
"Here we ask python to create a legend, add a grid, and make a title"
plt.legend(framealpha = 0.25)
plt.grid()
plt.title('Example of Plotting Multiple Plots')
plt.show()


'''let's, say we want to integrate y_vals4 over the interval 0 - 10; numpy can take
care of that'''

I = np.trapz(y = y_vals4, x = x_vals)
print('The integral of y_vals is:',str(round(I,3)))


'''or lets differentiate'''
dy_vals4 = np.gradient(y_vals4, x_vals)


'''lets create one more plot that shows the differentiation and integration
Note that I used LaTex syntax in the differentiation label - just put r outside
of the string'''
plt.figure(3)
plt.fill_between(x_vals, y1 = y_vals4,linewidth = 3, label = 'y_4', alpha = 0.5)
plt.plot(x_vals,dy_vals4,linewidth = 3, label = r'$\frac{dy_4}{dx}$' , \
         color = 'orange')

'''Create a legend and also set change the axis limits and such'''
plt.legend(framealpha = 0.25, fontsize = 16)
plt.grid()
plt.title('Example of numerical integration and differentiation -  I = '+ str(round(I,3)),\
          fontsize = 20, weight = 'bold')

'''accessing an array at [-1] automatically grabs the last element in the array'''
plt.xlim(left = x_vals[0], right = x_vals[-1])
plt.show()

'''Next, lets' consider the case where we want to know the values of a list that 
satisfy a certain condition. For, instance, let's say we want to know all the data points
for which y_vals4 is less than it's derivative. This is accomplished using
the np.where() function.'''

indicies = np.where(y_vals4<dy_vals4)

'''The Indicies array then contains the index of each point in y_vals2 that is greater 
than 0.5. If we want to know the functional values at these indicies, we can do that easily!'''
vals = y_vals2[indicies]


'''Next, let's plot this specific segment of y_vals4 overlayed upon our current 
figure'''
plt.plot(x_vals[indicies],y_vals4[indicies],linewidth=6,color='black')

