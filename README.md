# Kuzushiji-MNIST

https://github.com/rois-codh/kmnist

http://codh.rois.ac.jp/kmnist/



|Model                            | MNIST | Kuzushiji-MNIST | Credit
|---------------------------------|-------|--------|---|
|[4-Nearest Neighbour Baseline](benchmarks/kuzushiji_mnist_knn.py)     |97.14% | 91.56% | 
|[Tuned SVM (RBF kernel)](https://github.com/rois-codh/kmnist/issues/3) | 98.57% |  | [TomZephire](https://github.com/TomZephire)
|[Keras Simple CNN Benchmark](benchmarks/kuzushiji_mnist_cnn.py)       |99.06% | 95.12% |
|PreActResNet-18                  |99.56% | 97.82% |
|PreActResNet-18 + Input Mixup    |99.54% | 98.41% |
|PreActResNet-18 + Manifold Mixup |99.54% | 98.83% |
|[ResNet18 + VGG Ensemble](https://github.com/ranihorev/Kuzushiji_MNIST) | **99.60%** | **98.90%** | [Rani Horev](https://twitter.com/HorevRani)
|[PyTorch Simple CNN](code/kuzushiji_mnist_pytorch.py)       |99.10% | 95.02% |
