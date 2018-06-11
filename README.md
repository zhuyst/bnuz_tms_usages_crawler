# BNUZ-TMS系统-教室使用情况-爬虫
用于爬取TMS系统的教室使用情况，主要用于爬取考试周的考试科目（因为教务系统上的考试时间会慢一段时间），实现了`TMS系统的登陆以及信息爬取`。

## 基本信息

* 爬取系统：[TMS系统](http://tm.bnuz.edu.cn)
* Python版本： 3.6
* 第三方模块： [requests](http://www.python-requests.org/en/master/)

## 模块介绍

* main.py：启动
* session.py：用于Session保存与Headers伪造
* login.py：用于登陆TMS系统
* classroom.py：用于获取教室相关信息

## 爬取API

```python
# 教室使用情况API的基础URL
baseUrl = "http://tm.bnuz.edu.cn/api/"

# 教学楼API URL
buildingsUrl = baseUrl + "place/buildings"

# 教室API URL
placesUrl = buildingsUrl + "/:building/places"

# 教室使用情况API URL
usagesUrl = placesUrl + "/:place/usages"
```

## 运行效果

因为考试周是在第18-19周，所以筛选出这个时间段中`type='ks'`的`usages`即可

```
登陆成功
开始获取考试科目信息...

数学教研部 线性代数 丽泽楼A103 第18周 星期1 第7 - 9节
应用数学学院 应用统计学 丽泽楼A103 第19周 星期2 第3 - 4节
法律与行政学院 宪法学 丽泽楼A103 第19周 星期4 第3 - 4节
文学院 实用文体写作 丽泽楼A103 第18周 星期3 第3 - 4节
数学教研部 微积分 丽泽楼A103 第19周 星期1 第7 - 9节
法律与行政学院 政治学原理 丽泽楼A103 第19周 星期5 第3 - 4节
教育学院 女性研究 丽泽楼A103 第19周 星期2 第10 - 11节
教育学院 社会学 丽泽楼A103 第18周 星期6 第10 - 11节
教育学院 人类学 丽泽楼A103 第18周 星期7 第7 - 9节

..............
```

