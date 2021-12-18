# 写在前面的话

**OpenCV**是计算机视觉中经典的专用库，其支持多语言、跨平台，功能强大。**OpenCV-Python**为OpenCV提供了Python接口，使得使用者在Python中能够调用C/C++，在保证易读性和运行效率的前提下，实现所需的功能。

**OpenCV-Python Tutorials**是官方提供的文档，其内容全面、简单易懂，使得初学者能够快速上手使用。2014年段力辉在当时已翻译过OpenCV3.0，但时隔五年，如今的**OpenCV4.1**中许多函数和内容已经有所更新，因此有必要对该官方文档再进行一次翻译。

翻译过程中难免有所疏漏，如发现错误，希望大家指出，谢谢支持。

OpenCV-Python Tutorials官方文档：https://docs.opencv.org/4.1.2/d6/d00/tutorial_py_root.html

# 目录

### [OpenCV中文官方文档](http://www.woshicver.com/.)

*   <span class="caption-text">OpenCV简介</span>

    * [0_OpenCV-Python Tutorials](FirstSection/0_OpenCV-Python_Tutorials.md)
    
*   <span class="caption-text">OpenCV安装</span>

    *   [1_1_OpenCV-Python教程简介](SecondSection/1_1_OpenCV-Python教程简介.md)
    *   [1_2_在Windows中安装OpenCV-Python](SecondSection/1_2_在Windows中安装OpenCV-Python.md)
    *   [1_3_在Fedora中安装OpenCV-Python](SecondSection/1_3_在Fedora中安装OpenCV-Python.md)
    *   [1_4_在Ubuntu中安装OpenCV-Python](SecondSection/1_4_在Ubuntu中安装OpenCV-Python.md)
    
*   <span class="caption-text">OpenCV中的GUI特性</span>

    *   [2_1_图像入门](ThirdSection/2_1_图像入门.md)
    *   [2_2_视频入门](ThirdSection/2_2_视频入门.md)
    *   [2_3_OpenCV中的绘图功能](ThirdSection/2_3_OpenCV中的绘图功能.md)
    *   [2_4_鼠标作为画笔](ThirdSection/2_4_鼠标作为画笔.md)
    *   [2_5_轨迹栏作为调色板](ThirdSection/2_5_轨迹栏作为调色板.md)
    
*   <span class="caption-text">核心操作</span>

    *   [3_1_图像的基本操作](FourthSection/3_1_图像的基本操作.md)
    *   [3_2_图像上的算法运算](FourthSection/3_2_图像上的算法运算.md)
    *   [3_3_性能衡量和提升技术](FourthSection/3_3_性能衡量和提升技术.md)
    
*   <span class="caption-text">OpenCV中的图像处理</span>

    *   [4_1_改变颜色空间](FifthSection/4_1_改变颜色空间.md)
    *   [4_2_图像几何变换](FifthSection/4_2_图像几何变换.md)
    *   [4_3_图像阈值](FifthSection/4_3_图像阈值.md)
    *   [4_4_图像平滑](FifthSection/4_4_图像平滑.md)
    *   [4_5_形态转换](FifthSection/4_5_形态转换.md)
    *   [4_6_图像梯度](FifthSection/4_6_图像梯度.md)
    *   [4_7_Canny边缘检测](FifthSection/4_7_Canny边缘检测.md)
    *   [4_8_图像金字塔](FifthSection/4_8_图像金字塔.md)
    *   [4_9_1_OpenCV中的轮廓](FifthSection/4_9_1_OpenCV中的轮廓.md)
    *   [4_9_2_轮廓特征](FifthSection/4_9_2_轮廓特征.md)
    *   [4_9_3_轮廓属性](FifthSection/4_9_3_轮廓属性.md)
    *   [4_9_4_轮廓：更多属性](FifthSection/4_9_4_轮廓：更多属性.md)
    *   [4_9_5_轮廓分层](FifthSection/4_9_5_轮廓分层.md)
    *   [4_10_1_直方图-1：查找，绘制，分析](FifthSection/4_10_1_直方图-1：查找，绘制，分析.md)
    *   [4_10_2_直方图-2：直方图均衡](FifthSection/4_10_2_直方图-2：直方图均衡.md)
    *   [4_10_3_直方图3：二维直方图](FifthSection/4_10_3_直方图3：二维直方图.md)
    *   [4_10_4_直方图-4：直方图反投影](FifthSection/4_10_4_直方图-4：直方图反投影.md)
    *   [4_11_傅里叶变换](FifthSection/4_11_傅里叶变换.md)
    *   [4_12_模板匹配](FifthSection/4_12_模板匹配.md)
    *   [4_13_霍夫线变换](FifthSection/4_13_霍夫线变换.md)
    *   [4_14_霍夫圈变换](FifthSection/4_14_霍夫圈变换.md)
    *   [4_15_图像分割与分水岭算法](FifthSection/4_15_图像分割与分水岭算法.md)
    *   [4_16_交互式前景提取使用GrabCut算法](FifthSection/4_16_交互式前景提取使用GrabCut算法.md)
    
*   <span class="caption-text">特征检测与描述</span>

    *   [5_1_理解特征](Sixth/5_1_理解特征.md)
    *   [5_2_哈里斯角检测](Sixth/5_2_哈里斯角检测.md)
    *   [5_3_Shi-Tomasi拐角探测器和良好的跟踪功能](Sixth/5_3_Shi-Tomasi拐角探测器和良好的跟踪功能.md)
    *   [5_4_SIFT（尺度不变特征变换）简介](Sixth/5_4_SIFT（尺度不变特征变换）简介.md)
    *   [5_5_SURF简介（加速的强大功能）](Sixth/5_5_SURF简介（加速的强大功能）.md)
    *   [5_6_用于角点检测的FAST算法](Sixth/5_6_用于角点检测的FAST算法.md)
    *   [5_7_BRIEF（二进制的鲁棒独立基本特征）](Sixth/5_7_BRIEF（二进制的鲁棒独立基本特征）.md)
    *   [5_8_ORB（定向快速和旋转简要）](Sixth/5_8_ORB（定向快速和旋转简要）.md)
    *   [5_9_特征匹配](Sixth/5_9_特征匹配.md)
    *   [5_10_特征匹配+单应性查找对象](Sixth/5_10_特征匹配+单应性查找对象.md)
    
*   <span class="caption-text">视频分析</span>

    *   [6_1_如何使用背景分离方法](Seventh/6_1_如何使用背景分离方法.md)
    *   [6_2_Meanshift和Camshift](Seventh/6_2_Meanshift和Camshift.md)
    *   [6_3_光流](Seventh/6_3_光流.md)
    
*   <span class="caption-text">相机校准和3D重建</span>

    *   [7_1_相机校准](Eighth/7_1_相机校准.md)
    *   [7_2_姿态估计](Eighth/7_2_姿态估计.md)
    *   [7_3_对极几何](Eighth/7_3_对极几何.md)
    *   [7_4_立体图像的深度图](Eighth/7_4_立体图像的深度图.md)
    
*   <span class="caption-text">机器学习</span>

    *   [8_1_理解KNN](Ninth/8_1_理解KNN.md)
    *   [8_2_使用OCR手写数据集运行KNN](Ninth/8_2_使用OCR手写数据集运行KNN.md)
    *   [8_3_理解SVM](Ninth/8_3_理解SVM.md)
    *   [8_4_使用OCR手写数据集运行SVM](Ninth/8_4_使用OCR手写数据集运行SVM.md)
    *   [8_5_理解K均值聚类](Ninth/8_5_理解K均值聚类.md)
    *   [8_6_OpenCV中的K均值](Ninth/8_6_OpenCV中的K均值.md)
    
*   <span class="caption-text">计算摄影学</span>

    *   [9_1_图像去噪](Tenth/9_1_图像去噪.md)
    *   [9_2_图像修补](Tenth/9_2_图像修补.md)
    *   [9_3_高动态范围](Tenth/9_3_高动态范围.md)
    
*   <span class="caption-text">目标检测</span>

    *   [10_1_级联分类器](Eleventh/10_1_级联分类器.md)
    *   [10_2_级联分类器训练](Eleventh/10_2_级联分类器训练.md)
    
*   <span class="caption-text">OpenCV-Python Binding</span>

    *   [11_1_OpenCV-Python Bindings](Twelfth/11_1_OpenCV-Python_Bindings.md)

# 关于

OpenCV 中文官方文档

[http://woshicver.com/](http://woshicver.com/)
