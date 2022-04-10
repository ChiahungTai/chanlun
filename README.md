# 历史行情缠论分析工具

---

`chanlun` 是一个基于缠中说禅理论，用于历史行情数据分析的 Python 包。

可用于量化交易、Jupyter 分析、以及 Html 页面展示。

[在线 Demo 展示](http://www.chanlun-trader.com/)

在线Demo只做上证指数的缠论示例

> 项目 GitHub 地址 : https://github.com/yijixiuxin/chanlun

**主要功能**

目前，`chanlun` 已经实现以下功能:

* 分型
* 笔
* 线段
* 笔中枢
* 走势类型
* 走势中枢 (只限PRO)
* 买卖点 (只限PRO)
* 背驰 (只限PRO)
* 多级别分析 (只限PRO)

## 付费项目介绍

**chanlun-pro 项目限时优惠，原价1000元，永久使用权，截止 2022-04-17 24点**

[chanlun-pro](https://github.com/yijixiuxin/chanlun/blob/main/README_PRO.md)

## 安装

### 用 pip 安装

    pip install -U chanlun

### 本地编译安装

    git clone https://github.com/yijixiuxin/chanlun.git
    cd chanlun
    python3 setup.py install

### 使用示例

[使用示例.ipynb](https://github.com/yijixiuxin/chanlun/tree/main/example/使用示例.ipynb)

    import pandas as pd
    from chanlun import cl
    from chanlun import kcharts

    # 获取 行情K线数据
    code = 'SH.688122'
    frequency = '30m'
    klines = pd.read_csv('./data/688122.csv')

    # 依据 K 线数据，计算缠论数据
    cl_data = cl.CL(code, frequency).process_klines(klines)
    chart = kcharts.render_charts('%s - %s' % (code, frequency), cl_data)
    # 图标展示
    chart

### 实际效果展示

![Demo-1](https://github.com/yijixiuxin/chanlun/raw/main/images/demo-1.png)

**有 bug 请在这个页面提交： https://github.com/yijixiuxin/chanlun/issues**

**缠论交流，可加微信 【添加请备注： 缠论。否则不会添加通过】**

![微信](https://github.com/yijixiuxin/chanlun/raw/main/images/wx.jpg)

### 赞助

开发维护不易，如果觉得项目对你有帮助，还请多多支持

![微信支付](https://github.com/yijixiuxin/chanlun/raw/main/images/wx_pay.jpg)
