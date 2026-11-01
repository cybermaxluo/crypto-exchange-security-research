# 交易所安全案例目录：2016—2026

[English](../en/case-catalogue.md) | **简体中文**

检索截止：2026-11-01；覆盖2016-01-01至截止日。共98条公开事件及线索。未声称穷尽未公开事件或每条均已完成独立取证。

## 阅读方法

- P：平台、供应商、监管、司法等原始披露；不自动等于独立验证。
- I：调查机构研究；M：媒体或二手转引；C：仅索引线索。组合标签表示不同字段来自不同证据。
- 金额默认为事发时估值或原始币量；冻结、追回、赔付及应对成本不混算。未知根因不填成私钥泄露。
- 归因保留执法确认、研究判断、受害方判断、团伙自称和未知的区别。日期区分发生、发现与披露。
- [金额统计样本](../../data/loss-sample.csv)另选41起可比较事件，数值和逐案排除理由见[统计方法与结果](methodology.md)。

| 范围 | 条目数 |
| --- | ---: |
| 交易所及客户事件 | 90 |
| 关联服务 | 8 |

另有5条存在事件性质或归属争议，状态单列，不作为另一种业务范围。

证据标签分布：P：21；I+M：2；M：15；P+M：3；C：38；I：9；P+C：3；P+I：6；P+I+M：1。标签反映本次检索深度，不代表行业发生率。

## 年度明细

### 2016

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX001<br>2016-03—04 | **ShapeShift**<br>交易所及客户事件 | 约23万美元；三次盗取属同一事件组 | 内部人员协助及终端恶意程序<br>→ 访问凭据与重建环境继续暴露 | 内外部人员协作；个人身份未全部公开 | **P**：重建后仍发生失守；按一个攻击事件组记录<br>[SHAPE](#source-shape) |
| EX002<br>2016-05 | **Gatecoin**<br>交易所及客户事件 | 250 BTC、18.5万 ETH；当时约200万美元 | 服务器入侵；具体入口未公开<br>→ 热钱包资产被转出 | 未知 | **I+M**：不把2019年清算直接归因为这次攻击<br>[GATECOIN](#source-gatecoin) · [SM9](#source-sm9) · [CERT2019](#source-cert2019) |
| EX003<br>2016-08-02 | **Bitfinex**<br>交易所及客户事件 | 约119755 BTC；当时约7200万美元 | 入侵平台；完整初始入口未公开<br>→ 未经授权转出BTC | Ilya Lichtenstein；司法确认 | **P**：Heather Morgan参与洗钱，不记为已确认入侵者；后续追回估值不能替代事发损失<br>[BFDOJ](#source-bfdoj) · [BFFAQ](#source-bffaq) |
| EX004<br>2016-10-13 | **Bitcurex**<br>交易所及客户事件 | 媒体报道约150万美元 | 未披露<br>→ 平台资产外流 | 未知 | **M**：技术根因不足，不补写私钥泄露<br>[BITCUREX](#source-bitcurex) |

### 2017

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX005<br>2017-04 | **Yapizon**<br>交易所及客户事件 | 3831 BTC；披露时约500万美元 | 未披露<br>→ 热钱包失守 | 未知 | **M**：与同年更名后的Youbit事件分开<br>[YOUBIT](#source-youbit) · [SM9](#source-sm9) · [CERT2019](#source-cert2019) |
| EX006<br>2017-06—07披露 | **Bithumb**<br>交易所及客户事件 | 约31800名用户信息；客户资损总额未统一 | 员工电脑被入侵<br>→ 客户信息被用于后续账户欺诈 | 未知 | **M**：数据泄露与平台钱包被清空不同<br>[BITHUMB17](#source-bithumb17) |
| EX007<br>2017-12-19 | **Youbit**<br>交易所及客户事件 | 平台称约17%的资产；美元口径不详 | 未披露<br>→ 再次发生资产外流 | 未知 | **M**：原Yapizon；第二次事件，不能与4月合并为一次<br>[YOUBIT](#source-youbit) |

### 2018

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX008<br>2018-01-26 | **Coincheck**<br>交易所及客户事件 | 526300010 XEM；采用事发时约5.30亿美元估值；后续申报日元口径另列 | 平台调查推定：员工终端感染恶意程序，攻击者经终端进入内网并在NEM服务器侧窃取私钥<br>→ 单一热钱包资产外流 | 未知 | **P+M**：币量、估值及赔付口径有差异；不与后续赔付直接混算<br>[COINCHECK](#source-coincheck) · [SM9](#source-sm9) · [CCFAQ](#source-ccfaq) · [CCUSD](#source-ccusd) |
| EX009<br>2018-02披露 | **BitGrail**<br>交易所及客户事件 | 约1700万NANO；当时约1.7亿美元 | 责任及资金缺口形成过程有争议<br>→ 提现逻辑与平台管理问题需依据司法材料进一步拆分 | 未知 | **M**；性质或归属有争议：不按一场根因明确的外部APT攻击统计<br>[BITGRAIL](#source-bitgrail) |
| EX010<br>2018-03-07 | **Binance VIA**<br>交易所及客户事件 | 攻击者外部提款被拦截；部分受害账户的非授权成交无法撤销，未披露可分离损失总额 | 长期钓鱼取得用户凭据并创建API<br>→ 交易权限被用于跨账户转移价值；后续提现被拦截 | 未知 | **P**：31个预先入金账户卖出VIA；部分受害买单与无辜对手方成交。不能把阻止外部提款等同于客户零损失<br>[VIA](#source-via) |
| EX011<br>2018-04 | **Coinsecure**<br>交易所及客户事件 | 438 BTC；当时约350万美元 | 具体入口及内部人员责任未定<br>→ 钱包密钥处理过程涉嫌暴露 | 内部人员参与属指控，不作为定论 | **C**：恢复操作与内鬼说法须进一步查原始材料<br>[SM9](#source-sm9) |
| EX013<br>2018-06 | **Bithumb**<br>交易所及客户事件 | 初报约3000万—3150万美元 | 未披露<br>→ 热钱包资产外流 | 未知 | **C**：金额后来有修订报道，净损失不据初报推算<br>[SM9](#source-sm9) |
| EX012<br>2018-06-10 | **Coinrail**<br>交易所及客户事件 | 韩联社当时报约3720万美元；其他当时估算约4000万美元 | 平台披露网络入侵，细节不足<br>→ 托管资产外流 | 未知 | **M**：采用当时估算，不换算当前币价<br>[SM9](#source-sm9) · [COINRAILUSD](#source-coinrailusd) |
| EX014<br>2018-09-14 | **Zaif**<br>交易所及客户事件 | 当时约6000万美元 | 未披露<br>→ BTC、BCH、MONA等热钱包外流 | 未知 | **M**：多资产属同一事件<br>[SM9](#source-sm9) · [ZAIFUSD](#source-zaifusd) |
| EX015<br>2018-10-20 | **Trade.io**<br>交易所及客户事件 | 5000万TIO；当时约750万美元 | 未披露<br>→ 平台称冷存储中的代币被转出 | 未知 | **C**：冷存储为受害方描述，不据此推断硬件被破解<br>[SM9](#source-sm9) |
| EX016<br>2018-11-03—06 | **Gate.io / StatCounter**<br>交易所及客户事件 | 未取得可靠总损失数字 | 统计服务JavaScript供应链被污染<br>→ 提现页面中的交易信息被定向篡改 | 未知 | **I**：按提现页面路径、金额或可用余额触发篡改；ESET未取得可靠被盗总额，不记为Gate.io私钥泄露<br>[ESET](#source-eset) |

### 2019

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX017<br>2019-01 | **Gate.io / ETC**<br>交易所及客户事件 | 平台披露收到约10万美元返还；事件总损失待统一 | ETC链重组与双花<br>→ 已入账充值被链上重组撤销 | 未知 | **P**：返还额不等于攻击总额；非交易所服务器入侵<br>[GATEETC](#source-gateetc) |
| EX018<br>2019-01 | **Cryptopia**<br>交易所及客户事件 | 估算约1600万—1750万美元 | 完整入口未公开<br>→ 多地址持续外流 | 未知 | **P+C**：1月后续流出按同一攻击事件组保留；清算期另案不能重复并入<br>[CRYPTOPIA](#source-cryptopia) · [SM8](#source-sm8) |
| EX019<br>2019-01-26 | **LocalBitcoins**<br>交易所及客户事件 | 约7.9 BTC；当时约2.7万美元 | 第三方软件相关漏洞<br>→ 少量用户账户被未授权操作 | 未知 | **C**：不是整个托管钱包余额<br>[SM8](#source-sm8) |
| EX020<br>2019-02-15披露 | **Coinmama**<br>交易所及客户事件 | 约45万条邮件及密码哈希；资损总额未知 | 数据系统被入侵；入口细节未公开<br>→ 客户认证数据泄露 | 未知 | **M**：非45万个钱包被盗<br>[COINMAMA](#source-coinmama) |
| EX021<br>2019-03-24 | **DragonEx**<br>交易所及客户事件 | 约600万—700万美元 | 本库尚未核实完整初始入口<br>→ 多个币种钱包外流 | 未知 | **C**：假交易软件等解释未在本条编码为已证实根因<br>[SM8](#source-sm8) |
| EX022<br>2019-03-29 | **Bithumb**<br>交易所及客户事件 | 约313万EOS及2017万XRP；合计约1900万—2000万美元 | 未披露<br>→ 多资产外流 | 平台怀疑内部人员，未确证 | **C**：EOS与XRP记录合为同一事件<br>[SM8](#source-sm8) |
| EX023<br>2019-05-02 | **BitoPro / XRP**<br>交易所及客户事件 | 索引估约700万XRP；非700万美元 | 充值处理异常，详细原始技术报告待核<br>→ 异常余额及交易回溯 | 未知 | **P+C**：平台公告确认回溯；金额和具体解析错误证据较弱<br>[BITOPRO19](#source-bitopro19) · [SM8](#source-sm8) |
| EX024<br>2019-05-07 | **Binance**<br>交易所及客户事件 | 7000 BTC；当时约4000万美元 | 钓鱼、恶意代码等获取API及2FA信息<br>→ 多账户协同操作通过原有检查并完成提现 | 未知 | **P**：官方通告未把根因定为钱包私钥泄露<br>[BINANCE19](#source-binance19) |
| EX096<br>2019-06-17 | **Coinbase Firefox 双零日攻击**<br>交易所及客户事件 | 平台称阻止攻击，未发生客户资金损失 | 定向社工链接与两项Firefox零日漏洞<br>→ 浏览器执行扩展到终端；后续路径被检测阻断 | Coinbase追踪为CRYPTO-3 / HYDSEVEN；原始复盘未确认国家归属 | **P**：保留成功阻断案例；不能以入侵入口存在推算最终盗币成功<br>[COINBASE19](#source-coinbase19) |
| EX025<br>2019-06-27 | **Bitrue**<br>交易所及客户事件 | 930万XRP及250万ADA；约420万—450万美元 | 平台所述二次审核流程缺陷<br>→ 从用户账户相关权限扩展到热钱包资金 | 未知 | **C**：930万是XRP数量，不是美元<br>[SM7](#source-sm7) |
| EX026<br>2019-07-12 | **BITPoint**<br>交易所及客户事件 | 初报35亿日元；后续口径约30.2亿日元 | 未披露<br>→ 多币种热钱包失守 | 未知 | **C**：修订口径与初报分开<br>[SM7](#source-sm7) |
| EX027<br>2019-11-08 | **VinDAX**<br>交易所及客户事件 | 至少约50万美元 | 未披露<br>→ 热钱包外流 | 未知 | **C**：平台层面的完整技术复盘不足<br>[SM7](#source-sm7) |
| EX028<br>2019-11-27 | **Upbit**<br>交易所及客户事件 | 342000 ETH；当时约4900万美元 | 初始入口未公开<br>→ ETH钱包异常转出 | 索引引述后续政府归因为朝鲜；原始归因文件待补 | **M**：不把热冷调拨时点直接推断为内鬼<br>[SM7](#source-sm7) · [UPBIT19USD](#source-upbit19usd) |

### 2020

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX029<br>2020-02-05—06 | **Altsbit**<br>交易所及客户事件 | 约7万美元BTC及ETH；其他代币另列 | 未披露<br>→ 平台钱包失守 | 未知 | **C**：不是按全部币种完整估值确认的净损失<br>[SM7](#source-sm7) |
| EX030<br>2020-07-11 | **Cashaa**<br>关联服务 | 336 BTC；当时约310万美元 | 平台称操作终端恶意程序<br>→ 相关钱包资金被转走 | 未知 | **C**：加密金融服务商，单列避免与普通CEX完全混同<br>[SM6](#source-sm6) |
| EX031<br>2020-07-31 | **2gether**<br>交易所及客户事件 | 约120万欧元初报；后续美元报道有口径冲突 | 恶意程序相关说法待原始调查核实<br>→ 平台资产被转走 | 后续有嫌疑人被捕报道，未在本库完成司法核验 | **C**：不采用索引700万美元作为无争议损失<br>[CS](#source-cs) · [SM6](#source-sm6) |
| EX032<br>2020-07-31—08 | **OKEx / ETC**<br>交易所及客户事件 | 约560万美元双花损失 | ETC多数算力攻击与重组<br>→ 交易所确认并兑出的充值随后失效 | 未知 | **P**：属于结算最终性风险，不能编码为热钱包密钥泄露<br>[ETC20](#source-etc20) |
| EX033<br>2020-09-08 | **Eterbase**<br>交易所及客户事件 | 约540万美元 | 未披露<br>→ 多币种热钱包外流 | 未知 | **C**：技术入口未确认<br>[SM6](#source-sm6) |
| EX034<br>2020-09-26 | **KuCoin**<br>交易所及客户事件 | 后续平台口径约2.85亿美元；初报更低 | 热钱包私钥受影响；初始获取方式未公开<br>→ 多链钱包外流 | 未知 | **P**：冻结、追回与保险覆盖不是同一金额<br>[KUCOIN20](#source-kucoin20) |
| EX035<br>2020-11-13 | **Liquid**<br>交易所及客户事件 | 用户信息受影响；未确认当次盗币总额 | 域名服务与相关账户遭控制<br>→ 域名/邮件信任链影响内部访问与客户信息 | 未知 | **C**：与2021年资产失窃分开，不自动认定两次同源<br>[SM6](#source-sm6) |
| EX036<br>2020-12-21 | **EXMO**<br>交易所及客户事件 | 平台称约5%资产受影响；媒体估约1050万美元 | 未披露<br>→ 部分热钱包外流 | 未知 | **P+C**：5%采用平台通告；净损失不详<br>[EXMO](#source-exmo) · [SM6](#source-sm6) |
| EX037<br>2020-12-24 | **Livecoin**<br>交易所及客户事件 | 总额未可靠核实 | 平台称失去服务器控制<br>→ 价格及交易系统异常 | 未知 | **C**；性质或归属有争议：不采用流传金额，不把平台说法当完成取证的结论<br>[SM6](#source-sm6) |
| EX038<br>2020-12-26 | **Altilly**<br>交易所及客户事件 | 索引列30 BTC及12000 USDT | 未授权访问；完整入口未核实<br>→ 托管系统与资产受影响 | 未知 | **C**：低披露事件，保留为待深入条目<br>[SM6](#source-sm6) |

### 2021

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX098<br>2021-03—05-20；09-24通知 | **Coinbase SMS账户恢复**<br>交易所及客户事件 | 至少6000名客户发生未授权资金转出；未披露可分离总金额 | 攻击者已掌握客户邮箱、密码、电话号码及邮箱访问；最初取得方式：未知<br>→ SMS账户恢复缺陷使攻击者取得验证令牌，进入客户账户并转出资金 | 未知 | **P**：不等于攻破所有MFA机制；通知未给出发现、修复或恢复的准确时刻<br>[CB21NOTICE](#source-cb21notice) |
| EX039<br>2021-04-29 | **Hotbit**<br>交易所及客户事件 | 平台称资金攻击被阻断；数据与服务受损 | 基础设施入侵<br>→ 业务数据破坏，资金路径未被成功突破 | 未知 | **C**：成功阻断与可用性损害分别记录<br>[SM5](#source-sm5) |
| EX040<br>2021-08-19 | **Liquid**<br>交易所及客户事件 | Elliptic后续估算约9700万美元；初报约8000万美元 | 初始入口未在采用材料中确认<br>→ 多个暖钱包资产外流 | 未知 | **I+M**：不把后来的估价混入初报时点<br>[LIQUID21](#source-liquid21) · [LIQUIDELL](#source-liquidell) |
| EX041<br>2021-08-28—29 | **Bilaxy**<br>交易所及客户事件 | 约2170万美元估算 | 未披露<br>→ 热钱包代币外流 | 未知 | **C**：资产流动性影响可变现价值<br>[SM5](#source-sm5) |
| EX042<br>2021-12-04 | **BitMart**<br>交易所及客户事件 | 平台2026年公告回溯列3.195亿美元（按2021-12-04估值）；初报1.5亿、当时研究约1.96亿 | 平台确认私钥被盗；入口未完整公开<br>→ ETH与BSC两个热钱包受影响 | 未知 | **P**：主统计采用后续平台回溯披露，另做1.96亿美元敏感性比较；未独立审计该回溯总额<br>[BITMART](#source-bitmart) · [BITMART26](#source-bitmart26) |
| EX043<br>2021-12-11 | **AscendEX**<br>交易所及客户事件 | 估约7770万美元 | 未披露<br>→ 多个网络热钱包外流 | 未知 | **P+M**：平台披露重建热钱包并更换充值地址<br>[ASCEND](#source-ascend) · [SM5](#source-sm5) · [ASCENDUSD](#source-ascendusd) |

### 2022

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX044<br>2022-01-08 | **LCX**<br>交易所及客户事件 | 平台后续列约794万美元 | 未公开确认<br>→ 单一热钱包及代币外流 | 未知 | **P**：1月9日为报告日期；冻结额不直接抵扣为已追回<br>[LCX](#source-lcx) · [LCXCOURT](#source-lcxcourt) |
| EX045<br>2022-01-17 | **Crypto.com**<br>交易所及客户事件 | 约3380万—3400万美元；483账户 | 2FA控制被绕过，完整技术根因未公开<br>→ 未获用户正常授权的提现 | 未知 | **M**：旧来源为月度业务回顾，不能支撑事件细节；使用原始通告的公开转引，美元额为约数<br>[CRYPTODGA](#source-cryptodga) · [CRYPTOUSD](#source-cryptousd) |
| EX046<br>2022-02-01 | **Bitbns**<br>交易所及客户事件 | 链上调查估约750万美元 | 未披露<br>→ 热钱包外流；披露滞后 | 未知 | **C**：金额与当时维护公告之间存在争议，需进一步原始核验<br>[SM5](#source-sm5) |
| EX047<br>2022-08-01—02 | **ZB.com**<br>交易所及客户事件 | 疑似约430万—480万美元 | 未披露<br>→ 链上异常外流 | 未知 | **C**；性质或归属有争议：不把疑似外流直接记为已确证外部入侵<br>[SM5](#source-sm5) |
| EX048<br>2022-11-01—02 | **Deribit**<br>交易所及客户事件 | 2800万美元 | 未披露<br>→ BTC、ETH、USDC热钱包资金外流 | 未知 | **M**：平台称由公司储备承担；入口仍未知<br>[DERIBIT](#source-deribit) |
| EX049<br>2022-11-11 | **FTX**<br>交易所及客户事件 | 公开估算约4.77亿美元；早期6亿美元口径混杂 | 完整路径和后续刑事案件映射待逐项核实<br>→ 破产期间未经授权的资产转移 | 未知 | **I**：与挪用、破产缺口及监管保全转账严格区分<br>[CASA](#source-casa) · [SM4](#source-sm4) · [SINBAD](#source-sinbad) |
| EX050<br>2022-12-28披露 | **3Commas / 多家交易所账户**<br>交易所及客户事件 | 至少10万组API数据暴露；相关总资损未可靠统一 | 供应商数据库API数据泄露<br>→ 交易账户被未授权交易 | 未知 | **P**：不是交易所主钱包私钥；暴露条数不等于受害人数<br>[THREEC](#source-threec) · [THREEFAQ](#source-threefaq) |

### 2023

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX097<br>2023-02-05 | **Coinbase 员工社会工程**<br>交易所及客户事件 | 有限企业通讯录信息暴露；平台称客户资金及信息未受影响 | 短信钓鱼取得员工凭据，后续电话社工<br>→ 员工身份信任遭滥用；关键系统访问被阻断 | 平台讨论与既有社工活动相似性，不作司法确认 | **P**：不能据此认定2025年支持人员事件与本次同源<br>[COINBASE23](#source-coinbase23) |
| EX051<br>2023-04-09 | **GDAC**<br>交易所及客户事件 | 约1300万美元；平台称约23%托管资产 | 未披露<br>→ 热钱包外流 | 未知 | **M**：比例是该平台当时口径<br>[GDAC](#source-gdac) |
| EX052<br>2023-04-14 | **Bitrue**<br>交易所及客户事件 | 约2300万美元 | 未披露<br>→ 热钱包外流 | 未知 | **P**：与2019年事件分开<br>[SM4](#source-sm4) · [BITRUE23](#source-bitrue23) |
| EX053<br>2023-04-24 | **KuCoin 社交账号**<br>交易所及客户事件 | 22628 USDT等值，经平台确认 | 官方社交账号被控制<br>→ 假活动引导用户遭受资产损失 | 未知 | **C**：不是KuCoin托管钱包被盗<br>[SM4](#source-sm4) |
| EX054<br>2023-05披露 | **Patricia**<br>交易所及客户事件 | 公开索引约200万美元；事件时间需细分 | 零售交易应用受影响<br>→ BTC及法币相关资产受损 | 未知 | **C**：金额、实际发生时间和后续代币化处理需继续核实<br>[SM4](#source-sm4) |
| EX055<br>2023-06-11 | **Floating Point Group**<br>关联服务 | 约1500万—2000万美元 | 未披露<br>→ 机构交易/托管服务资产损失 | 未知 | **C**：机构经纪与资产管理基础设施，单列<br>[SM4](#source-sm4) |
| EX056<br>2023-07-23 | **CoinList 社交账号**<br>交易所及客户事件 | 未取得可靠损失数字 | 社交账号被控制<br>→ 虚假代币销售链接 | 未知 | **C**：不将无已知资损写成零损失<br>[SM4](#source-sm4) |
| EX057<br>2023-09-07 | **Fortress Trust**<br>关联服务 | 约1200万—1500万美元 | 第三方云工具供应商受影响<br>→ 托管客户资产被转走 | 未知 | **C**：属于托管基础设施依赖，不是普通CEX<br>[SM4](#source-sm4) |
| EX058<br>2023-09-12 | **CoinEx**<br>交易所及客户事件 | 后续估算约7000万美元 | 热钱包私钥受影响的初步判断<br>→ 多链资产外流 | 研究机构指向朝鲜；本库尚未补齐原始归因报告 | **I**：初始数额明显较低；密钥入口未公开<br>[SM4](#source-sm4) · [SINBAD](#source-sinbad) |
| EX059<br>2023-09-14 | **Remitano**<br>交易所及客户事件 | 疑似270万美元；约140万美元被冻结 | 未披露<br>→ 异常大额转账 | 未知 | **C**；性质或归属有争议：疑似被盗与冻结分别记；不将冻结算作归还<br>[SM4](#source-sm4) |
| EX060<br>2023-09-24 | **HTX**<br>交易所及客户事件 | 约5000 ETH；当时约800万—820万美元 | 未披露<br>→ 热钱包外流 | 未知 | **C**：与11月HTX/HECO事件分开<br>[SM4](#source-sm4) |
| EX061<br>2023-09-24 | **Upbit / 假APT**<br>交易所及客户事件 | 未确认统一资损 | 充值资产识别异常，细节待原始核实<br>→ 非预期代币被记为APT并进入交易 | 未知 | **C**：不把第三方推断的解析根因当平台确认<br>[SM3](#source-sm3) |
| EX062<br>2023-10-17 | **Coins.ph**<br>交易所及客户事件 | 约1220万XRP；当时约600万美元 | 未公开确认<br>→ 异常XRP转出 | 未知 | **M**；性质或归属有争议：采用报道的疑似攻击性质；不是1220万美元<br>[COINSPH](#source-coinsph) |
| EX063<br>2023-11-08 | **CoinSpot**<br>交易所及客户事件 | 约1283 ETH；约247万美元 | 未公开确认<br>→ 两个热钱包外流 | 未知 | **C**：不由链上签名反推密钥泄露<br>[SM3](#source-sm3) |
| EX064<br>2023-11-10 | **Poloniex**<br>交易所及客户事件 | CertiK估约1.32亿美元；其他研究约1.30亿美元 | CertiK按密钥失陷分析，初始入侵及密钥如何暴露未完整披露<br>→ 多资产钱包外流 | 有朝鲜关联研究判断，未在本库作确定归因 | **I**：估值与覆盖资产差异待统一<br>[SM3](#source-sm3) · [CASA](#source-casa) · [POLOCERT](#source-polocert) |
| EX065<br>2023-11-22 | **HTX / HECO 关联事件**<br>交易所及客户事件 | 合并估约1.13亿美元；含桥及交易所，不能全算CEX | 未公开确认<br>→ HTX钱包与HECO桥同期外流 | 未知 | **C**：保留一个关联事件组；需拆分后才能参与CEX金额统计<br>[SM3](#source-sm3) |
| EX066<br>2023-12-20披露 | **INX 关联供应商**<br>关联服务 | 约160万美元 | 第三方供应商服务器被入侵<br>→ 未经授权交易使子公司损失 | 未知 | **C**：强调交易系统依赖；金额不等于主钱包被盗<br>[SM3](#source-sm3) |

### 2024

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX067<br>2024-02-18披露 | **FixedFloat**<br>关联服务 | 约2610万美元 | 完整入口未在采用材料中确认<br>→ 即时兑换服务资产被盗 | 未知 | **C**：不把自称非托管或索引DEX标签作为架构定论<br>[SM3](#source-sm3) |
| EX068<br>2024-03-31—04-01 | **FixedFloat**<br>关联服务 | 约280万—300万美元 | 平台称第三方托管服务相关问题<br>→ 再次发生资产外流 | 未知 | **C**：与2月事件分开；未证明相同初始入口<br>[SM3](#source-sm3) |
| EX069<br>2024-04-29 | **Rain**<br>交易所及客户事件 | 链上研究估约1480万美元 | 未公开确认<br>→ 多个钱包异常外流 | 未知 | **I**：根因与团伙未定<br>[SM2](#source-sm2) · [SM2024](#source-sm2024) |
| EX070<br>2024-05-31 | **DMM Bitcoin**<br>交易所及客户事件 | 4502.9 BTC；约3.05亿—3.08亿美元 | 假招聘测试侵入Ginco员工终端并取得会话<br>→ 供应商通信访问被判断很可能用于操纵合法交易请求 | TraderTraitor；FBI/DC3/NPA归因 | **P**：操纵具体交易请求保留调查中的likely措辞；监管缺陷不等于已证明被利用<br>[DMM](#source-dmm) · [DMMREG](#source-dmmreg) |
| EX072<br>2024-06-09报告 | **Kraken 入账漏洞**<br>交易所及客户事件 | 争议研究提款约300万美元；不作永久净损失统计 | 入账实现缺陷<br>→ 未完成真实充值即可形成余额 | CertiK Skyfall 团队；漏洞利用范围存在争议 | **P**：不归为Lazarus或普通刑事盗币；技术机制与争议分开<br>[KRAKEN](#source-kraken) · [CERTIK24](#source-certik24) |
| EX073<br>2024-06-22 | **BtcTurk**<br>交易所及客户事件 | 研究及报道约5400万—5500万美元；平台确认热钱包受影响 | 未披露<br>→ 部分资产热钱包受影响 | 未知 | **M**：钱包归属及金额包含研究者的时点关联判断；不把冻结530万美元当作已追回<br>[SM2](#source-sm2) · [CASA](#source-casa) · [BTCTURK24](#source-btcturk24) |
| EX071<br>2024-06上旬 | **Lykke**<br>交易所及客户事件 | 估约2240万—2280万美元 | 未披露<br>→ 平台资产外流 | 未知 | **C**：发生与披露日期有差异，不用索引日期假装精确发生时间<br>[SM2](#source-sm2) |
| EX074<br>2024-07-18 | **WazirX**<br>交易所及客户事件 | 超过2.3亿美元；常见约2.35亿美元 | 交易所与Liminal之间具体责任链存在争议<br>→ 多签钱包出现未经预期的交易执行 | 有朝鲜关联归因；本条不据争议材料确认全部链路 | **P+I**：受害方通告不是对供应商责任的独立裁定<br>[WAZIR](#source-wazir) · [WAZIRELL](#source-wazirell) |
| EX075<br>2024-09-11 | **Indodax**<br>交易所及客户事件 | 约2200万美元 | 未确认；提现系统受影响属研究推测<br>→ 多资产外流 | 未知 | **I**：不能将研究排除/怀疑当最终根因<br>[SM2](#source-sm2) · [SM2024](#source-sm2024) |
| EX076<br>2024-09-20 | **BingX**<br>交易所及客户事件 | 索引估约4500万美元；外部估算不同 | 未披露<br>→ 热钱包异常转出 | 未知 | **I**：净损失及恢复另行核对<br>[SM2](#source-sm2) · [SM2024](#source-sm2024) |
| EX077<br>2024-10-31 | **M2**<br>交易所及客户事件 | 约1370万美元 | 未披露<br>→ 多链热钱包外流 | 未知 | **C**：具体入口未公开<br>[SM2](#source-sm2) |
| EX078<br>2024-11-28 | **XT.com**<br>交易所及客户事件 | 约170万美元 | 未披露<br>→ 平台资产异常转出 | 未知 | **C**：不把异常流出自动解释为密钥泄露<br>[SM2](#source-sm2) |

### 2025

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX079<br>2025-01-01 | **NoOnes**<br>关联服务 | 约790万美元 | 平台称Solana桥相关攻击<br>→ P2P服务关联桥/钱包资产受损 | 未知 | **C**：不能与纯CEX钱包事件不加区分地合计<br>[SM1](#source-sm1) |
| EX080<br>2025-01-23 | **Phemex**<br>交易所及客户事件 | Immunefi及SlowMist约6910万美元；后续媒体另报8500万美元，口径差异保留 | 未披露完整链路<br>→ 多链热钱包外流 | 有朝鲜关联研究判断，未在本库确证 | **P+I+M**：金额为不同估算区间<br>[SM1](#source-sm1) · [CASA](#source-casa) · [PHEMEX](#source-phemex) · [PHEMEX69](#source-phemex69) · [PHEMEX85](#source-phemex85) |
| EX081<br>2025-02-21 | **Bybit**<br>交易所及客户事件 | 约14.6亿—15亿美元 | Safe开发者终端及AWS会话被侵入<br>→ 前端污染待签名交易，影响冷钱包资产控制 | TraderTraitor；FBI归因 | **P+I**：不是多签密码算法被破解的证据<br>[BYBIT](#source-bybit) · [BYFBI](#source-byfbi) |
| EX082<br>2025-05-08 UTC | **BitoPro**<br>交易所及客户事件 | 约1150万美元 | 云运维人员遭社工，恶意程序及AWS会话劫持<br>→ 钱包升级迁移期间模拟正常操作转移资产 | 平台认为手法与Lazarus Group相似；非司法确认 | **P+I**：平台当地通告记5月9日凌晨，属于时区差异<br>[BITOPRO25](#source-bitopro25) · [SM1](#source-sm1) · [SM2025H1](#source-sm2025h1) |
| EX083<br>2025-05-15披露 | **Coinbase 支持人员事件**<br>交易所及客户事件 | 1.8亿—4亿美元为初步应对及自愿赔付成本，不是钱包失窃总额 | 部分外包支持人员被收买<br>→ 客户信息泄露并被用于社会工程欺诈 | 未知 | **P**：数据访问权限不等于直接提现权限，但能影响后续欺诈<br>[COINBASE](#source-coinbase) · [COINBASESEC](#source-coinbasesec) |
| EX084<br>2025-06-18 | **Nobitex**<br>交易所及客户事件 | 超过9000万美元 | 完整入口未公开<br>→ 资产转往被判断难以恢复控制的销毁地址 | Gonjeshke Darande / Predatory Sparrow自称负责 | **I**：政治动机及销毁行为区别于通常洗钱；不等于国家归因已证实<br>[NOBITEX](#source-nobitex) |
| EX085<br>2025-07-16 | **BigONE**<br>交易所及客户事件 | 约2700万美元 | 第三方攻击及生产环境受影响<br>→ 账户与风控相关逻辑遭操纵；平台称私钥安全 | 未知 | **P+M**：公开说明仍非完整独立取证报告<br>[BIGONE](#source-bigone) · [BIGLOGIC](#source-biglogic) · [SM1](#source-sm1) · [BIGUSD](#source-bigusd) |
| EX086<br>2025-07-19 | **CoinDCX**<br>交易所及客户事件 | 约4420万美元 | 平台称服务器被侵入<br>→ 合作交易所流动性用途的内部运营账户受影响 | 未知 | **P+I**：与主客户冷钱包区分；与2026旧地址损失建立事件关联<br>[CDX25](#source-cdx25) · [SM1](#source-sm1) · [SM2025](#source-sm2025) |
| EX087<br>2025-07-24 | **WOO X**<br>交易所及客户事件 | 1400万美元；9个账户 | 外部协作项目恶意程序侵入开发者终端<br>→ 开发环境、Kubernetes权限及数据库访问扩展至账户与提现 | 平台判断涉及UNC4899/UNC5565等朝鲜活动；措辞存在差异 | **P**：不把所有别名视为无条件完全等价；保留受害方判断层级<br>[WOO](#source-woo) |
| EX088<br>2025-08-14 | **BtcTurk**<br>交易所及客户事件 | Beosin资金追踪采用约4800万美元；其他目录口径另有差异 | 未披露<br>→ 热钱包外流 | 未知 | **I**：独立于2024年事件<br>[SM1](#source-sm1) · [CASA](#source-casa) · [BTCTURK25](#source-btcturk25) |
| EX089<br>2025-08-31操作；09-08发现 | **SwissBorg / Kiln**<br>关联服务 | 约19.2万SOL；当时约4100万—4150万美元 | Kiln工程师GitHub令牌失窃，经CI取得基础设施凭据<br>→ 交易构造API返回恶意交易，客户签名后提款权限改变 | 未知 | **P**：Kiln复盘区分8月31日签署恶意交易和9月8日发现；不能把两日混为同一时间点<br>[KILN](#source-kiln) · [SWISS](#source-swiss) |
| EX090<br>2025-11-27 | **Upbit**<br>交易所及客户事件 | 后续估约445亿韩元，约3030万美元 | 未确认<br>→ Solana相关资产异常外流 | 未知 | **M**：发现过潜在密钥推断问题，不等于已证明本次根因<br>[SM1](#source-sm1) · [UPBIT25USD](#source-upbit25usd) |

### 2026

| 编号 / 时间 | 平台及范围 | 资损或影响口径 | 入口 → 失守环节 | 团伙与归因 | 证据、限制与来源 |
| --- | --- | --- | --- | --- | --- |
| EX092<br>2026-03—07；07-19上报 | **KuCoin / Zilliqa Ledger应用**<br>交易所及客户事件 | KuCoin单独损失未披露；生态统计不并作交易所损失 | 旧版签名应用nonce处理缺陷<br>→ 公开签名可暴露特定账户私钥 | 未知 | **P**：链项目称KuCoin冷钱包异常触发上报；生态约6.83亿ZIL统计含后续流转，不直接视为CEX净损失<br>[ZIL](#source-zil) |
| EX091<br>2026-04-16 | **Grinex**<br>交易所及客户事件 | 约1310万—1500万美元估算 | 未披露<br>→ 钱包资产外流后转换资产 | 平台指责敌对国家；独立归因未确认 | **C**：不把受害方政治指控当取证结论<br>[SM1](#source-sm1) |
| EX093<br>2026-09-24 | **Bitget**<br>交易所及客户事件 | 修订为3.875亿美元；初报3.516亿美元 | 第三方安全产品漏洞取得高权限内部凭据<br>→ 伪造提现命令经钱包系统执行 | Chainalysis归因朝鲜；注明机构判断 | **P+I**：平台排除私钥泄露；金额上调来自补充核算，不是持续失窃<br>[BITGET](#source-bitget) · [BGAMT](#source-bgamt) · [BGCHAIN](#source-bgchain) |
| EX094<br>2026-10-21 | **CoinDCX 旧钱包**<br>交易所及客户事件 | 1599万USDT | 完整攻击手法未公开；受影响为已退役旧基础设施<br>→ 旧地址继续收款，先记账后归集，归集失效后出现资产损失 | 未知 | **P**：关联2025事件；不是已证实的第二次新密钥窃取<br>[CDX26](#source-cdx26) |
| EX095<br>2026-10-29 | **Binance**<br>交易所及客户事件 | 平台后续约63亿美元；冻结不等于追回 | 平台初查指向DevOps终端失陷、服务容器被访问；后续发现其他入侵点<br>→ 初步披露容器内提交未授权提现；完整权限与资金操作链路仍待调查 | TraderTraitor；FBI归因 | **P+I**：平台称尚无钱包私钥泄露证据；DevOps链路属于初步判断，授权取得细节未披露<br>[BNINITIAL26](#source-bninitial26) · [BINANCE26](#source-binance26) · [BNFBI](#source-bnfbi) · [BNELL](#source-bnell) |

## 来源索引

<a id="source-sm1"></a>
- **SM1 · 索引**：[SlowMist 事件索引，第 1 页](https://hacked.slowmist.io/?c=Exchange)

<a id="source-sm2"></a>
- **SM2 · 索引**：[SlowMist 事件索引，第 2 页](https://hacked.slowmist.io/?c=Exchange&page=2)

<a id="source-sm3"></a>
- **SM3 · 索引**：[SlowMist 事件索引，第 3 页](https://hacked.slowmist.io/?c=Exchange&page=3)

<a id="source-sm4"></a>
- **SM4 · 索引**：[SlowMist 事件索引，第 4 页](https://hacked.slowmist.io/?c=Exchange&page=4)

<a id="source-sm5"></a>
- **SM5 · 索引**：[SlowMist 事件索引，第 5 页](https://hacked.slowmist.io/?c=Exchange&page=5)

<a id="source-sm6"></a>
- **SM6 · 索引**：[SlowMist 事件索引，第 6 页](https://hacked.slowmist.io/?c=Exchange&page=6)

<a id="source-sm7"></a>
- **SM7 · 索引**：[SlowMist 事件索引，第 7 页](https://hacked.slowmist.io/?c=Exchange&page=7)

<a id="source-sm8"></a>
- **SM8 · 索引**：[SlowMist 事件索引，第 8 页](https://hacked.slowmist.io/?c=Exchange&page=8)

<a id="source-sm9"></a>
- **SM9 · 索引**：[SlowMist 事件索引，第 9 页](https://hacked.slowmist.io/?c=Exchange&page=9)

<a id="source-casa"></a>
- **CASA · 索引**：[Casa 事件目录；含倒闭与冻结，不能直接视为盗币总表](https://casa.io/exchange-hacks)

<a id="source-cs"></a>
- **CS · 索引**：[ChainSec 事件目录；日期、币量与美元口径存在错误，需逐项核对](https://www.chainsec.io/exchange-hacks)

<a id="source-shape"></a>
- **SHAPE · 原始报告存档**：[ShapeShift / Ledger Labs 复盘存档](https://postmortem.io/incidents/shapeshift--2016-04-19--cyberattack-postmortem/)

<a id="source-gatecoin"></a>
- **GATECOIN · 研究记录**：[Gatecoin 事件研究记录](https://www.csidb.net/csidb/incidents/8673c914-86b4-47c8-b3fe-0e776431f512/)

<a id="source-bfdoj"></a>
- **BFDOJ · 司法**：[美国司法部：2016 Bitfinex 案](https://www.justice.gov/usao-dc/2016-bitfinex-hack)

<a id="source-bffaq"></a>
- **BFFAQ · 平台**：[Bitfinex 2016 事件与追回 FAQ](https://support.bitfinex.com/hc/en-us/articles/4417401349657-2016-Security-Breach-Bitcoin-Recovery-Frequently-Asked-Questions-FAQ)

<a id="source-bitcurex"></a>
- **BITCUREX · 媒体**：[Bitcurex 事件报道](https://news.bitcoin.com/bitcurex-forced-million-theft/)

<a id="source-youbit"></a>
- **YOUBIT · 媒体**：[韩联社：Youbit 二次事件](https://en.yna.co.kr/view/AEN20171219015800320)

<a id="source-bithumb17"></a>
- **BITHUMB17 · 媒体**：[Bithumb 员工电脑与客户信息事件](https://bravenewcoin.com/insights/fourth-largest-bitcoin-exchange-bithumb-hacked-for-billions-of-won)

<a id="source-coincheck"></a>
- **COINCHECK · 公司申报**：[Coincheck SEC 披露](https://www.coincheckgroup.com/sec-filings/all-sec-filings/content/0001213900-25-007203/0001213900-25-007203.pdf)

<a id="source-bitgrail"></a>
- **BITGRAIL · 媒体**：[BitGrail 初始事件报道](https://techcrunch.com/2018/02/12/bitgrail-hack-nano/)

<a id="source-via"></a>
- **VIA · 平台**：[Binance VIA 钓鱼与盗币未遂复盘](https://www.binance.com/en/support/announcement/detail/360001547431)

<a id="source-eset"></a>
- **ESET · 调查**：[ESET：StatCounter 定向攻击 Gate.io](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/)

<a id="source-gateetc"></a>
- **GATEETC · 平台**：[Gate：ETC 双花资金部分返还](https://www.gate.com/ru/announcements/article/16740)

<a id="source-cryptopia"></a>
- **CRYPTOPIA · 清算材料**：[Cryptopia 清算人宣誓材料](https://www.grantthornton.co.nz/globalassets/1.-member-firms/new-zealand/pdfs/cryptopia/2023/affidavit-of-david-ian-ruscoe-in-support-of-originating-application-1.pdf)

<a id="source-coinmama"></a>
- **COINMAMA · 媒体**：[Coinmama 450000 条信息泄露](https://www.ccn.com/breaking-major-crypto-brokerage-coinmama-hacked-450000-users-affected-in-massive-worldwide-breach/)

<a id="source-binance19"></a>
- **BINANCE19 · 平台**：[Binance 2019 安全事件通告](https://www.binance.com/en-AU/support/announcement/detail/360028031711)

<a id="source-bitopro19"></a>
- **BITOPRO19 · 平台**：[BitoPro XRP 账户回溯处理](https://www.bitopro.com/ns/announcements/173)

<a id="source-etc20"></a>
- **ETC20 · 链项目**：[ETC Cooperative 2020 年 8 月董事会资料](https://etccooperative.org/ETC-Coop-Board-Package-August-2020.pdf)

<a id="source-kucoin20"></a>
- **KUCOIN20 · 平台**：[KuCoin CEO 2020 年总结](https://www.kucoin.com/fil/announcement/a-letter-from-kucoin-ceo-2020-2021-and-beyond)

<a id="source-exmo"></a>
- **EXMO · 平台**：[EXMO 安全事件更新](https://exmo.com/blog/en/notifications/exmo-security-incident-update)

<a id="source-liquid21"></a>
- **LIQUID21 · 媒体**：[Liquid 2021 初报](https://cointelegraph.com/news/breaking-liquid-exchange-hacked-to-the-tune-of-80-million)

<a id="source-bitmart"></a>
- **BITMART · 平台**：[BitMart 事件更新与原因说明](https://www.bitmart.com/en-US/support/articles/7922665245339/7923672421147/4411998987419)

<a id="source-ascend"></a>
- **ASCEND · 平台**：[AscendEX 2021 重建及恢复通告](https://ascendex.com/hi/support/articles/62199-dec-11-security-incident-timing-for-resuming-deposit-and-withdraw)

<a id="source-lcx"></a>
- **LCX · 平台**：[LCX 事件报告](https://lcx.com/de/hot-wallet-incident-report)

<a id="source-cryptocom"></a>
- **CRYPTOCOM · 平台**：[Crypto.com 2022 年 1 月回顾](https://crypto.com/nl/company-news/crypto-com-january-2022-updates/)

<a id="source-deribit"></a>
- **DERIBIT · 媒体**：[Deribit 热钱包事件报道](https://cointelegraph.com/news/deribit-crypto-exchange-halts-withdrawals-amid-28m-hot-wallet-hack)

<a id="source-threec"></a>
- **THREEC · 平台**：[3Commas API 数据泄露通告](https://3commas.io/blog/notice-on-api-data-disclosure-incident)

<a id="source-threefaq"></a>
- **THREEFAQ · 平台**：[3Commas API 泄露 FAQ](https://3commas.io/blog/api-security-incident-faq)

<a id="source-gdac"></a>
- **GDAC · 媒体**：[GDAC 事件报道](https://www.coindesk.com/tech/2023/04/10/s-korean-crypto-exchange-gdac-hacked-for-nearly-13m)

<a id="source-coinsph"></a>
- **COINSPH · 媒体**：[Coins.ph XRP 外流报道](https://www.theblock.co/news/business/2023-10-20-philippines-based-exchange-coins-ph-appears-to-have-lost-12-2-million-xrp-in-possible-exploit-258701)

<a id="source-dmm"></a>
- **DMM · 执法调查**：[FBI/DC3/NPA：DMM Bitcoin 攻击链与归因](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom)

<a id="source-dmmreg"></a>
- **DMMREG · 监管**：[关东财务局对 DMM Bitcoin 的检查](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html)

<a id="source-kraken"></a>
- **KRAKEN · 平台**：[Kraken：入账漏洞披露](https://blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug)

<a id="source-wazir"></a>
- **WAZIR · 平台**：[WazirX 多签钱包事件通告](https://wazirx.com/blog/important-update-cyber-attack-incident-and-measures-to-protect-your-assets/)

<a id="source-bybit"></a>
- **BYBIT · 调查**：[Sygnia：Bybit 调查分析](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/)

<a id="source-byfbi"></a>
- **BYFBI · 执法调查**：[FBI：Bybit 归因](https://www.ic3.gov/PSA/2025/PSA250226)

<a id="source-bitopro25"></a>
- **BITOPRO25 · 平台**：[BitoPro 2025 年 6 月 19 日调查说明](https://www.bitopro.com/ns/en-US/announcements/1226)

<a id="source-coinbase"></a>
- **COINBASE · 平台**：[Coinbase：支持人员被收买与数据泄露](https://www.coinbase.com/en-nl/blog/protecting-our-customers-standing-up-to-extortionists)

<a id="source-coinbasesec"></a>
- **COINBASESEC · 公司申报**：[Coinbase 2025 年 5 月 15 日 8-K](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm)

<a id="source-nobitex"></a>
- **NOBITEX · 调查**：[Chainalysis：Nobitex 攻击与销毁地址](https://www.chainalysis.com/blog/nobitex-iranian-exchange-exploit-june-2025/)

<a id="source-bigone"></a>
- **BIGONE · 平台**：[BigONE 2025 年 7 月 16 日通告](https://bigone.zendesk.com/hc/en-us/articles/48906456010393-Announcement-Regarding-BigONE-Security-Incident-on-16-July-2025)

<a id="source-biglogic"></a>
- **BIGLOGIC · 关联平台**：[BigONE Eurasia 对全球平台事件的说明](https://bigoneeurasia.ladesk.com/275817-Temporary-Platform-Maintenance)

<a id="source-cdx25"></a>
- **CDX25 · 平台**：[CoinDCX 2025 年 7 月 19 日事件报告](https://coindcx.com/blog/announcements/incident-report-july-19-2025)

<a id="source-woo"></a>
- **WOO · 平台**：[WOO X 7 月 24 日事件复盘](https://woox.io/blog/july-24th-security-incident-post-mortem)

<a id="source-kiln"></a>
- **KILN · 供应商**：[Kiln 2025 年 10 月 7 日复盘](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information)

<a id="source-swiss"></a>
- **SWISS · 平台**：[SwissBorg：Kiln 事件调查更新](https://swissborg.com/blog/swissborg-security-update-kiln-breach)

<a id="source-zil"></a>
- **ZIL · 链项目**：[Zilliqa：旧版签名应用 nonce 缺陷复盘](https://www.zilliqa.com/ledger-incident/post-mortem/)

<a id="source-bitget"></a>
- **BITGET · 平台**：[Bitget 事件调查说明，更新至 2026 年 10 月 20 日](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)

<a id="source-bgamt"></a>
- **BGAMT · 平台**：[Bitget 2026 年 9 月 25 日金额修订](https://www.bitget.com/support/articles/12560603896108)

<a id="source-bgchain"></a>
- **BGCHAIN · 调查**：[Chainalysis：Bitget 调查](https://www.chainalysis.com/blog/387m-bitget-theft-2026/)

<a id="source-cdx26"></a>
- **CDX26 · 平台**：[CoinDCX 2026 年旧钱包活动通告](https://coindcx.com/blog/coindcx-news/on-chain-wallet-activity-update-21-oct-2026)

<a id="source-binance26"></a>
- **BINANCE26 · 平台**：[Binance 2026 年 10 月 30 日通告](https://www.binance.com/en-TR/support/announcement/detail/d3306d9dca5243548c813b605e1d1751)

<a id="source-bnfbi"></a>
- **BNFBI · 执法调查**：[FBI：Binance 2026 事件归因](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack)

<a id="source-eip"></a>
- **EIP · 技术规范**：[EIP-7702 规范](https://eips.ethereum.org/EIPS/eip-7702)

<a id="source-erc20"></a>
- **ERC20 · 技术规范**：[ERC-20：代币授权与转账规范](https://eips.ethereum.org/EIPS/eip-20)

<a id="source-ai"></a>
- **AI · 威胁研究**：[GTIG：从提示辅助到自主工作流，2026 年 9 月](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai)

<a id="source-iso"></a>
- **ISO · 标准**：[ISO/IEC 27001:2022 标准说明](https://www.iso.org/standard/27001)

<a id="source-maple"></a>
- **MAPLE · 媒体**：[MapleChange 事件及退出诈骗争议报道](https://blockonomi.com/maplechange-hacked-scam/)

<a id="source-coinbase19"></a>
- **COINBASE19 · 平台**：[Coinbase：Firefox 双零日攻击及阻断复盘](https://www.coinbase.com/blog/responding-to-firefox-0-days-in-the-wild)

<a id="source-coinbase23"></a>
- **COINBASE23 · 平台**：[Coinbase：2023 年员工社会工程事件](https://www.coinbase.com/en-ca/blog/social-engineering-a-coinbase-case-study)

<a id="source-elliptic23"></a>
- **ELLIPTIC23 · 调查**：[Elliptic：2023 年朝鲜关联攻击与资金联系](https://www.elliptic.co/insights/how-the-lazarus-group-is-stepping-up-crypto-hacks-and-changing-its-tactics/)

<a id="source-ccfaq"></a>
- **CCFAQ · 平台**：[Coincheck 2018 事件官方 FAQ](https://coincheck.com/info/faq_nem)

<a id="source-ccusd"></a>
- **CCUSD · 媒体**：[Reuters：Coincheck 事发时美元估值](https://www.investing.com/news/stock-market-news/exclusive-coincheck-hackers-attempting-to-sell-stolen-cryptocurrency--executive-1171410)

<a id="source-coinrailusd"></a>
- **COINRAILUSD · 媒体**：[韩联社：Coinrail 2018 事件](https://en.yna.co.kr/view/AEN20180611009700320)

<a id="source-zaifusd"></a>
- **ZAIFUSD · 媒体**：[Reuters：Zaif 2018 事件](https://www.investing.com/news/cryptocurrency-news/japan-hit-by-another-cryptocurrency-heist-60-million-stolen-1616872)

<a id="source-upbit19usd"></a>
- **UPBIT19USD · 媒体**：[Korea Times：Upbit 2019 事件](https://www.koreatimes.co.kr/economy/20191128/security-concerns-grow-over-cryptocurrency-exchanges)

<a id="source-liquidell"></a>
- **LIQUIDELL · 调查**：[Elliptic：Liquid 2021 估算与资产转换](https://www.elliptic.co/insights/liquid-exchange-hacked-94-million-stolen/)

<a id="source-bitmart26"></a>
- **BITMART26 · 平台**：[BitMart：2026 年方案公告中修订 2021 年事件金额](https://bitmart.zendesk.com/hc/en-us/articles/56571281537051-Announcement-on-BitMart-s-Initial-Indicative-Proposal-and-Roadmap)

<a id="source-ascendusd"></a>
- **ASCENDUSD · 媒体**：[The Block：AscendEX / PeckShield 金额估算](https://www.theblock.co/news/regulation/2021-12-12-crypto-exchange-ascendex-hacked-for-78-million-in-latest-swindle-127231)

<a id="source-lcxcourt"></a>
- **LCXCOURT · 诉讼附件**：[LCX 公开诉讼附件：资金追踪报告](https://www.hklaw.com/-/media/files/generalpages/lcx-ag-v-doe/exhibit2_nyscefno8.pdf?la=en)

<a id="source-cryptodga"></a>
- **CRYPTODGA · 研究转引**：[DGA 研究对 Crypto.com 原始通告的记录](https://dga.gov.sa/sites/default/files/2023-08/Digital%20Fraud%20-%20Research%20Study.pdf)

<a id="source-sinbad"></a>
- **SINBAD · 调查**：[Elliptic：Sinbad 相关案件的资金规模](https://www.elliptic.co/insights/sinbad-crypto-mixer-flagged-by-elliptic-sanctioned-and-seized/)

<a id="source-bitrue23"></a>
- **BITRUE23 · 平台**：[Bitrue：2023 年 4 月 14 日安全通告](https://support.bitrue.com/hc/en-001/articles/17538384324121-Update-on-Bitrue-s-Security-Breach)

<a id="source-polocert"></a>
- **POLOCERT · 调查**：[CertiK：Poloniex 事件分析](https://www.certik.com/blog/poloniex-incident-analysis)

<a id="source-sm2024"></a>
- **SM2024 · 调查汇编**：[SlowMist：2024 年度报告](https://www.slowmist.com/report/2024-Blockchain-Security-and-AML-Annual-Report%28EN%29.pdf)

<a id="source-btcturk24"></a>
- **BTCTURK24 · 媒体**：[The Block：BtcTurk 2024 年异常外流与冻结](https://www.theblock.co/news/regulation/2024-06-22-binance-freezes-5-million-in-funds-looted-from-btcturk-after-alleged-54-million-hack-of-turkish-exchange-301340)

<a id="source-wazirell"></a>
- **WAZIRELL · 调查**：[Elliptic：WazirX 资金追踪](https://www.elliptic.co/insights/235-million-lost-by-wazirx-in-north-korea-linked-breach/)

<a id="source-phemex"></a>
- **PHEMEX · 平台**：[Phemex：2025 年 1 月事件时间线](https://phemex.com/announcements/phemex-hot-wallet-security-incident-update-and-timeline)

<a id="source-phemex69"></a>
- **PHEMEX69 · 调查汇编**：[Immunefi：2025 年 1 月损失报告](https://assets.ctfassets.net/t3wqy70tc3bv/1Vj4VSUY97UCFp3mLgG7ov/f1de70826f9c2992c481b124d849aa55/Immunefi_Crypto_Losses_January_2025.pdf)

<a id="source-phemex85"></a>
- **PHEMEX85 · 媒体**：[BleepingComputer：Phemex 后续金额报道](https://www.bleepingcomputer.com/news/security/hackers-steal-85-million-worth-of-cryptocurrency-from-phemex/amp/)

<a id="source-sm2025h1"></a>
- **SM2025H1 · 调查汇编**：[SlowMist：2025 上半年报告](https://www.slowmist.com/report/SlowMist-first-half-of-the-2025-report%28EN%29.pdf)

<a id="source-sm2025"></a>
- **SM2025 · 调查汇编**：[SlowMist：2025 年度报告](https://www.slowmist.com/report/2025-Blockchain-Security-and-AML-Annual-Report%28EN%29.pdf)

<a id="source-bigusd"></a>
- **BIGUSD · 媒体**：[The Block：BigONE 事件及金额](https://www.theblock.co/news/regulation/2025-07-16-bigone-hack-362814)

<a id="source-btcturk25"></a>
- **BTCTURK25 · 调查**：[Beosin：BtcTurk 2025 年资金追踪](https://www.beosin.com/resources/fund-flow-analysis-of-btcturk-48-million-hack)

<a id="source-upbit25usd"></a>
- **UPBIT25USD · 媒体**：[Korea Times：Upbit 2025 年金额口径](https://www.koreatimes.co.kr/economy/cryptocurrency/20251208/repeat-cyberthefts-raise-questions-about-upbits-security-governance)

<a id="source-bnell"></a>
- **BNELL · 调查**：[Elliptic：Binance 2026 年链上估算](https://www.elliptic.co/insights/binance-largest-hack-in-history/)

<a id="source-cert2019"></a>
- **CERT2019 · 研究汇编**：[CERT-EU：2019 年加密平台攻击备忘录](https://cert.europa.eu/publications/threat-intelligence/threat-memo-191126-1/pdf)

<a id="source-ca2025"></a>
- **CA2025 · 调查**：[Chainalysis：2025 年被盗资金研究](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026-/)

<a id="source-cryptousd"></a>
- **CRYPTOUSD · 媒体**：[The Block：Crypto.com 披露及美元折算](https://www.theblock.co/news/regulation/2022-01-19-crypto-com-ceo-confirms-400-accounts-were-compromised-in-recent-hack-130857)

<a id="source-applejeus"></a>
- **APPLEJEUS · 调查**：[Kaspersky：2018 年 AppleJeus 交易软件攻击](https://www.kaspersky.co.uk/blog/lazarus-crypto-exchange-attack/14314/)

<a id="source-trader2022"></a>
- **TRADER2022 · 联合通告**：[CISA/FBI：2022 年 TraderTraitor 联合通告](https://www.ic3.gov/CSA/2022/220418.pdf)

<a id="source-cb21notice"></a>
- **CB21NOTICE · 平台原始通知／监管存档**：[Coinbase 2021 客户通知（加州司法部长存档）](https://oag.ca.gov/system/files/09-24-2021%20Customer%20Notification.pdf)

<a id="source-mangomech"></a>
- **MANGOMECH · 链上研究**：[Chainalysis：Mango Markets 价格及抵押品操纵机制](https://www.chainalysis.com/blog/oracle-manipulation-attacks-rising/)

<a id="source-parity17"></a>
- **PARITY17 · 原始安全研究**：[OpenZeppelin：2017 年 Parity 多签钱包攻击分析](https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7)

<a id="source-bfdoj24"></a>
- **BFDOJ24 · 司法**：[美国司法部：Bitfinex 入侵者及洗钱案判刑说明](https://www.justice.gov/archives/opa/pr/bitfinex-hacker-sentenced-money-laundering-conspiracy-involving-billions-stolen)

<a id="source-bnresume26"></a>
- **BNRESUME26 · 平台**：[Binance：2026年11月1日分阶段恢复提现安排](https://www.binance.com/en/support/announcement/detail/73911fb819b240f88b88256bdd318eda)

<a id="source-fbi24social"></a>
- **FBI24SOCIAL · 执法威胁通告／防御参考**：[FBI：朝鲜针对加密行业人员的定向社会工程通告](https://www.ic3.gov/PSA/2024/PSA240903)

<a id="source-nistauth"></a>
- **NISTAUTH · 技术规范／防御参考**：[NIST SP 800-63B-4：认证器与抗钓鱼要求](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/)

<a id="source-nistsession"></a>
- **NISTSESSION · 技术规范／防御参考**：[NIST SP 800-63B-4：会话管理](https://pages.nist.gov/800-63-4/sp800-63b/session/)

<a id="source-certik24"></a>
- **CERTIK24 · 事件参与方声明**：[CertiK：Kraken 漏洞事件声明](https://www.certik.com/blog/certik-statement-on-kraken-vulnerability)

<a id="source-owasptx"></a>
- **OWASPTX · 技术指南／防御参考**：[OWASP：交易授权与执行前校验](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

<a id="source-owaspbiz"></a>
- **OWASPBIZ · 技术指南／防御参考**：[OWASP：业务逻辑、并发与外部操作重试](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)

<a id="source-bninitial26"></a>
- **BNINITIAL26 · 平台初步调查**：[Binance：DevOps终端与服务容器的初步调查通告](https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7)
