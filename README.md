# Kuzushiji-MNIST

https://github.com/rois-codh/kmnist

http://codh.rois.ac.jp/kmnist/



|Model                            | Kuzushiji-MNIST | Memo
|---------------------------------|--------|---|
|[4-Nearest Neighbour Baseline](benchmarks/kuzushiji_mnist_knn.py)       | 91.56% | 
|[Keras Simple CNN Benchmark](benchmarks/kuzushiji_mnist_cnn.py)         | 95.12% |
|[PyTorch Simple CNN](colab_kmnist_pytorch_cnn_2.ipynb)                  | 95.14% |
|[PyTorch ResNet18](colab_kmnist_pytorch_resnet18_4.ipynb)               | 97.19% |
|[PyTorch ResNet50](colab_kmnist_pytorch_resnet50_2.ipynb)               | 97.45% |
|[PyTorch resnext50_32x4d](colab_kmnist_pytorch_resnext50_32x4d_2.ipynb) | 97.45% |
|[PyTorch VGG](colab_kmnist_pytorch_vgg_2.ipynb)                         | 97.01% |
|[PyTorch VGG_bn](colab_kmnist_pytorch_vgg_bn_2.ipynb)                   | 97.56% |


Environment (Google Colaboratory)
- Python  3.6.9
- PyTorch 1.3.1
- torchvision 0.4.2
- Numpy   1.17.4
