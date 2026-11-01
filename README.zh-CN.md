# 加密交易所安全研究

[English](README.md) | **简体中文**

复盘2016年至2026年11月1日的交易所安全事件，追踪攻击者如何接近资金、防御在哪一环失效，以及交易所如何验证自己的防御能力。

研究围绕六条资金攻击路径展开：签名材料泄露、交易内容篡改、账户接管、交易与估值操纵、错误入账与双花，以及客户受骗操作。技术分析同时覆盖钱包、账务、业务风控、研发和安全团队的职责。

## 阅读入口

| 文档 | 内容 | 语言 |
| --- | --- | --- |
| 从 Bybit 到币安：黑客如何攻破交易所 | 五部分调查，包含跨案例比较、攻击归因、响应分析、防御优先级及15幅配图 | [English](docs/en/research.md) · [中文](docs/zh-CN/research.md) |
| 从资损案例看交易所防御 | 18项建设工作，明确专业职能、部门交接和验收证据 | [English](docs/en/defense-matrix.md) · [中文](docs/zh-CN/defense-matrix.md) |
| 交易所六类攻击路径解析 | 攻击机制、逐案依据、调查记录和验证场景 | [English](docs/en/attack-paths.md) · [中文](docs/zh-CN/attack-paths.md) |
| 交易所安全案例目录 | 98条记录，逐案列出资损、攻击过程、归因、证据限制及来源 | [English](docs/en/case-catalogue.md) · [中文](docs/zh-CN/case-catalogue.md) |
| 统计方法与数据说明 | 样本范围、金额口径、响应指标、数据字段和复算方式 | [English](docs/en/methodology.md) · [中文](docs/zh-CN/methodology.md) |

建议先读调查文章，再用防御矩阵检查自身业务。攻击路径解析供应用安全、安全运营、钱包安全和红队人员核对技术细节。

## 研究数据

| 材料 | 范围 |
| --- | --- |
| [事件目录](data/case-registry.csv) | 98条公开事件及线索，其中38条仅有索引材料 |
| [金额样本](data/loss-sample.csv) | 41起有可单独统计估值的事件，合计11,582.86百万美元 |
| [统计结果](data/statistics.json) | 金额分布、年度收录及敏感性计算 |
| [来源索引](data/sources.json) | 底层研究引用的113项来源URL |

正文比较15起案例，并分析12起事件的归因与响应。7项公开时间数据分别记录，起止点不同，不合并计算MTTR。金额采用事发时的名义估值，并非审计后的净损失，复用前请阅读统计说明。

事件目录是公开资料研究样本，不是全部攻击的普查，也不表示每条记录都有完整取证。防御要求属于待验证的建设建议，不代表已经完成生产验收。

## 复算与检查

文档和数据检查仅依赖Python 3.11及以上版本：

```bash
python3 scripts/check.py
```

英文配图使用Matplotlib重新生成：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/render_figures.py
```

中文配图保留原文图表。两种语言均使用仓库相对链接和本地图片，不包含账号凭据、内部系统记录、写作过程文件或发布状态。

## 作者与勘误

- **Max Luo** — 加密交易所AI安全与自动化负责人；[cybermaxluo](https://github.com/cybermaxluo)。
- **Morgan Chen** — 加密交易所AI SOC平台负责人；[Extrader-home](https://github.com/Extrader-home)。

欢迎通过Issue提交更正，请附事件ID、原文位置、来源URL及该来源支持的具体修改。区分已确认事实、调查判断和建议的验证场景。第三方来源内容归各自发布者所有。
