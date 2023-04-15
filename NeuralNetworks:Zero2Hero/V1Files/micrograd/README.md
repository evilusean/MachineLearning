https://github.com/karpathy/micrograd </br>
A tiny Autograd engine (with a bite! :)). Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API. Both are tiny, with about 100 and 50 lines of code respectively. The DAG only operates over scalar values, so e.g. we chop up each neuron into all of its individual tiny adds and multiplies. However, this is enough to build up entire deep neural nets doing binary classification, as the demo notebook shows. Potentially useful for educational purposes.

Installation</br>
pip install micrograd</br>
Example usage</br>
Below is a slightly contrived example showing a number of possible supported operations:</br>

from micrograd.engine import Value

a = Value(-4.0) </br>
b = Value(2.0)</br>
c = a + b</br>
d = a * b + b**3</br>
c += c + 1</br>
c += 1 + c + (-a)</br>
d += d * 2 + (b + a).relu()</br>
d += 3 * d + (b - a).relu()</br>
e = c - d</br>
f = e**2</br>
g = f / 2.0</br>
g += 10.0 / f</br>
print(f'{g.data:.4f}') # prints 24.7041, the outcome of this forward pass</br>
g.backward()</br>
print(f'{a.grad:.4f}') # prints 138.8338, i.e. the numerical value of dg/da</br>
print(f'{b.grad:.4f}') # prints 645.5773, i.e. the numerical value of dg/db</br>
Training a neural net</br>
The notebook demo.ipynb provides a full demo of training an 2-layer neural network (MLP) binary classifier. This is achieved by initializing a neural net from micrograd.nn module, implementing a simple svm "max-margin" binary classification loss and using SGD for optimization. As shown in the notebook, using a 2-layer neural net with two 16-node hidden layers we achieve the following decision boundary on the moon dataset:

2d neuron</br>

Tracing / visualization</br>
For added convenience, the notebook trace_graph.ipynb produces graphviz visualizations. E.g. this one below is of a simple 2D neuron, arrived at by calling draw_dot on the code below, and it shows both the data (left number in each node) and the gradient (right number in each node).

from micrograd import nn</br>
n = nn.Neuron(2)</br>
x = [Value(1.0), Value(-2.0)]</br>
y = n(x)</br>
dot = draw_dot(y)</br>
2d neuron</br>

Running tests</br>
To run the unit tests you will have to install PyTorch, which the tests use as a reference for verifying the correctness of the calculated gradients. Then simply:
</br>
python -m pytest</br>
License</br>
MIT</br>
