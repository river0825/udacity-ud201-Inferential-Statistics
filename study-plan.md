
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Study Resources](#study-resources)
  * [入門](#入門)
  * [Machine Learning: Python 機器學習：使­用Pytho­n](#machine-learning-python-機器學習使用pythonhttpswwwgitbookcombookhtygithubmachine-learning-python)
  * [Deep Learning Prerequisites: The Numpy Stack in Python](#deep-learning-prerequisites-the-numpy-stack-in-pythonhttpswwwudemycomdeep-learning-prerequisites-the-numpy-stack-in-pythonlearnv4overview)
  * [Deep Learning A-Z™: Hands-On Artificial Neural Networks](#deep-learning-a-ztm-hands-on-artificial-neural-networkshttpswwwudemycomdeeplearninglearnv4overview)
  * [TensorFlow](#tensorflow)
    * [CHAPTER 4A visual proof that neural nets can compute any function](#chapter-4a-visual-proof-that-neural-nets-can-compute-any-functionhttpneuralnetworksanddeeplearningcomchap4html)
      * [名詞](#名詞)
      * [摘要](#摘要)
  * [youtube](#youtube)
* [技術](#技術)
* [Books](#books)

<!-- tocstop -->


## Study Resources

### 入門
[ML Lesson from Google](https://www.youtube.com/playlist?list=PLN9fv183LecmymGioYSgYpC-dAJ6wMKaE)

[How Deep Neural Networks Work](
https://www.youtube.com/watch?v=ILsA4nyG7I0&index=2&list=PLN9fv183LecmymGioYSgYpC-dAJ6wMKaE&t=79s)


### [Machine Learning: Python 機器學習：使­用Pytho­n](https://www.gitbook.com/book/htygithub/machine-learning-python)

### [Deep Learning Prerequisites: The Numpy Stack in Python](https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/overview)

### [Deep Learning A-Z™: Hands-On Artificial Neural Networks](https://www.udemy.com/deeplearning/learn/v4/overview)

### TensorFlow

[tensorflow playground](
http://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.34635&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

[结合TensorFlow PlayGround的简单神经网络原理解释](http://hp.stuhome.net/index.php/2016/10/15/tensorflow-playground/)

#### [CHAPTER 4A visual proof that neural nets can compute any function](http://neuralnetworksanddeeplearning.com/chap4.html)
> 搭配 tensorflow playground 來看會比較清楚
> 前面的[章節](http://neuralnetworksanddeeplearning.com/chap4.html)有提到如何 用 python implement
> 這一章屬於入門

##### 名詞
Universal approximation theorem -> [通用近似定理](https://en.wikipedia.org/wiki/Universal_approximation_theorem)
Step function -> [階躍函數](https://zh.wikipedia.org/wiki/%E9%98%B6%E8%B7%83%E5%87%BD%E6%95%B0)

##### 摘要

類神經網路幾乎可以學習所有的 function

* 兩個要注意的地方
  1. 類神經網路並不是完整(exactly)的計算要學習的 function, 而是得到一個近似的可以接受的值
  2. function 必需是連續的，如果要摸擬的 function 有中斷 或是有突波，那麼在使用類神經網路就注意一點。但是在現實的狀況中，就算 function 不是連續的，類神經網路所近似出來的結果也常常是可以被接受的。

* Universality with one input and one output
  如何模擬一個 function   
  $$ f(x) = 0.2 + 0.4x^2 + 0.3xsin(15x) + 0.05 cos(50x) $$

  以兩個神經元來形成一個 方波，再調整方波的大小高度。再以很多小小的方波以積分的方式來逼近近似值
  ```viz
  digraph g {
      rankdir=LR
      splines=line

      subgraph cluster_0 {
        color=white;
        node [style=solid,color=blue4, shape=circle];
        x1 ;
        //x2 x3;
        label = "layer 1 (Input layer)";
      }

      subgraph cluster_1 {
        color=white;
        node [style=solid,color=red2, shape=circle];
        a12 a22 a32 a42;
        label = "layer 2 (hidden layer)";
      }

      subgraph cluster_2 {
        color=white;
        node [style=solid,color=seagreen2, shape=circle];
        O;
        label="layer 3 (output layer)";
      }

      x1 -> a12;
      x1 -> a22;
      x1 -> a32;
      x1 -> a42;

      /*x2 -> a12;
      x2 -> a22;
      x2 -> a32;
      x3 -> a12;
      x3 -> a22;
      x3 -> a32;*/

      a12 -> O
      a22 -> O

      a32 -> O
      a42 -> O

    }
  ```

讀到這!!!
to be continue
http://neuralnetworksanddeeplearning.com/chap4.html#many_input_variables

### youtube

[李宏毅 - ML Lecture 1: Regression - Case Study](https://www.youtube.com/watch?v=fegAeph9UaA_)


## 技術
[keras](https://keras.io/)
[sclearn](http://scikit-learn.org/stable/)

## Books

[TensorFlow+Keras 深度學習人工智慧實務應用 ](https://www.tenlong.com.tw/products/9789864342167)
