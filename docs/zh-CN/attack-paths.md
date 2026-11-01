# 交易所六类攻击路径解读

[仓库首页](../../README.zh-CN.md) · [English](../en/attack-paths.md) | **简体中文**

[调查正文](research.md) · **六类攻击路径** · [防御矩阵](defense-matrix.md) · [案例目录](case-catalogue.md) · [统计方法](methodology.md)

六类路径按攻击者如何取得资金控制权或造成资产损失划分。P1—P5涉及平台资金和客户账户，P6涉及客户受骗后主动转账或授权。同一事件可能经过多条路径，入口手法和攻击者归因另外记录。

## 分类规则与覆盖

分类覆盖签名、交易内容、账户授权、交易估值、入账结算和客户操作六个环节。同一事件在多条路径中出现时，事件总数只计一次。勒索、DDoS等风险另行评估。

| 风险场景 | 对应路径 | 覆盖说明 |
| --- | --- | --- |
| 私钥、备份、签名随机数缺陷 | P1 | 分别检查私钥被盗，以及签名实现缺陷导致私钥可被推算的情况 |
| 恶意前端、API输出、请求展示 | P2 | 区分用户业务确认和托管签名 |
| 盗号、恢复流程、MFA绕过、生产指令、钱包权限 | P3 | 包括客户账户恢复、后台写权限和钱包权限检查中的漏洞 |
| 被盗交易API、自有账户操纵价格或抵押估值 | P4 | 认证正确仍可能发生经济攻击 |
| 假充值、错误入账、重放、重组与双花 | P5 | 内部记账缺陷与外部结算变化分别验证 |
| 客户信任受骗、主动转账或授权 | P6 | 客户侧延伸；不等同平台钱包失守 |
| 合约权限及抵押协议（Parity、Mango） | P3 / P4 | 两案用于说明攻击机制，未计入CEX样本；其他协议另行分析 |
| 勒索、DDoS、没有资金影响的数据泄露 | 本模型之外 | 仍属网络风险，六条资金路径不能替代完整威胁模型 |

## P1 · 签名材料失守

**攻击过程**：存储泄露或实现缺陷 → 取得足够签名材料 → 形成有效签名 → 绕过原业务转出。

**失效环节**：密钥保密、备份隔离或签名实现失效，使攻击者可独立形成有效签名。

**检测证据**：密钥生成、读取、导出、备份与恢复记录；签名随机数及受影响实现版本；链上交易与业务请求、签名记录的对应关系；单凭链上无法确定广播者。

**验证场景**：按实际架构模拟主机、备份或一方签名材料泄露，检查攻击者还缺哪些条件才能签名。完整私钥已泄露时，验证资产迁移、旧密钥退役及后续入金处置；暂停本方签名服务后，攻击者仍可在外部使用泄露的私钥。

**案例说明**：BitMart 已确认私钥被盗，但最初的入侵方式尚未完整披露。Zilliqa 事件涉及旧版签名应用的随机数处理缺陷，攻击者可利用公开签名恢复特定账户的私钥。

| 案例 | 已知入口与失守位置 | 归因／限制 | 来源 |
| --- | --- | --- | --- |
| EX008 Coincheck 2018 | 平台调查推定：员工终端感染恶意程序，攻击者经终端进入内网并在NEM服务器侧窃取私钥；单一热钱包资产外流 | 未知；币量、估值及赔付口径有差异；不与后续赔付直接混算 | [Coincheck SEC 披露](https://www.coincheckgroup.com/sec-filings/all-sec-filings/content/0001213900-25-007203/0001213900-25-007203.pdf)、[SlowMist 事件索引，第 9 页](https://hacked.slowmist.io/?c=Exchange&page=9)、[Coincheck 2018 事件官方 FAQ](https://coincheck.com/info/faq_nem)、[Reuters：Coincheck 事发时美元估值](https://www.investing.com/news/stock-market-news/exclusive-coincheck-hackers-attempting-to-sell-stolen-cryptocurrency--executive-1171410) |
| EX042 BitMart 2021 | 平台确认私钥被盗；入口未完整公开；ETH与BSC两个热钱包受影响 | 未知；主统计采用后续平台回溯披露，另做1.96亿美元敏感性比较；未独立审计该回溯总额 | [BitMart 事件更新与原因说明](https://www.bitmart.com/en-US/support/articles/7922665245339/7923672421147/4411998987419)、[BitMart：2026 年方案公告中修订 2021 年事件金额](https://bitmart.zendesk.com/hc/en-us/articles/56571281537051-Announcement-on-BitMart-s-Initial-Indicative-Proposal-and-Roadmap) |
| EX092 KuCoin / Zilliqa Ledger应用 2026 | 旧版签名应用nonce处理缺陷；公开签名可暴露特定账户私钥 | 未知；链项目称KuCoin冷钱包异常触发上报；生态约6.83亿ZIL统计含后续流转，不直接视为CEX净损失 | [Zilliqa：旧版签名应用 nonce 缺陷复盘](https://www.zilliqa.com/ledger-incident/post-mortem/) |

## P2 · 交易意图与执行内容脱节

**攻击过程**：构造或展示被篡改 → 获批操作被替换 → 业务审批或签名通过 → 执行另一项资产操作。

**失效环节**：交易构造服务或展示页面返回的内容被直接用于批准，实际收款方、资产操作或权限变更未得到有效核对。

**检测证据**：CI及发布身份活动；运行中资源、API响应与发布物差异；批准意图、实际签名字节与执行后权限变化。

**验证场景**：替换实际业务响应，核验请求来源、业务批准、最终字节及执行时状态；测试构造方伪造批准记录，覆盖定向触发和权限变更，验证业务审批与链上签名各自的拒绝位置。

**案例说明**：Gate.io 的攻击发生在客户提现页面。DMM 的联合调查认为，攻击者很可能操纵了合法交易请求；具体操作过程尚未完整披露。

| 案例 | 已知入口与失守位置 | 归因／限制 | 来源 |
| --- | --- | --- | --- |
| EX016 Gate.io / StatCounter 2018 | 统计服务JavaScript供应链被污染；提现页面中的交易信息被定向篡改 | 未知；按提现页面路径、金额或可用余额触发篡改；ESET 确认提现页面请求被篡改，未取得可靠被盗总额 | [ESET：StatCounter 定向攻击 Gate.io](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/) |
| EX070 DMM Bitcoin 2024 | 假招聘测试侵入Ginco员工终端并取得会话；供应商通信访问被判断很可能用于操纵合法交易请求 | TraderTraitor；FBI/DC3/NPA归因；操纵具体交易请求保留调查中的likely措辞；监管缺陷不等于已证明被利用 | [FBI/DC3/NPA：DMM Bitcoin 攻击链与归因](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom)、[关东财务局对 DMM Bitcoin 的检查](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html) |
| EX081 Bybit 2025 | Safe开发者终端及AWS会话被侵入；前端污染待签名交易，影响冷钱包资产控制 | TraderTraitor；FBI归因；恶意交易取得了有效签名；攻击者篡改了交易内容 | [Sygnia：Bybit 调查分析](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/)、[FBI：Bybit 归因](https://www.ic3.gov/PSA/2025/PSA250226) |
| EX089 SwissBorg / Kiln 2025 | Kiln工程师GitHub令牌失窃，经CI取得基础设施凭据；交易构造API返回恶意交易，客户签名后提款权限改变 | 未知；Kiln复盘区分8月31日签署恶意交易和9月8日发现；不能把两日混为同一时间点 | [Kiln 2025 年 10 月 7 日复盘](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information)、[SwissBorg：Kiln 事件调查更新](https://swissborg.com/blog/swissborg-security-update-kiln-breach) |

## P3 · 账户及提现授权失守

**攻击过程**：账户恢复或后台失守 → 冒用或改写授权身份 → 提现权限被接受 → 平台执行资金支出。

**失效环节**：账户恢复、后台授权或钱包权限检查存在漏洞，攻击者因此取得本不属于自己的资金操作权限。

**检测证据**：登录、恢复、MFA变更及会话使用记录；生产与数据库写入、服务身份和提现指令；钱包所有者、模块、阈值及其他执行权限变更。

**验证场景**：分别测试客户账户恢复、生产身份伪造指令、钱包权限检查；检查正常流程与恢复流程能否绕过同一门槛。

**案例说明**：Coinbase 2021 年事件利用短信账户恢复缺陷取得验证令牌。WOO X 的攻击者利用生产环境写权限改写客户身份信息。Parity 则通过合约初始化缺陷修改钱包所有者和签名阈值，仅用来说明钱包权限风险。

| 案例 | 已知入口与失守位置 | 归因／限制 | 来源 |
| --- | --- | --- | --- |
| EX098 Coinbase SMS账户恢复 2021 | 攻击者已掌握客户邮箱、密码、电话号码及邮箱访问；最初取得方式：未知；SMS账户恢复缺陷使攻击者取得验证令牌，进入客户账户并转出资金 | 未知；不等于攻破所有MFA机制；通知未给出发现、修复或恢复的准确时刻 | [Coinbase 2021 客户通知（加州司法部长存档）](https://oag.ca.gov/system/files/09-24-2021%20Customer%20Notification.pdf) |
| EX085 BigONE 2025 | 第三方攻击及生产环境受影响；账户与风控相关逻辑遭操纵；平台称私钥安全 | 未知；公开说明仍非完整独立取证报告 | [BigONE 2025 年 7 月 16 日通告](https://bigone.zendesk.com/hc/en-us/articles/48906456010393-Announcement-Regarding-BigONE-Security-Incident-on-16-July-2025)、[BigONE Eurasia 对全球平台事件的说明](https://bigoneeurasia.ladesk.com/275817-Temporary-Platform-Maintenance)、[SlowMist 事件索引，第 1 页](https://hacked.slowmist.io/?c=Exchange)、[The Block：BigONE 事件及金额](https://www.theblock.co/news/regulation/2025-07-16-bigone-hack-362814) |
| EX087 WOO X 2025 | 外部协作项目恶意程序侵入开发者终端；开发环境、Kubernetes权限及数据库访问扩展至账户与提现 | 平台判断涉及UNC4899/UNC5565等朝鲜活动；措辞存在差异；归因来自平台复盘，涉及多个活动标签 | [WOO X 7 月 24 日事件复盘](https://woox.io/blog/july-24th-security-incident-post-mortem) |
| EX093 Bitget 2026 | 第三方安全产品漏洞取得高权限内部凭据；伪造提现命令经钱包系统执行 | Chainalysis归因朝鲜；注明机构判断；平台排除私钥泄露；金额上调来自补充核算，不是持续失窃 | [Bitget 事件调查说明，更新至 2026 年 10 月 20 日](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)、[Bitget 2026 年 9 月 25 日金额修订](https://www.bitget.com/support/articles/12560603896108)、[Chainalysis：Bitget 调查](https://www.chainalysis.com/blog/387m-bitget-theft-2026/) |

## P4 · 交易与估值被操纵

**攻击过程**：盗用交易权或自有账户 → 异常成交或价格操纵 → 价值转移或抵押膨胀 → 提现或借出真实资产。

**失效环节**：交易权限或价格输入被用于转移价值、夸大可借资产；账户和签名均有效也可能产生损失。

**检测证据**：API凭据创建、请求来源与使用偏差；盘口深度、成交集中度、关联账户和估值来源；持仓、未实现收益、可借额度及真实清算能力。

**验证场景**：分别测试盗用API的不利成交与自有账户操纵薄市场；追踪现货、抵押、借贷和提现之间的价值转换。

**案例说明**：VIA 事件中，平台拦住了外部提款，但部分受害成交已无法撤回。Mango 用于说明抵押估值操纵，未计入中心化交易所样本。判断是否存在操纵，还需结合订单、账户关系和资金去向。

| 案例 | 已知入口与失守位置 | 归因／限制 | 来源 |
| --- | --- | --- | --- |
| EX010 Binance VIA 2018 | 长期钓鱼取得用户凭据并创建API凭据；交易权限被用于跨账户转移价值；后续提现被拦截 | 未知；31个预先入金账户卖出VIA；部分受害买单与无辜对手方成交。不能把阻止外部提款等同于客户零损失 | [Binance VIA 钓鱼与盗币未遂复盘](https://www.binance.com/en/support/announcement/detail/360001547431) |
| EX050 3Commas / 多家交易所账户 2022 | 供应商数据库API数据泄露；交易账户被未授权交易 | 未知；不是交易所主钱包私钥；暴露条数不等于受害人数 | [3Commas API 数据泄露通告](https://3commas.io/blog/notice-on-api-data-disclosure-incident)、[3Commas API 泄露 FAQ](https://3commas.io/blog/api-security-incident-faq) |

## P5 · 账面权益与实际结算脱节

**攻击过程**：入账缺陷或双花 → 生成可用余额 → 兑换或提现 → 形成资产缺口。

**失效环节**：可用余额缺少最终可支配的外部资产支撑；重组可能发生在兑出之后。

**检测证据**：链上原始事件、确认和重组状态；入账规则、幂等键及余额变更；交易、抵押、借贷和多链提款的后续使用。

**验证场景**：重放未完成充值、重组和重复事件，追踪余额是否仍可跨业务使用；检验风险限制何时实际生效。

**案例说明**：Kraken 事件由研究人员测试触发，双方对授权范围存在争议，本文将其与犯罪盗币事件分开记录。虚增余额能否用于借款，是在入账漏洞基础上提出的扩展测试场景。

| 案例 | 已知入口与失守位置 | 归因／限制 | 来源 |
| --- | --- | --- | --- |
| EX017 Gate.io / ETC 2019 | ETC链重组与双花；已入账充值被链上重组撤销 | 未知；返还额不等于攻击总额；非交易所服务器入侵 | [Gate：ETC 双花资金部分返还](https://www.gate.com/ru/announcements/article/16740) |
| EX032 OKEx / ETC 2020 | ETC多数算力攻击与重组；交易所确认并兑出的充值随后失效 | 未知；充值被链重组撤销，交易所此前已兑出资产；公开材料指向双花 | [ETC Cooperative 2020 年 8 月董事会资料](https://etccooperative.org/ETC-Coop-Board-Package-August-2020.pdf) |
| EX072 Kraken 入账漏洞 2024 | 入账实现缺陷；未完成真实充值即可形成余额 | CertiK Skyfall 团队；漏洞利用范围存在争议；不归为Lazarus或普通刑事盗币；技术机制与争议分开 | [Kraken：入账漏洞披露](https://blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug)、[CertiK：Kraken 漏洞事件声明](https://www.certik.com/blog/certik-statement-on-kraken-vulnerability) |

## P6 · 客户受骗后主动授权

**攻击过程**：滥用品牌或客户信息 → 伪造可信身份 → 客户相信虚假目的 → 主动转账或授权。

**失效环节**：客户相信了虚假的收款方身份或操作理由，主动完成转账或授权。泄露的客户资料可能被用来增强欺骗性。

**检测证据**：支持人员查询与导出行为；身份恢复记录和客户报告；泄露客户群体与异常资产操作的关联。

**验证场景**：在授权演练中核验支持数据访问和导出限制，测试已知泄露客户的异常恢复、会话与资金操作联动。

**范围说明**：P3 由攻击者接管账户后直接操作；P6 由受骗客户本人转账或授权。资损记录需注明资产所在位置及实际操作人。

| 案例 | 已知入口与失守位置 | 归因／限制 | 来源 |
| --- | --- | --- | --- |
| EX083 Coinbase 支持人员事件 2025 | 部分外包支持人员被收买；客户信息泄露并被用于社会工程欺诈 | 未知；数据访问权限不等于直接提现权限，但能影响后续欺诈 | [Coinbase：支持人员被收买与数据泄露](https://www.coinbase.com/en-nl/blog/protecting-our-customers-standing-up-to-extortionists)、[Coinbase 2025 年 5 月 15 日 8-K](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm) |

## 外部机制对照

- **M01 Mango Markets 2022 → P4**：攻击者控制自己的账户，操纵薄流动性价格，将未实现收益作为抵押借走资产；不以盗取API为前提。外部DEX机制对照，不进入交易所案例数及金额样本。[Chainalysis：Mango Markets 价格及抵押品操纵机制](https://www.chainalysis.com/blog/oracle-manipulation-attacks-rising/)
- **M02 Parity 2017 → P3**：初始化权限缺陷允许改写所有者和阈值，再支配资产；不以窃取原有密钥为前提。外部钱包合约机制对照，不进入交易所案例数及金额样本。[OpenZeppelin：2017 年 Parity 多签钱包攻击分析](https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7)
