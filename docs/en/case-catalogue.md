# Exchange Security Case Catalogue: 2016–2026

[Repository home](../../README.md) · **English** | [简体中文](../zh-CN/case-catalogue.md)

[Research](research.md) · [Attack paths](attack-paths.md) · [Defense matrix](defense-matrix.md) · **Case catalogue** · [Methodology](methodology.md)

This catalogue records 98 public incidents and leads through November 1, 2026: 90 exchange or customer incidents and 8 related-service incidents. It retains losses, data exposure, interrupted attacks, and disputed research activity. It is not a census of all incidents.

## Reading the records

- **P**: platform, supplier, regulatory, judicial, or other original disclosure; **I**: investigative research; **M**: media or secondary reporting; **C**: index-only lead. Combined codes identify the kinds of sources collected, not a numerical confidence score. Thirty-eight entries remain index-only.
- Amounts retain incident-time estimates or original coin quantities. Freezing, recovery, reimbursement, and response cost are different measures. An unknown root cause is not recorded as private-key exposure without supporting evidence.
- Actor claims, platform assessments, researcher attribution, and law-enforcement findings remain distinct. Five records are marked as disputed because the nature of the incident or responsibility for it remains contested. Dates retain disclosed precision.
- The [loss sample](../../data/loss-sample.csv) selects 41 incidents under the [methodology](methodology.md). Case IDs connect this catalogue with the [machine-readable registry](../../data/case-registry.csv).

Source-type distribution: P: 21; I+M: 2; M: 15; P+M: 3; C: 38; I: 9; P+C: 3; P+I: 6; P+I+M: 1. These counts describe the evidence collected for this registry, not industry-wide incident rates.

## Annual records

### 2016

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX001<br>2016-03—04 | **ShapeShift**<br>Exchange / customer | Approximately $230,000; three thefts treated as one incident group | Insider assistance and endpoint malware → credentials and the rebuilt environment remained exposed | Internal and external collaborators; not all individuals identified publicly | **P**: Further compromise occurred after rebuilding.<br>[SHAPE](#source-shape) |
| EX002<br>2016-05 | **Gatecoin**<br>Exchange / customer | 250 BTC and 185,000 ETH; approximately $2 million at the time | Server intrusion; exact entry unknown → hot-wallet assets transferred | Unknown | **I+M**: The 2019 liquidation is not directly attributed to this attack.<br>[GATECOIN](#source-gatecoin) · [SM9](#source-sm9) · [CERT2019](#source-cert2019) |
| EX003<br>2016-08-02 | **Bitfinex**<br>Exchange / customer | Approximately 119,755 BTC; approximately $72 million at the time | Platform intrusion; full initial access sequence undisclosed → unauthorized BTC transfers | Ilya Lichtenstein; confirmed in court proceedings | **P**: Heather Morgan participated in laundering; she is not recorded as a confirmed intruder. Later recovery valuations do not replace incident-time loss.<br>[BFDOJ](#source-bfdoj) · [BFFAQ](#source-bffaq) |
| EX004<br>2016-10-13 | **Bitcurex**<br>Exchange / customer | Media estimate: approximately $1.5 million | Initial access undisclosed → platform asset outflows | Unknown | **M**: Public materials do not explain the technical cause.<br>[BITCUREX](#source-bitcurex) |

### 2017

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX005<br>2017-04 | **Yapizon**<br>Exchange / customer | 3,831 BTC; approximately $5 million when disclosed | Initial access undisclosed → hot-wallet compromise | Unknown | **M**: Separate from the later Youbit incident after the exchange was renamed.<br>[YOUBIT](#source-youbit) · [SM9](#source-sm9) · [CERT2019](#source-cert2019) |
| EX006<br>2017-06–07 (disclosed) | **Bithumb**<br>Exchange / customer | Information on approximately 31,800 users; aggregate customer loss not established | Employee computer compromised → customer information used for subsequent account fraud | Unknown | **M**: A customer-data incident, not evidence that the platform's custody wallet was drained.<br>[BITHUMB17](#source-bithumb17) |
| EX007<br>2017-12-19 | **Youbit**<br>Exchange / customer | Platform reported approximately 17% of its assets; dollar amount unknown | Initial access undisclosed → another asset outflow | Unknown | **M**: Formerly Yapizon; this second incident is separate from April 2017.<br>[YOUBIT](#source-youbit) |

### 2018

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX008<br>2018-01-26 | **Coincheck**<br>Exchange / customer | 526,300,010 XEM; selected incident-time estimate approximately $530 million | Platform investigation inferred malware infection of an employee endpoint → internal-network access → NEM-server private-key theft → outflow from a single hot wallet | Unknown | **P+M**: Coin quantity, valuation, subsequent yen disclosures, and reimbursement differ; they are not combined.<br>[COINCHECK](#source-coincheck) · [SM9](#source-sm9) · [CCFAQ](#source-ccfaq) · [CCUSD](#source-ccusd) |
| EX009<br>2018-02 (disclosed) | **BitGrail**<br>Exchange / customer | Approximately 17 million NANO; approximately $170 million at the time | How the shortfall arose and who was responsible remain disputed → court records require further analysis to distinguish withdrawal-logic failures from management issues | Unknown | **M**: Incident classification or responsibility disputed; not coded as a technically established external APT attack.<br>[BITGRAIL](#source-bitgrail) |
| EX010<br>2018-03-07 | **Binance VIA**<br>Exchange / customer | External withdrawals blocked; some unauthorized victim trades irreversible; no loss total specific to this incident disclosed | Sustained credential phishing and creation of API keys → trading permissions used to transfer value between accounts → withdrawals blocked | Unknown | **P**: Thirty-one prefunded accounts sold VIA. Some victim buys matched uninvolved counterparties; blocked payouts do not establish zero customer loss.<br>[VIA](#source-via) |
| EX011<br>2018-04 | **Coinsecure**<br>Exchange / customer | 438 BTC; approximately $3.5 million | Entry and insider responsibility unresolved → possible exposure during wallet-key handling | Insider involvement alleged, not established | **C**: Index-only evidence; claims about recovery operations and insider involvement require verification against primary sources.<br>[SM9](#source-sm9) |
| EX013<br>2018-06 | **Bithumb**<br>Exchange / customer | Initial estimate approximately $30–31.5 million | Initial access undisclosed → hot-wallet outflows | Unknown | **C**: Later amount revisions were reported; net loss is not calculated from the initial estimate.<br>[SM9](#source-sm9) |
| EX012<br>2018-06-10 | **Coinrail**<br>Exchange / customer | Yonhap estimate approximately $37.2 million; other contemporary estimates approximately $40 million | Platform disclosed network intrusion without full detail → outflows of assets held in custody | Unknown | **M**: Uses contemporary valuation, not current token prices.<br>[SM9](#source-sm9) · [COINRAILUSD](#source-coinrailusd) |
| EX014<br>2018-09-14 | **Zaif**<br>Exchange / customer | Approximately $60 million at the time | Initial access undisclosed → BTC, BCH, MONA and other hot-wallet outflows | Unknown | **M**: Multiple assets belong to one incident.<br>[SM9](#source-sm9) · [ZAIFUSD](#source-zaifusd) |
| EX015<br>2018-10-20 | **Trade.io**<br>Exchange / customer | 50 million TIO; approximately $7.5 million | Initial access undisclosed → tokens transferred from what the platform called cold storage | Unknown | **C**: The platform's cold-storage description does not establish that hardware security was broken.<br>[SM9](#source-sm9) |
| EX016<br>2018-11-03—06 | **Gate.io / StatCounter**<br>Exchange / customer | Reliable aggregate loss unavailable | Compromised StatCounter JavaScript → targeted alteration of withdrawal-page transaction information | Unknown | **I**: Triggered by withdrawal page, amount, or available balance. ESET confirmed withdrawal-page request tampering but did not establish total theft.<br>[ESET](#source-eset) |

### 2019

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX017<br>2019-01 | **Gate.io / ETC**<br>Exchange / customer | Platform reported approximately $100,000 returned; total loss from the attack not established | ETC reorganization and double spending → previously credited deposits removed from chain history | Unknown | **P**: Returned amount is not total theft; this was not an exchange-server intrusion.<br>[GATEETC](#source-gateetc) |
| EX018<br>2019-01 | **Cryptopia**<br>Exchange / customer | Approximately $16–17.5 million | Full initial access sequence undisclosed → continuing outflows across addresses | Unknown | **P+C**: Later January outflows remain in one incident group; the separate theft during liquidation is not included in this incident group.<br>[CRYPTOPIA](#source-cryptopia) · [SM8](#source-sm8) |
| EX019<br>2019-01-26 | **LocalBitcoins**<br>Exchange / customer | Approximately 7.9 BTC; approximately $27,000 | Third-party software-related vulnerability → unauthorized activity in a small number of customer accounts | Unknown | **C**: Not the entire custody-wallet balance.<br>[SM8](#source-sm8) |
| EX020<br>2019-02-15 (disclosed) | **Coinmama**<br>Exchange / customer | Approximately 450,000 email-address and password-hash records; financial loss unknown | Data-system intrusion, initial details undisclosed → customer authentication data exposed | Unknown | **M**: Does not mean 450,000 wallets were stolen.<br>[COINMAMA](#source-coinmama) |
| EX021<br>2019-03-24 | **DragonEx**<br>Exchange / customer | Approximately $6–7 million | Complete initial entry unverified in this registry → outflows from wallets holding several assets | Unknown | **C**: Fake trading-software explanations are not coded here as confirmed root cause.<br>[SM8](#source-sm8) |
| EX022<br>2019-03-29 | **Bithumb**<br>Exchange / customer | Approximately 3.13 million EOS and 20.17 million XRP; approximately $19–20 million | Initial access undisclosed → multiple asset outflows | Platform suspected insiders; unconfirmed | **C**: EOS and XRP records are combined as one incident.<br>[SM8](#source-sm8) |
| EX023<br>2019-05-02 | **BitoPro / XRP**<br>Exchange / customer | Index estimate approximately 7 million XRP, not $7 million | Deposit-processing anomaly; original technical report not verified → abnormal balances and transaction rollback | Unknown | **P+C**: Platform notice confirms rollback; amount and exact parsing defect have weaker evidence.<br>[BITOPRO19](#source-bitopro19) · [SM8](#source-sm8) |
| EX024<br>2019-05-07 | **Binance**<br>Exchange / customer | 7,000 BTC; approximately $40 million | Phishing and malware acquired API credentials and 2FA information → coordinated account activity passed checks and completed withdrawal | Unknown | **P**: The official notice did not identify wallet private-key exposure as the root cause.<br>[BINANCE19](#source-binance19) |
| EX096<br>2019-06-17 | **Coinbase Firefox double zero-day attack**<br>Exchange / customer | Platform reported blocking the attack without customer-fund loss | Targeted social-engineering link and two Firefox zero-days → code execution in the browser extended to the host; subsequent attacker activity was detected and stopped | Coinbase tracking labels CRYPTO-3 / HYDSEVEN; national affiliation unconfirmed in original report | **P**: Successful interruption retained; the existence of an entry route does not establish theft success.<br>[COINBASE19](#source-coinbase19) |
| EX025<br>2019-06-27 | **Bitrue**<br>Exchange / customer | 9.3 million XRP and 2.5 million ADA; approximately $4.2–4.5 million | Platform-described secondary-review flaw → account-related authority extended to hot-wallet funds | Unknown | **C**: 9.3 million refers to XRP quantity, not dollars.<br>[SM7](#source-sm7) |
| EX026<br>2019-07-12 | **BITPoint**<br>Exchange / customer | Initially JPY 3.5 billion; later approximately JPY 3.02 billion | Initial access undisclosed → multiple hot wallets compromised | Unknown | **C**: Initial and revised amounts are kept separate.<br>[SM7](#source-sm7) |
| EX027<br>2019-11-08 | **VinDAX**<br>Exchange / customer | At least approximately $500,000 | Initial access undisclosed → hot-wallet outflows | Unknown | **C**: No sufficiently detailed platform technical postmortem collected.<br>[SM7](#source-sm7) |
| EX028<br>2019-11-27 | **Upbit**<br>Exchange / customer | 342,000 ETH; approximately $49 million | Initial entry undisclosed → abnormal ETH wallet transfer | Index cites later government attribution to North Korea; original attribution document not collected | **M**: Timing during hot/cold transfers does not establish insider involvement.<br>[SM7](#source-sm7) · [UPBIT19USD](#source-upbit19usd) |

### 2020

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX029<br>2020-02-05—06 | **Altsbit**<br>Exchange / customer | Approximately $70,000 in BTC and ETH; other tokens listed separately | Initial access undisclosed → platform wallet compromise | Unknown | **C**: Not a verified all-asset net loss.<br>[SM7](#source-sm7) |
| EX030<br>2020-07-11 | **Cashaa**<br>Related service | 336 BTC; approximately $3.1 million | Platform reported malware on an endpoint used for wallet operations → wallet funds transferred | Unknown | **C**: Crypto-financial service provider; categorized separately from ordinary centralized exchanges.<br>[SM6](#source-sm6) |
| EX031<br>2020-07-31 | **2gether**<br>Exchange / customer | Initially approximately EUR 1.2 million; later dollar reports conflict | Malware explanation needs original-investigation confirmation → platform assets transferred | Later arrest reports have not been checked against judicial records in this registry | **C**: Index figure of $7 million is not treated as an undisputed loss.<br>[CS](#source-cs) · [SM6](#source-sm6) |
| EX032<br>2020-07-31—08 | **OKEx / ETC**<br>Exchange / customer | Approximately $5.6 million in double-spend losses | ETC majority-hashpower attack and reorganization → deposits accepted and exchanged by the platform later invalidated | Unknown | **P**: A chain reorganization invalidated deposits after the exchange had paid out; public materials describe a double spend.<br>[ETC20](#source-etc20) |
| EX033<br>2020-09-08 | **Eterbase**<br>Exchange / customer | Approximately $5.4 million | Initial access undisclosed → multiple asset hot-wallet outflows | Unknown | **C**: Technical entry not confirmed.<br>[SM6](#source-sm6) |
| EX034<br>2020-09-26 | **KuCoin**<br>Exchange / customer | Later platform estimate approximately $285 million; initial estimates lower | Hot-wallet keys affected; acquisition method undisclosed → multichain wallet outflows | Unknown | **P**: Frozen, recovered, and insurance-covered amounts are different measures.<br>[KUCOIN20](#source-kucoin20) |
| EX035<br>2020-11-13 | **Liquid**<br>Exchange / customer | Customer information affected; theft total for this incident unconfirmed | Domain-service and related account compromise → domain/email trust affected internal access and customer information | Unknown | **C**: Separate from the 2021 theft; a shared cause is not assumed.<br>[SM6](#source-sm6) |
| EX036<br>2020-12-21 | **EXMO**<br>Exchange / customer | Platform reported approximately 5% of assets affected; media estimate approximately $10.5 million | Initial access undisclosed → some hot-wallet outflows | Unknown | **P+C**: The 5% figure comes from the platform; net loss is unknown.<br>[EXMO](#source-exmo) · [SM6](#source-sm6) |
| EX037<br>2020-12-24 | **Livecoin**<br>Exchange / customer | Reliable total unavailable | Platform reported loss of server control → abnormal prices and trading-system behavior | Unknown | **C**: Incident classification or responsibility disputed; circulating amounts and the platform explanation are not treated as completed forensic findings.<br>[SM6](#source-sm6) |
| EX038<br>2020-12-26 | **Altilly**<br>Exchange / customer | Index lists 30 BTC and 12,000 USDT | Unauthorized access; full attack sequence unverified → custody systems and assets affected | Unknown | **C**: Public details are limited; retained for further investigation.<br>[SM6](#source-sm6) |

### 2021

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX098<br>2021-03–05-20; 2021-09-24 (notice) | **Coinbase SMS account recovery**<br>Exchange / customer | At least 6,000 customers experienced unauthorized transfers; no loss total specific to this incident disclosed | Attacker already held credentials, phone numbers, and email access, initial acquisition unknown → SMS-recovery flaw yielded authentication tokens → account access and transfers | Unknown | **P**: Not a breach of every MFA mechanism. Notice gives no exact detection, repair, or restoration time.<br>[CB21NOTICE](#source-cb21notice) |
| EX039<br>2021-04-29 | **Hotbit**<br>Exchange / customer | Platform reported preventing theft; data and services were damaged | Infrastructure intrusion → destruction of business data; attackers reportedly failed to gain access to funds | Unknown | **C**: The reported prevention of theft is recorded separately from disruption to services.<br>[SM5](#source-sm5) |
| EX040<br>2021-08-19 | **Liquid**<br>Exchange / customer | Later Elliptic estimate approximately $97 million; initial reports approximately $80 million | Initial access sequence not established in the selected material → multiple warm-wallet outflows | Unknown | **I+M**: Later estimates are distinguished from initial disclosure.<br>[LIQUID21](#source-liquid21) · [LIQUIDELL](#source-liquidell) |
| EX041<br>2021-08-28—29 | **Bilaxy**<br>Exchange / customer | Approximately $21.7 million estimated | Initial access undisclosed → hot-wallet token outflows | Unknown | **C**: Asset liquidity affects realizable value.<br>[SM5](#source-sm5) |
| EX042<br>2021-12-04 | **BitMart**<br>Exchange / customer | Platform's 2026 retrospective: $319.5 million valued on December 4, 2021; initial $150 million and contemporary research approximately $196 million | Platform confirmed private-key theft; full initial access sequence undisclosed → ETH and BSC hot wallets affected | Unknown | **P**: Main sample uses the later platform estimate, with a $196 million sensitivity scenario; retrospective total not independently audited.<br>[BITMART](#source-bitmart) · [BITMART26](#source-bitmart26) |
| EX043<br>2021-12-11 | **AscendEX**<br>Exchange / customer | Approximately $77.7 million estimated | Initial access undisclosed → hot-wallet outflows on several networks | Unknown | **P+M**: Platform disclosed rebuilding hot wallets and changing deposit addresses.<br>[ASCEND](#source-ascend) · [SM5](#source-sm5) · [ASCENDUSD](#source-ascendusd) |

### 2022

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX044<br>2022-01-08 | **LCX**<br>Exchange / customer | Later platform estimate approximately $7.94 million | Initial access not publicly confirmed → one hot wallet and its tokens affected | Unknown | **P**: January 9 was the report date; frozen amounts are not automatically recovered amounts.<br>[LCX](#source-lcx) · [LCXCOURT](#source-lcxcourt) |
| EX045<br>2022-01-17 | **Crypto.com**<br>Exchange / customer | Approximately $33.8–34 million; 483 accounts | 2FA controls bypassed; complete technical cause undisclosed → withdrawals lacking normal customer authorization | Unknown | **M**: Uses public quotation of the original notice rather than an unrelated monthly business review; dollar amount is approximate.<br>[CRYPTODGA](#source-cryptodga) · [CRYPTOUSD](#source-cryptousd) |
| EX046<br>2022-02-01 | **Bitbns**<br>Exchange / customer | On-chain estimate approximately $7.5 million | Initial access undisclosed → hot-wallet outflows; delayed disclosure | Unknown | **C**: Amount and the contemporaneous maintenance explanation remain disputed and need primary-source verification.<br>[SM5](#source-sm5) |
| EX047<br>2022-08-01—02 | **ZB.com**<br>Exchange / customer | Suspected approximately $4.3–4.8 million | Initial access undisclosed → abnormal on-chain outflows | Unknown | **C**: Incident classification or responsibility disputed; suspected outflow does not establish external intrusion.<br>[SM5](#source-sm5) |
| EX048<br>2022-11-01—02 | **Deribit**<br>Exchange / customer | $28 million | Initial access undisclosed → BTC, ETH and USDC hot-wallet outflows | Unknown | **M**: Platform stated company reserves would cover the loss; entry remains unknown.<br>[DERIBIT](#source-deribit) |
| EX049<br>2022-11-11 | **FTX**<br>Exchange / customer | Public estimate approximately $477 million; early $600 million figure mixes categories | Complete route and correspondence with later criminal cases require further verification → unauthorized transfers during bankruptcy | Unknown | **I**: Kept distinct from misappropriation, bankruptcy shortfalls, and transfers made to safeguard assets under regulatory direction.<br>[CASA](#source-casa) · [SM4](#source-sm4) · [SINBAD](#source-sinbad) |
| EX050<br>2022-12-28 (disclosed) | **3Commas / exchange accounts**<br>Exchange / customer | At least 100,000 API records exposed; aggregate related loss not reliably established | API credentials exposed from a supplier database → unauthorized trading on exchange accounts | Unknown | **P**: These were trading credentials, not exchange master-wallet keys; record count does not equal victim count.<br>[THREEC](#source-threec) · [THREEFAQ](#source-threefaq) |

### 2023

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX097<br>2023-02-05 | **Coinbase employee social engineering**<br>Exchange / customer | Limited corporate-directory information exposed; platform reported no customer-fund or customer-data impact | SMS phishing obtained employee credentials, followed by telephone social engineering → employee trust abused; critical-system access blocked | Platform discussed similarities to existing social-engineering activity; not an attribution established in court | **P**: Does not establish a common operator with the 2025 support-personnel incident.<br>[COINBASE23](#source-coinbase23) |
| EX051<br>2023-04-09 | **GDAC**<br>Exchange / customer | Approximately $13 million; platform reported approximately 23% of assets held in custody | Initial access undisclosed → hot-wallet outflows | Unknown | **M**: Percentage is the platform's incident-time disclosure.<br>[GDAC](#source-gdac) |
| EX052<br>2023-04-14 | **Bitrue**<br>Exchange / customer | Approximately $23 million | Initial access undisclosed → hot-wallet outflows | Unknown | **P**: Separate from the 2019 incident.<br>[SM4](#source-sm4) · [BITRUE23](#source-bitrue23) |
| EX053<br>2023-04-24 | **KuCoin social account**<br>Exchange / customer | 22,628 USDT equivalent, confirmed by platform | Official social account compromised → fake campaign caused customer losses | Unknown | **C**: Not theft from KuCoin custody wallets.<br>[SM4](#source-sm4) |
| EX054<br>2023-05 (disclosed) | **Patricia**<br>Exchange / customer | Incident index reports approximately $2 million; the date of the attack requires clarification | Retail exchange application affected → BTC and fiat-related assets lost | Unknown | **C**: Amount, actual occurrence, and later tokenization treatment need further verification.<br>[SM4](#source-sm4) |
| EX055<br>2023-06-11 | **Floating Point Group**<br>Related service | Approximately $15–20 million | Initial access undisclosed → assets lost from institutional trading/custody service | Unknown | **C**: Institutional brokerage and asset-management infrastructure; categorized separately.<br>[SM4](#source-sm4) |
| EX056<br>2023-07-23 | **CoinList social account**<br>Exchange / customer | Reliable loss total unavailable | Social account compromised → fraudulent token-sale links | Unknown | **C**: Unknown loss is not recorded as zero.<br>[SM4](#source-sm4) |
| EX057<br>2023-09-07 | **Fortress Trust**<br>Related service | Approximately $12–15 million | Third-party cloud-tool supplier affected → customer assets held in custody transferred | Unknown | **C**: Custody-infrastructure dependency, not an ordinary centralized exchange.<br>[SM4](#source-sm4) |
| EX058<br>2023-09-12 | **CoinEx**<br>Exchange / customer | Later estimate approximately $70 million | Preliminary assessment of affected hot-wallet keys → multichain outflows | Researchers pointed to North Korea; original attribution report not collected in this registry | **I**: Initial amounts were much lower; key-acquisition route undisclosed.<br>[SM4](#source-sm4) · [SINBAD](#source-sinbad) |
| EX059<br>2023-09-14 | **Remitano**<br>Exchange / customer | Suspected $2.7 million; approximately $1.4 million frozen | Initial access undisclosed → abnormal large transfer | Unknown | **C**: Incident classification or responsibility disputed; suspected theft, freezing, and return are separate states.<br>[SM4](#source-sm4) |
| EX060<br>2023-09-24 | **HTX**<br>Exchange / customer | Approximately 5,000 ETH; approximately $8–8.2 million | Initial access undisclosed → hot-wallet outflow | Unknown | **C**: Separate from the November HTX/HECO incident.<br>[SM4](#source-sm4) |
| EX061<br>2023-09-24 | **Upbit / fake APT deposits**<br>Exchange / customer | Total loss unconfirmed | Deposit-processing asset-identification error; technical details not verified against a primary source → unintended tokens credited as APT and traded | Unknown | **C**: Third-party parsing explanations are not treated as platform-confirmed causes.<br>[SM3](#source-sm3) |
| EX062<br>2023-10-17 | **Coins.ph**<br>Exchange / customer | Approximately 12.2 million XRP; approximately $6 million | Initial access not publicly confirmed → abnormal XRP transfer | Unknown | **M**: Incident classification or responsibility disputed; reported suspected attack, not $12.2 million.<br>[COINSPH](#source-coinsph) |
| EX063<br>2023-11-08 | **CoinSpot**<br>Exchange / customer | Approximately 1,283 ETH; approximately $2.47 million | Initial access not publicly confirmed → outflows from two hot wallets | Unknown | **C**: An on-chain signature does not alone establish key exposure.<br>[SM3](#source-sm3) |
| EX064<br>2023-11-10 | **Poloniex**<br>Exchange / customer | CertiK estimate approximately $132 million; other research approximately $130 million | CertiK analyzed key compromise; initial intrusion and how the keys were exposed not fully disclosed → multiple asset outflows | Some research suggests a North Korea link; not treated as definite attribution here | **I**: Differences in valuation and asset coverage remain unresolved.<br>[SM3](#source-sm3) · [CASA](#source-casa) · [POLOCERT](#source-polocert) |
| EX065<br>2023-11-22 | **HTX / HECO related incident**<br>Exchange / customer | Combined estimate approximately $113 million, including bridge and exchange | Initial access not publicly confirmed → concurrent HTX-wallet and HECO-bridge outflows | Unknown | **C**: One linked incident group; cannot enter the CEX loss sample without separating components.<br>[SM3](#source-sm3) |
| EX066<br>2023-12-20 (disclosed) | **INX related vendor**<br>Related service | Approximately $1.6 million | Third-party supplier server compromised → unauthorized trades caused a subsidiary loss | Unknown | **C**: Trading-system dependency; amount does not mean master-wallet theft.<br>[SM3](#source-sm3) |

### 2024

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX067<br>2024-02-18 (disclosed) | **FixedFloat**<br>Related service | Approximately $26.1 million | Full initial access sequence not established in selected material → instant-swap service assets stolen | Unknown | **C**: The service's non-custodial claims and an index's DEX label do not establish how its architecture actually handles funds.<br>[SM3](#source-sm3) |
| EX068<br>2024-03-31—04-01 | **FixedFloat**<br>Related service | Approximately $2.8–3 million | Platform reported a third-party hosting issue → another asset outflow | Unknown | **C**: Separate from February; a shared initial entry is not established.<br>[SM3](#source-sm3) |
| EX069<br>2024-04-29 | **Rain**<br>Exchange / customer | On-chain estimate approximately $14.8 million | Initial access not publicly confirmed → abnormal outflows across wallets | Unknown | **I**: Root cause and operator unresolved.<br>[SM2](#source-sm2) · [SM2024](#source-sm2024) |
| EX070<br>2024-05-31 | **DMM Bitcoin**<br>Exchange / customer | 4,502.9 BTC; approximately $305–308 million | Fake recruitment test compromised a Ginco employee endpoint and exposed session information → supplier-communication access likely used to manipulate a legitimate transaction request | TraderTraitor; FBI/DC3/NPA attribution | **P**: Investigators assessed request manipulation as likely, rather than establishing every step. Regulatory deficiencies are not proof of specific exploitation.<br>[DMM](#source-dmm) · [DMMREG](#source-dmmreg) |
| EX072<br>2024-06-09 (reported) | **Kraken deposit-crediting flaw**<br>Exchange / customer | Approximately $3 million withdrawn during disputed research; not counted as permanent net loss | Crediting implementation flaw → spendable balance without a completed real deposit | CertiK Skyfall; exploitation scope disputed | **P**: Technical mechanism is separated from research-authorization dispute; not attributed to Lazarus or classified as ordinary criminal theft.<br>[KRAKEN](#source-kraken) · [CERTIK24](#source-certik24) |
| EX073<br>2024-06-22 | **BtcTurk**<br>Exchange / customer | Research/media estimates approximately $54–55 million; platform confirmed hot-wallet impact | Initial access undisclosed → hot wallets for some assets affected | Unknown | **M**: Wallet attribution and amount partly rely on researchers' timing correlations. $5.3 million frozen is not automatically recovered.<br>[SM2](#source-sm2) · [CASA](#source-casa) · [BTCTURK24](#source-btcturk24) |
| EX071<br>2024-06 (early) | **Lykke**<br>Exchange / customer | Approximately $22.4–22.8 million | Initial access undisclosed → platform asset outflows | Unknown | **C**: Occurrence and disclosure dates differ; an index date is not treated as an exact attack time.<br>[SM2](#source-sm2) |
| EX074<br>2024-07-18 | **WazirX**<br>Exchange / customer | More than $230 million; common estimate approximately $235 million | Responsibility between WazirX and Liminal disputed → unexpected execution from a multisignature wallet | North Korea-linked attribution reported; disputed material does not establish the complete chain here | **P+I**: Victim disclosures are not independent judgments of supplier responsibility.<br>[WAZIR](#source-wazir) · [WAZIRELL](#source-wazirell) |
| EX075<br>2024-09-11 | **Indodax**<br>Exchange / customer | Approximately $22 million | Entry unconfirmed; affected withdrawal system was a research hypothesis → multiple asset outflows | Unknown | **I**: Research suspicions or exclusions are not a final root-cause finding.<br>[SM2](#source-sm2) · [SM2024](#source-sm2024) |
| EX076<br>2024-09-20 | **BingX**<br>Exchange / customer | Index estimate approximately $45 million; external estimates differ | Initial access undisclosed → abnormal hot-wallet transfers | Unknown | **I**: Net loss and recovery require separate confirmation.<br>[SM2](#source-sm2) · [SM2024](#source-sm2024) |
| EX077<br>2024-10-31 | **M2**<br>Exchange / customer | Approximately $13.7 million | Initial access undisclosed → multichain hot-wallet outflows | Unknown | **C**: The initial access method is undisclosed.<br>[SM2](#source-sm2) |
| EX078<br>2024-11-28 | **XT.com**<br>Exchange / customer | Approximately $1.7 million | Initial access undisclosed → abnormal platform asset transfer | Unknown | **C**: Abnormal outflow is not automatically explained as key exposure.<br>[SM2](#source-sm2) |

### 2025

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX079<br>2025-01-01 | **NoOnes**<br>Related service | Approximately $7.9 million | Platform described a Solana-bridge attack → bridge/wallet assets associated with a P2P service affected | Unknown | **C**: Not indiscriminately combined with pure CEX-wallet incidents.<br>[SM1](#source-sm1) |
| EX080<br>2025-01-23 | **Phemex**<br>Exchange / customer | Immunefi/SlowMist approximately $69.1 million; later media approximately $85 million | Full attack sequence undisclosed → multichain hot-wallet outflows | Some research suggests a North Korea link; not confirmed in this registry | **P+I+M**: Alternative estimate ranges are retained.<br>[SM1](#source-sm1) · [CASA](#source-casa) · [PHEMEX](#source-phemex) · [PHEMEX69](#source-phemex69) · [PHEMEX85](#source-phemex85) |
| EX081<br>2025-02-21 | **Bybit**<br>Exchange / customer | Approximately $1.46–1.5 billion | Safe developer endpoint and AWS session compromised → frontend tampering altered the transaction to be signed, affecting cold-wallet asset control | TraderTraitor; FBI attribution | **P+I**: The tampered transaction received valid signatures.<br>[BYBIT](#source-bybit) · [BYFBI](#source-byfbi) |
| EX082<br>2025-05-08 UTC | **BitoPro**<br>Exchange / customer | Approximately $11.5 million | Cloud-operations employee socially engineered; malware and AWS-session hijacking → transfers disguised as routine operations during wallet upgrade/migration | Platform assessed the methods as similar to those of Lazarus Group; not an attribution established in court | **P+I**: The platform's notice dates the incident to early May 9 local time; May 8 UTC reflects the time-zone difference.<br>[BITOPRO25](#source-bitopro25) · [SM1](#source-sm1) · [SM2025H1](#source-sm2025h1) |
| EX083<br>2025-05-15 (disclosed) | **Coinbase support-personnel incident**<br>Exchange / customer | Preliminary $180–400 million response and voluntary-reimbursement costs, not a wallet-theft total | Some outsourced support personnel bribed → customer information used in social-engineering fraud | Unknown | **P**: Data access is not direct withdrawal authority, but supports later fraud.<br>[COINBASE](#source-coinbase) · [COINBASESEC](#source-coinbasesec) |
| EX084<br>2025-06-18 | **Nobitex**<br>Exchange / customer | More than $90 million | Full initial access sequence undisclosed → assets sent to addresses assessed to be irrecoverable burn destinations | Gonjeshke Darande / Predatory Sparrow claimed responsibility | **I**: Political motive and destruction differ from ordinary laundering; national attribution is not established.<br>[NOBITEX](#source-nobitex) |
| EX085<br>2025-07-16 | **BigONE**<br>Exchange / customer | Approximately $27 million | Third-party attack and production compromise → account and risk-control logic manipulated; platform stated keys remained safe | Unknown | **P+M**: Public statement is not a complete independent forensic report.<br>[BIGONE](#source-bigone) · [BIGLOGIC](#source-biglogic) · [SM1](#source-sm1) · [BIGUSD](#source-bigusd) |
| EX086<br>2025-07-19 | **CoinDCX**<br>Exchange / customer | Approximately $44.2 million | Platform reported server intrusion → internal operating account for liquidity at a partner exchange affected | Unknown | **P+I**: Separate from principal customer cold wallets; linked to the 2026 legacy-address incident.<br>[CDX25](#source-cdx25) · [SM1](#source-sm1) · [SM2025](#source-sm2025) |
| EX087<br>2025-07-24 | **WOO X**<br>Exchange / customer | $14 million; 9 accounts | Malware in an external collaboration project compromised a developer endpoint → development, Kubernetes, and database access extended to accounts and withdrawals | Platform assessed North Korea-linked UNC4899/UNC5565 activity; report wording varies | **P**: Attribution comes from the platform postmortem, which uses several activity labels.<br>[WOO](#source-woo) |
| EX088<br>2025-08-14 | **BtcTurk**<br>Exchange / customer | Beosin tracing uses approximately $48 million; other directories differ | Initial access undisclosed → hot-wallet outflows | Unknown | **I**: Separate from the 2024 incident.<br>[SM1](#source-sm1) · [CASA](#source-casa) · [BTCTURK25](#source-btcturk25) |
| EX089<br>2025-08-31 (operation); 2025-09-08 (discovered) | **SwissBorg / Kiln**<br>Related service | Approximately 192,000 SOL; approximately $41–41.5 million | Kiln engineer's GitHub token stolen; CI yielded infrastructure credentials → transaction API returned malicious content changing withdrawal authority after customer signing | Unknown | **P**: Signing the malicious transaction on August 31 and discovering the intrusion on September 8 are distinct events.<br>[KILN](#source-kiln) · [SWISS](#source-swiss) |
| EX090<br>2025-11-27 | **Upbit**<br>Exchange / customer | Later estimate approximately KRW 44.5 billion, approximately $30.3 million | Entry unconfirmed → abnormal Solana-related asset outflows | Unknown | **M**: A potential flaw that could allow private-key recovery was found; this does not establish it as the incident's cause.<br>[SM1](#source-sm1) · [UPBIT25USD](#source-upbit25usd) |

### 2026

| ID / date | Platform / scope | Loss or impact | Initial access and affected control | Attribution | Evidence and limitations |
| --- | --- | --- | --- | --- | --- |
| EX092<br>2026-03–07; 2026-07-19 (reported) | **KuCoin / Zilliqa Ledger application**<br>Exchange / customer | KuCoin-specific loss undisclosed; ecosystem total not counted as exchange loss | Nonce-handling flaw in an old signing application → public signatures could expose private keys for specific accounts | Unknown | **P**: Chain project said a KuCoin cold-wallet anomaly prompted the report. Ecosystem figure of approximately 683 million ZIL includes later flows, not CEX net loss.<br>[ZIL](#source-zil) |
| EX091<br>2026-04-16 | **Grinex**<br>Exchange / customer | Estimated approximately $13.1–15 million | Initial access undisclosed → wallet assets transferred and converted | Platform blamed hostile states; independent attribution unconfirmed | **C**: Victim political allegations are not forensic conclusions.<br>[SM1](#source-sm1) |
| EX093<br>2026-09-24 | **Bitget**<br>Exchange / customer | Revised to $387.5 million from initial $351.6 million | Third-party security-product flaw exposed privileged internal credentials → forged withdrawal instructions executed through wallet systems | North Korea attribution by Chainalysis; researcher assessment | **P+I**: Platform ruled out private-key exposure. Amount revision reflects additional accounting, not continuing theft.<br>[BITGET](#source-bitget) · [BGAMT](#source-bgamt) · [BGCHAIN](#source-bgchain) |
| EX094<br>2026-10-21 | **CoinDCX legacy wallet**<br>Exchange / customer | 15.99 million USDT | Full attack method undisclosed; retired infrastructure affected → old addresses still received deposits, credited before sweeping; loss occurred after sweeping failed | Unknown | **P**: Linked to the 2025 incident; no confirmation that newly issued keys were stolen in this second incident.<br>[CDX26](#source-cdx26) |
| EX095<br>2026-10-29 | **Binance**<br>Exchange / customer | Later platform estimate approximately $6.3 billion; freezing is not recovery | Preliminary platform assessment: compromised DevOps endpoint and service-container access; additional breach points later found → unauthorized withdrawals submitted in container; complete attack sequence unknown | TraderTraitor; FBI attribution | **P+I**: Platform reported no evidence of key exposure. DevOps route is preliminary; details of obtaining authorization remain undisclosed.<br>[BNINITIAL26](#source-bninitial26) · [BINANCE26](#source-binance26) · [BNFBI](#source-bnfbi) · [BNELL](#source-bnell) |

## Source index

<a id="source-sm1"></a>
- [SM1 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange)

<a id="source-sm2"></a>
- [SM2 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=2)

<a id="source-sm3"></a>
- [SM3 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=3)

<a id="source-sm4"></a>
- [SM4 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=4)

<a id="source-sm5"></a>
- [SM5 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=5)

<a id="source-sm6"></a>
- [SM6 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=6)

<a id="source-sm7"></a>
- [SM7 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=7)

<a id="source-sm8"></a>
- [SM8 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=8)

<a id="source-sm9"></a>
- [SM9 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=9)

<a id="source-casa"></a>
- [CASA — casa.io](https://casa.io/exchange-hacks)

<a id="source-cs"></a>
- [CS — chainsec.io](https://www.chainsec.io/exchange-hacks)

<a id="source-shape"></a>
- [SHAPE — postmortem.io](https://postmortem.io/incidents/shapeshift--2016-04-19--cyberattack-postmortem/)

<a id="source-gatecoin"></a>
- [GATECOIN — csidb.net](https://www.csidb.net/csidb/incidents/8673c914-86b4-47c8-b3fe-0e776431f512/)

<a id="source-bfdoj"></a>
- [BFDOJ — justice.gov](https://www.justice.gov/usao-dc/2016-bitfinex-hack)

<a id="source-bffaq"></a>
- [BFFAQ — support.bitfinex.com](https://support.bitfinex.com/hc/en-us/articles/4417401349657-2016-Security-Breach-Bitcoin-Recovery-Frequently-Asked-Questions-FAQ)

<a id="source-bitcurex"></a>
- [BITCUREX — news.bitcoin.com](https://news.bitcoin.com/bitcurex-forced-million-theft/)

<a id="source-youbit"></a>
- [YOUBIT — en.yna.co.kr](https://en.yna.co.kr/view/AEN20171219015800320)

<a id="source-bithumb17"></a>
- [BITHUMB17 — bravenewcoin.com](https://bravenewcoin.com/insights/fourth-largest-bitcoin-exchange-bithumb-hacked-for-billions-of-won)

<a id="source-coincheck"></a>
- [COINCHECK — coincheckgroup.com](https://www.coincheckgroup.com/sec-filings/all-sec-filings/content/0001213900-25-007203/0001213900-25-007203.pdf)

<a id="source-bitgrail"></a>
- [BITGRAIL — techcrunch.com](https://techcrunch.com/2018/02/12/bitgrail-hack-nano/)

<a id="source-via"></a>
- [VIA — binance.com](https://www.binance.com/en/support/announcement/detail/360001547431)

<a id="source-eset"></a>
- [ESET — welivesecurity.com](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/)

<a id="source-gateetc"></a>
- [GATEETC — gate.com](https://www.gate.com/ru/announcements/article/16740)

<a id="source-cryptopia"></a>
- [CRYPTOPIA — grantthornton.co.nz](https://www.grantthornton.co.nz/globalassets/1.-member-firms/new-zealand/pdfs/cryptopia/2023/affidavit-of-david-ian-ruscoe-in-support-of-originating-application-1.pdf)

<a id="source-coinmama"></a>
- [COINMAMA — ccn.com](https://www.ccn.com/breaking-major-crypto-brokerage-coinmama-hacked-450000-users-affected-in-massive-worldwide-breach/)

<a id="source-binance19"></a>
- [BINANCE19 — binance.com](https://www.binance.com/en-AU/support/announcement/detail/360028031711)

<a id="source-bitopro19"></a>
- [BITOPRO19 — bitopro.com](https://www.bitopro.com/ns/announcements/173)

<a id="source-etc20"></a>
- [ETC20 — etccooperative.org](https://etccooperative.org/ETC-Coop-Board-Package-August-2020.pdf)

<a id="source-kucoin20"></a>
- [KUCOIN20 — kucoin.com](https://www.kucoin.com/fil/announcement/a-letter-from-kucoin-ceo-2020-2021-and-beyond)

<a id="source-exmo"></a>
- [EXMO — exmo.com](https://exmo.com/blog/en/notifications/exmo-security-incident-update)

<a id="source-liquid21"></a>
- [LIQUID21 — cointelegraph.com](https://cointelegraph.com/news/breaking-liquid-exchange-hacked-to-the-tune-of-80-million)

<a id="source-bitmart"></a>
- [BITMART — bitmart.com](https://www.bitmart.com/en-US/support/articles/7922665245339/7923672421147/4411998987419)

<a id="source-ascend"></a>
- [ASCEND — ascendex.com](https://ascendex.com/hi/support/articles/62199-dec-11-security-incident-timing-for-resuming-deposit-and-withdraw)

<a id="source-lcx"></a>
- [LCX — lcx.com](https://lcx.com/de/hot-wallet-incident-report)

<a id="source-cryptocom"></a>
- [CRYPTOCOM — crypto.com](https://crypto.com/nl/company-news/crypto-com-january-2022-updates/)

<a id="source-deribit"></a>
- [DERIBIT — cointelegraph.com](https://cointelegraph.com/news/deribit-crypto-exchange-halts-withdrawals-amid-28m-hot-wallet-hack)

<a id="source-threec"></a>
- [THREEC — 3commas.io](https://3commas.io/blog/notice-on-api-data-disclosure-incident)

<a id="source-threefaq"></a>
- [THREEFAQ — 3commas.io](https://3commas.io/blog/api-security-incident-faq)

<a id="source-gdac"></a>
- [GDAC — coindesk.com](https://www.coindesk.com/tech/2023/04/10/s-korean-crypto-exchange-gdac-hacked-for-nearly-13m)

<a id="source-coinsph"></a>
- [COINSPH — theblock.co](https://www.theblock.co/news/business/2023-10-20-philippines-based-exchange-coins-ph-appears-to-have-lost-12-2-million-xrp-in-possible-exploit-258701)

<a id="source-dmm"></a>
- [DMM — fbi.gov](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom)

<a id="source-dmmreg"></a>
- [DMMREG — lfb.mof.go.jp](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html)

<a id="source-kraken"></a>
- [KRAKEN — blog.kraken.com](https://blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug)

<a id="source-wazir"></a>
- [WAZIR — wazirx.com](https://wazirx.com/blog/important-update-cyber-attack-incident-and-measures-to-protect-your-assets/)

<a id="source-bybit"></a>
- [BYBIT — sygnia.co](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/)

<a id="source-byfbi"></a>
- [BYFBI — ic3.gov](https://www.ic3.gov/PSA/2025/PSA250226)

<a id="source-bitopro25"></a>
- [BITOPRO25 — bitopro.com](https://www.bitopro.com/ns/en-US/announcements/1226)

<a id="source-coinbase"></a>
- [COINBASE — coinbase.com](https://www.coinbase.com/en-nl/blog/protecting-our-customers-standing-up-to-extortionists)

<a id="source-coinbasesec"></a>
- [COINBASESEC — sec.gov](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm)

<a id="source-nobitex"></a>
- [NOBITEX — chainalysis.com](https://www.chainalysis.com/blog/nobitex-iranian-exchange-exploit-june-2025/)

<a id="source-bigone"></a>
- [BIGONE — bigone.zendesk.com](https://bigone.zendesk.com/hc/en-us/articles/48906456010393-Announcement-Regarding-BigONE-Security-Incident-on-16-July-2025)

<a id="source-biglogic"></a>
- [BIGLOGIC — bigoneeurasia.ladesk.com](https://bigoneeurasia.ladesk.com/275817-Temporary-Platform-Maintenance)

<a id="source-cdx25"></a>
- [CDX25 — coindcx.com](https://coindcx.com/blog/announcements/incident-report-july-19-2025)

<a id="source-woo"></a>
- [WOO — woox.io](https://woox.io/blog/july-24th-security-incident-post-mortem)

<a id="source-kiln"></a>
- [KILN — kiln.fi](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information)

<a id="source-swiss"></a>
- [SWISS — swissborg.com](https://swissborg.com/blog/swissborg-security-update-kiln-breach)

<a id="source-zil"></a>
- [ZIL — zilliqa.com](https://www.zilliqa.com/ledger-incident/post-mortem/)

<a id="source-bitget"></a>
- [BITGET — bitget.com](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)

<a id="source-bgamt"></a>
- [BGAMT — bitget.com](https://www.bitget.com/support/articles/12560603896108)

<a id="source-bgchain"></a>
- [BGCHAIN — chainalysis.com](https://www.chainalysis.com/blog/387m-bitget-theft-2026/)

<a id="source-cdx26"></a>
- [CDX26 — coindcx.com](https://coindcx.com/blog/coindcx-news/on-chain-wallet-activity-update-21-oct-2026)

<a id="source-binance26"></a>
- [BINANCE26 — binance.com](https://www.binance.com/en-TR/support/announcement/detail/d3306d9dca5243548c813b605e1d1751)

<a id="source-bnfbi"></a>
- [BNFBI — fbi.gov](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack)

<a id="source-eip"></a>
- [EIP — eips.ethereum.org](https://eips.ethereum.org/EIPS/eip-7702)

<a id="source-erc20"></a>
- [ERC20 — eips.ethereum.org](https://eips.ethereum.org/EIPS/eip-20)

<a id="source-ai"></a>
- [AI — cloud.google.com](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai)

<a id="source-iso"></a>
- [ISO — iso.org](https://www.iso.org/standard/27001)

<a id="source-maple"></a>
- [MAPLE — blockonomi.com](https://blockonomi.com/maplechange-hacked-scam/)

<a id="source-coinbase19"></a>
- [COINBASE19 — coinbase.com](https://www.coinbase.com/blog/responding-to-firefox-0-days-in-the-wild)

<a id="source-coinbase23"></a>
- [COINBASE23 — coinbase.com](https://www.coinbase.com/en-ca/blog/social-engineering-a-coinbase-case-study)

<a id="source-elliptic23"></a>
- [ELLIPTIC23 — elliptic.co](https://www.elliptic.co/insights/how-the-lazarus-group-is-stepping-up-crypto-hacks-and-changing-its-tactics/)

<a id="source-ccfaq"></a>
- [CCFAQ — coincheck.com](https://coincheck.com/info/faq_nem)

<a id="source-ccusd"></a>
- [CCUSD — investing.com](https://www.investing.com/news/stock-market-news/exclusive-coincheck-hackers-attempting-to-sell-stolen-cryptocurrency--executive-1171410)

<a id="source-coinrailusd"></a>
- [COINRAILUSD — en.yna.co.kr](https://en.yna.co.kr/view/AEN20180611009700320)

<a id="source-zaifusd"></a>
- [ZAIFUSD — investing.com](https://www.investing.com/news/cryptocurrency-news/japan-hit-by-another-cryptocurrency-heist-60-million-stolen-1616872)

<a id="source-upbit19usd"></a>
- [UPBIT19USD — koreatimes.co.kr](https://www.koreatimes.co.kr/economy/20191128/security-concerns-grow-over-cryptocurrency-exchanges)

<a id="source-liquidell"></a>
- [LIQUIDELL — elliptic.co](https://www.elliptic.co/insights/liquid-exchange-hacked-94-million-stolen/)

<a id="source-bitmart26"></a>
- [BITMART26 — bitmart.zendesk.com](https://bitmart.zendesk.com/hc/en-us/articles/56571281537051-Announcement-on-BitMart-s-Initial-Indicative-Proposal-and-Roadmap)

<a id="source-ascendusd"></a>
- [ASCENDUSD — theblock.co](https://www.theblock.co/news/regulation/2021-12-12-crypto-exchange-ascendex-hacked-for-78-million-in-latest-swindle-127231)

<a id="source-lcxcourt"></a>
- [LCXCOURT — hklaw.com](https://www.hklaw.com/-/media/files/generalpages/lcx-ag-v-doe/exhibit2_nyscefno8.pdf?la=en)

<a id="source-cryptodga"></a>
- [CRYPTODGA — dga.gov.sa](https://dga.gov.sa/sites/default/files/2023-08/Digital%20Fraud%20-%20Research%20Study.pdf)

<a id="source-sinbad"></a>
- [SINBAD — elliptic.co](https://www.elliptic.co/insights/sinbad-crypto-mixer-flagged-by-elliptic-sanctioned-and-seized/)

<a id="source-bitrue23"></a>
- [BITRUE23 — support.bitrue.com](https://support.bitrue.com/hc/en-001/articles/17538384324121-Update-on-Bitrue-s-Security-Breach)

<a id="source-polocert"></a>
- [POLOCERT — certik.com](https://www.certik.com/blog/poloniex-incident-analysis)

<a id="source-sm2024"></a>
- [SM2024 — slowmist.com](https://www.slowmist.com/report/2024-Blockchain-Security-and-AML-Annual-Report%28EN%29.pdf)

<a id="source-btcturk24"></a>
- [BTCTURK24 — theblock.co](https://www.theblock.co/news/regulation/2024-06-22-binance-freezes-5-million-in-funds-looted-from-btcturk-after-alleged-54-million-hack-of-turkish-exchange-301340)

<a id="source-wazirell"></a>
- [WAZIRELL — elliptic.co](https://www.elliptic.co/insights/235-million-lost-by-wazirx-in-north-korea-linked-breach/)

<a id="source-phemex"></a>
- [PHEMEX — phemex.com](https://phemex.com/announcements/phemex-hot-wallet-security-incident-update-and-timeline)

<a id="source-phemex69"></a>
- [PHEMEX69 — assets.ctfassets.net](https://assets.ctfassets.net/t3wqy70tc3bv/1Vj4VSUY97UCFp3mLgG7ov/f1de70826f9c2992c481b124d849aa55/Immunefi_Crypto_Losses_January_2025.pdf)

<a id="source-phemex85"></a>
- [PHEMEX85 — bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/hackers-steal-85-million-worth-of-cryptocurrency-from-phemex/amp/)

<a id="source-sm2025h1"></a>
- [SM2025H1 — slowmist.com](https://www.slowmist.com/report/SlowMist-first-half-of-the-2025-report%28EN%29.pdf)

<a id="source-sm2025"></a>
- [SM2025 — slowmist.com](https://www.slowmist.com/report/2025-Blockchain-Security-and-AML-Annual-Report%28EN%29.pdf)

<a id="source-bigusd"></a>
- [BIGUSD — theblock.co](https://www.theblock.co/news/regulation/2025-07-16-bigone-hack-362814)

<a id="source-btcturk25"></a>
- [BTCTURK25 — beosin.com](https://www.beosin.com/resources/fund-flow-analysis-of-btcturk-48-million-hack)

<a id="source-upbit25usd"></a>
- [UPBIT25USD — koreatimes.co.kr](https://www.koreatimes.co.kr/economy/cryptocurrency/20251208/repeat-cyberthefts-raise-questions-about-upbits-security-governance)

<a id="source-bnell"></a>
- [BNELL — elliptic.co](https://www.elliptic.co/insights/binance-largest-hack-in-history/)

<a id="source-cert2019"></a>
- [CERT2019 — cert.europa.eu](https://cert.europa.eu/publications/threat-intelligence/threat-memo-191126-1/pdf)

<a id="source-ca2025"></a>
- [CA2025 — chainalysis.com](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026-/)

<a id="source-cryptousd"></a>
- [CRYPTOUSD — theblock.co](https://www.theblock.co/news/regulation/2022-01-19-crypto-com-ceo-confirms-400-accounts-were-compromised-in-recent-hack-130857)

<a id="source-applejeus"></a>
- [APPLEJEUS — kaspersky.co.uk](https://www.kaspersky.co.uk/blog/lazarus-crypto-exchange-attack/14314/)

<a id="source-trader2022"></a>
- [TRADER2022 — ic3.gov](https://www.ic3.gov/CSA/2022/220418.pdf)

<a id="source-cb21notice"></a>
- [CB21NOTICE — oag.ca.gov](https://oag.ca.gov/system/files/09-24-2021%20Customer%20Notification.pdf)

<a id="source-mangomech"></a>
- [MANGOMECH — chainalysis.com](https://www.chainalysis.com/blog/oracle-manipulation-attacks-rising/)

<a id="source-parity17"></a>
- [PARITY17 — openzeppelin.com](https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7)

<a id="source-bfdoj24"></a>
- [BFDOJ24 — justice.gov](https://www.justice.gov/archives/opa/pr/bitfinex-hacker-sentenced-money-laundering-conspiracy-involving-billions-stolen)

<a id="source-bnresume26"></a>
- [BNRESUME26 — binance.com](https://www.binance.com/en/support/announcement/detail/73911fb819b240f88b88256bdd318eda)

<a id="source-fbi24social"></a>
- [FBI24SOCIAL — ic3.gov](https://www.ic3.gov/PSA/2024/PSA240903)

<a id="source-nistauth"></a>
- [NISTAUTH — pages.nist.gov](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/)

<a id="source-nistsession"></a>
- [NISTSESSION — pages.nist.gov](https://pages.nist.gov/800-63-4/sp800-63b/session/)

<a id="source-certik24"></a>
- [CERTIK24 — certik.com](https://www.certik.com/blog/certik-statement-on-kraken-vulnerability)

<a id="source-owasptx"></a>
- [OWASPTX — cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)

<a id="source-owaspbiz"></a>
- [OWASPBIZ — cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)

<a id="source-bninitial26"></a>
- [BNINITIAL26 — binance.com](https://www.binance.com/en/support/announcement/detail/c5a8729a97ac486d963784d96c5642d7)
