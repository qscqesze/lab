# SurprisingTech Lab 吃惊科技实验室

[![Python](https://img.shields.io/badge/python-3.4.2-red.svg?style=flat-square)](https://www.python.org/downloads/release/python-342/)
[![Django](https://img.shields.io/badge/django-2.0.4-ff69b4.svg?style=flat-square)](https://www.djangoproject.com/)

## 技术栈

前端 基于 牛逼的scuoj的excel设计修改得到：

<pre>
    http://acm.scu.edu.cn/soj/index.action
</pre>

消息队列 基于 牛逼的kafka.txt文本，生产者不停往文本里面写，消费者读最后一行即可。

判题核心 基于 牛逼的docker 以及 精心制作的专业image

## How To Start

如果你是第一次运行

<pre>
	python3 manage.py migrate
</pre>

之后每次运行

<pre>
	bash -x start.sh
</pre>

## Others

mail:qscqesze@qq.com