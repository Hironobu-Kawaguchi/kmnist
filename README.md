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
|[PyTorch Simple CNN](colab_kmnist_pytorch.ipynb)                  | 94.93% |  2min 49s
|[PyTorch ResNet18](colab_kmnist_pytorch.ipynb)                    | 97.25% |  4min 37s
|[PyTorch ResNet50](colab_kmnist_pytorch.ipynb)                    | 97.32% |  8min 39s
|[PyTorch ResNeXt50_32x4d](colab_kmnist_pytorch.ipynb)             | 96.84% | 10min  2s
|[PyTorch VGG](colab_kmnist_pytorch.ipynb)                         | 97.98% |  4min  1s
|[PyTorch ResNet18+VGG](colab_kmnist_pytorch.ipynb)                | 97.26% |  6min 41s
|[PyTorch ResNeXt50+VGG](colab_kmnist_pytorch.ipynb)               | 98.06% | 12min 59s
|[PyTorch Simple CNN + DA](colab_kmnist_pytorch_da.ipynb)          | 93.08% |  3min  5s
|[PyTorch ResNet18 + DA](colab_kmnist_pytorch_da.ipynb)            | 97.67% |  4min  5s
|[PyTorch ResNet50 + DA](colab_kmnist_pytorch_da.ipynb)            | 97.74% |  7min 25s
|[PyTorch ResNeXt50_32x4d + DA](colab_kmnist_pytorch_da.ipynb)     | 97.74% |  8min  8s
|[PyTorch VGG + DA](colab_kmnist_pytorch_da.ipynb)                 | 98.24% |  3min 57s
|[PyTorch ResNet18+VGG + DA](colab_kmnist_pytorch_da.ipynb)        | 97.98% |  6min 31s
|[PyTorch ResNeXt50+VGG + DA](colab_kmnist_pytorch_da.ipynb)       | 98.45% | 11min 20s

https://github.com/rois-codh/kmnist

http://codh.rois.ac.jp/kmnist/
