# Kuzushiji-MNIST

https://github.com/rois-codh/kmnist

http://codh.rois.ac.jp/kmnist/



|Model                            | MNIST | Kuzushiji-MNIST | Memo
|---------------------------------|-------|--------|---|
|[4-Nearest Neighbour Baseline](benchmarks/kuzushiji_mnist_knn.py) |97.14% | 91.56% | 
|[Keras Simple CNN Benchmark](benchmarks/kuzushiji_mnist_cnn.py)   |99.06% | 95.12% |
|[PyTorch Simple CNN](code/kuzushiji_mnist_pytorch.py)             |99.10% | 95.02% |
|PyTorch ResNet18                                                  |       | 95.43% |


Environment (Google Colaboratory)
- Python  3.6.9
- PyTorch 1.3.1
- torchvision 0.4.2
- Numpy   1.17.4
