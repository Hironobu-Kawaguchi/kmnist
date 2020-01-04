# Kuzushiji-MNIST

Environment (Google Colaboratory)
- Python  3.6.9
- PyTorch 1.3.1
- torchvision 0.4.2
- Numpy   1.17.4

|Model                            | Kuzushiji-MNIST | Time
|---------------------------------|--------|---|
|[4-Nearest Neighbour Baseline](benchmarks/kuzushiji_mnist_knn.py) | 92.10% | 
|[Keras Simple CNN Benchmark](benchmarks/kuzushiji_mnist_cnn.py)   | 94.63% |
|[PyTorch Simple CNN](colab_kmnist_pytorch.ipynb)                  | 94.86% |  2min  4s
|[PyTorch ResNet18](colab_kmnist_pytorch.ipynb)                    | 97.25% |  3min 24s
|[PyTorch ResNet50](colab_kmnist_pytorch.ipynb)                    | 96.87% |  7min 22s
|[PyTorch ResNeXt50_32x4d](colab_kmnist_pytorch.ipynb)             | 96.82% | 10min 52s
|[PyTorch VGG](colab_kmnist_pytorch.ipynb)                         | 98.10% |  2min 52s
|[PyTorch ResNet18+VGG](colab_kmnist_pytorch.ipynb)                | 97.25% |  4min 57s
|[PyTorch ResNeXt50+VGG](colab_kmnist_pytorch.ipynb)               | 98.03% | 12min 42s

https://github.com/rois-codh/kmnist

http://codh.rois.ac.jp/kmnist/
