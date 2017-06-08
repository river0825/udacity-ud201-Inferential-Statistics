# udacity-ud201-Inferential-Statistics

location of this document : https://github.com/river0825/udacity-ud201-Inferential-Statistics

php practice for [Inferential Statistics](https://classroom.udacity.com/courses/ud201)

## Lesson one

### 名詞

Mean : $ \mu = \frac{ \sum_{i=1}^n x_i }{n} $
> 算術平均數

Variance :  $ \frac{1}{N} \sum_{i=1}^n (x_i - \mu)^2 $
> [變異數](https://zh.wikipedia.org/wiki/%E6%96%B9%E5%B7%AE)
> 一個隨機變數的變異數，描述的是它的離散程度，也就是該變數離其期望值的距離。在統計學中，要估算一個變數的期望值時，經常用到的方法是重複測量此變數的值，然後用所得數據的平均值來作為此變數的期望值。變異數有個簡易口訣為：「平方的平均」減去「平均的平方」。

Standard Deviation : $ \sigma = \sqrt{Variance} = \sqrt{ \frac{1}{N} \sum_{i=1}^n (x_i - \mu)^2 } $
> [標準差](https://zh.wikipedia.org/wiki/%E6%A8%99%E6%BA%96%E5%B7%AE) σ ( sigma )
>

Standard Error = $ Sd = \frac{\sigma}{\sqrt{n}} $
> [標準誤差](https://zh.wikipedia.org/wiki/%E6%A0%87%E5%87%86%E8%AF%AF): 樣本取樣統計量抽樣分佈的離散程度 對應 樣本本身的抽樣標準差 ($ \sigma $)的大小尺度



z-table : [標準常態分配表](http://www.linsgroup.com/Statistics/images/List13.gif)

sampling distribution : 抽樣分配 / 樣本分配

### 大綱

以 klout 的網站數據做為母數 , 來計算 平均值
