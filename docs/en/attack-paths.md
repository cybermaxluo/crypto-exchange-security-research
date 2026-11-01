# Six Attack Paths Against Crypto Exchanges

**English** | [简体中文](../zh-CN/attack-paths.md)

The paths describe how control over funds fails. Initial access methods, tools, and actor attribution are recorded separately. P1–P5 concern platform funds and accounts; P6 extends to customers. An incident can traverse multiple paths, so these are neither mutually exclusive statistical categories nor a complete inventory of cyber risk.

## Classification and coverage

Each case retains initial access, subsequent permission changes, actor attribution, and evidence type. Do not add path-level case counts as though they were distinct incidents.

| Risk branch | Path | Coverage |
| --- | --- | --- |
| Private keys, backups, signing nonce defects | P1 | Distinguish secret exposure from implementation flaws |
| Malicious frontend, API output, request display | P2 | Separate business confirmation from custody signing |
| Account theft, recovery flaws, MFA bypass, production instructions, wallet permissions | P3 | Cloud compromise is not a common prerequisite |
| Stolen trading API credentials; price or collateral manipulation using attacker-owned accounts | P4 | Valid authentication can coexist with economic exploitation |
| False deposits, erroneous credits, replay, reorganization, double spending | P5 | Test internal accounting flaws separately from external settlement changes |
| Deception leading to customer transfers or grants | P6 | Customer-side extension; not necessarily platform-wallet compromise |
| Contract permissions and external protocols | Map to the affected control | Parity and Mango are mechanism comparisons outside the CEX sample; protocol risk is not exhaustively covered |
| Ransomware, DDoS, data exposure without fund impact | Outside this model | Remain cyber risks; six fund paths do not replace a complete threat model |

## P1. Signing-material compromise

**Sequence:** storage exposure or implementation flaw → sufficient signing material → valid signature → transfer outside the original business workflow.

**Failed control:** failures in key protection, backup isolation, or the signing implementation allow the attacker to produce valid signatures independently.

**Evidence:** generation, read, export, backup, and recovery records; nonce behavior and implementation versions; correspondence between on-chain transactions, business requests, and signing records. On-chain data alone does not identify the broadcaster.

**Validation:** within the actual architecture, simulate compromise of one host, backup, or one party's signing material, then test the remaining signing requirements. Where a complete private key is exposed, separately test asset migration and key retirement. Suspending the exchange's own signing service does not establish that the key is unusable.

**Limits:** BitMart did not fully disclose initial entry. Zilliqa illustrates an implementation flaw and does not require prior endpoint intrusion.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX008 — Coincheck 2018 | Platform inference: malware on an employee endpoint led into the internal network and to NEM server keys; assets left a hot wallet | Unknown actor. Coin amounts, dollar estimates, and reimbursement figures differ and must be kept separate. | [COINCHECK](https://www.coincheckgroup.com/sec-filings/all-sec-filings/content/0001213900-25-007203/0001213900-25-007203.pdf) · [SM9](https://hacked.slowmist.io/?c=Exchange&page=9) · [CCFAQ](https://coincheck.com/info/faq_nem) · [CCUSD](https://www.investing.com/news/stock-market-news/exclusive-coincheck-hackers-attempting-to-sell-stolen-cryptocurrency--executive-1171410) |
| EX042 — BitMart 2021 | Confirmed private-key theft; initial entry not fully disclosed; Ethereum and BSC hot wallets affected | Unknown actor. The monetary sample uses a later platform retrospective, with a $196 million sensitivity alternative. The revised total was not independently audited. | [BITMART](https://www.bitmart.com/en-US/support/articles/7922665245339/7923672421147/4411998987419) · [BITMART26](https://bitmart.zendesk.com/hc/en-us/articles/56571281537051-Announcement-on-BitMart-s-Initial-Indicative-Proposal-and-Roadmap) |
| EX092 — KuCoin / Zilliqa Ledger application 2026 | Legacy signing nonce handling allowed particular account keys to be recovered from public signatures | Unknown actor. Zilliqa said a KuCoin cold-wallet anomaly triggered reporting. The approximately 683 million ZIL ecosystem figure includes later flows and is not a CEX net-loss estimate. | [ZIL](https://www.zilliqa.com/ledger-incident/post-mortem/) |

## P2. Transaction construction or display is altered

**Sequence:** transaction builder or display is tampered with → intended operation is replaced → the malicious operation receives business approval or a signature → an unintended asset operation executes.

**Failed control:** output from an upstream service is accepted as evidence of business approval; the change in transaction semantics or permissions is not rejected.

**Evidence:** CI/deployment identities; differences between running resources, API responses, and released artifacts; approved purpose, signed bytes, and resulting authority.

**Validation:** replace a response used in the actual business workflow and verify the request source, business approval, final transaction bytes, and state at execution. Test whether the transaction builder can forge approval records, including wallet-specific triggers and authority changes. Record where business approval and transaction signing each reject the substituted operation.

**Limits:** Gate.io involved withdrawal-page request tampering, not a cold-wallet multisignature flow. Investigators assessed transaction-request manipulation at DMM as likely; they did not establish every step. The cases follow different attack sequences.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX016 — Gate.io / StatCounter 2018 | Compromised analytics JavaScript selectively changed transaction information on the withdrawal page | Unknown actor. Triggers included page path, amount, or balance. ESET did not establish a reliable theft total; this is not classified as private-key exposure. | [ESET](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/) |
| EX070 — DMM Bitcoin 2024 | Recruitment-test lure compromised a Ginco employee endpoint/session; supplier communications were likely used to manipulate a legitimate request | TraderTraitor, attributed jointly by FBI/DC3/Japanese police. Retain the likely assessment. Regulatory deficiencies do not themselves prove exploitation. | [DMM](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom) · [DMMREG](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html) |
| EX081 — Bybit 2025 | Safe developer endpoint and AWS session compromised; frontend tampering affected the transaction signed from a cold wallet | TraderTraitor, FBI attribution. This is not evidence of a broken multisignature cryptographic algorithm. | [BYBIT](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/) · [BYFBI](https://www.ic3.gov/PSA/2025/PSA250226) |
| EX089 — SwissBorg / Kiln 2025 | A stolen GitHub token led through CI to infrastructure credentials; the transaction-building API returned a malicious transaction that changed withdrawal authority after the customer signed it | Unknown actor. August 31 signing and September 8 discovery are distinct events. | [KILN](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information) · [SWISS](https://swissborg.com/blog/swissborg-security-update-kiln-breach) |

## P3. Account or withdrawal-authorization takeover

**Sequence:** account recovery or backend controls are compromised → the attacker impersonates an authorized identity or rewrites its records → the platform accepts the withdrawal authorization → funds are paid out.

**Failed control:** account, backend-service, or wallet permissions recognize the attacker as authorized to spend. Cloud access is not required for every branch.

**Evidence:** login, recovery, MFA changes, sessions; production/database writes, service identities, withdrawal instructions; wallet owner, module, threshold, and execution-authority changes.

**Validation:** test customer recovery, forged instructions from production identities, and wallet permission checks separately. Examine whether normal and recovery flows bypass the same intended protection.

**Limits:** Coinbase 2021 is a customer-recovery branch, WOO X a production-write branch, and Parity an external contract-permission example. They do not form one common intrusion chain.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX098 — Coinbase SMS recovery 2021 | Attackers already had customers' email addresses, passwords, phone numbers, and email access; initial acquisition is unknown. The SMS-recovery flaw yielded authentication tokens, enabling account access and fund transfers | Unknown actor. This does not establish that every MFA mechanism failed. Precise detection, remediation, and recovery times were not given. | [CB21NOTICE](https://oag.ca.gov/system/files/09-24-2021%20Customer%20Notification.pdf) |
| EX085 — BigONE 2025 | Third-party attack affected production; account and risk logic manipulated; platform stated keys remained safe | Unknown actor. Disclosure is not a complete independent forensic report. | [BIGONE](https://bigone.zendesk.com/hc/en-us/articles/48906456010393-Announcement-Regarding-BigONE-Security-Incident-on-16-July-2025) · [BIGLOGIC](https://bigoneeurasia.ladesk.com/275817-Temporary-Platform-Maintenance) · [SM1](https://hacked.slowmist.io/?c=Exchange) · [BIGUSD](https://www.theblock.co/news/regulation/2025-07-16-bigone-hack-362814) |
| EX087 — WOO X 2025 | Malicious external collaboration project compromised a developer endpoint; development, Kubernetes, and database access extended into account/withdrawal control | Platform assessed North Korea-linked UNC4899/UNC5565 activity. Wording varies; aliases are not treated as unconditionally interchangeable. | [WOO](https://woox.io/blog/july-24th-security-incident-post-mortem) |
| EX093 — Bitget 2026 | Third-party security-product vulnerability exposed privileged internal credentials; forged withdrawal commands executed through the wallet system | Chainalysis attributed North Korea-linked activity. Platform excluded key leakage. The revised amount reflected additional accounting, not continuing theft. | [BITGET](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response) · [BGAMT](https://www.bitget.com/support/articles/12560603896108) · [BGCHAIN](https://www.chainalysis.com/blog/387m-bitget-theft-2026/) |

## P4. Trading and valuation manipulation

**Sequence:** stolen trading access or own accounts → abusive trades/price movement → value transfer or inflated collateral → withdrawal or borrowing of real assets.

**Failed control:** trading authority or price input transfers value or exaggerates borrowing capacity. Accounts and signatures can remain valid.

**Evidence:** API-key creation, request origins, and deviations from normal use; order-book depth, concentrated trading, linked accounts, and valuation sources; positions, unrealized gains, borrowing limits, and actual liquidation capacity.

**Validation:** separately test harmful trades using stolen API credentials and price manipulation using attacker-owned accounts in thin markets. Follow value across spot trading, collateral, lending, and withdrawals.

**Limits:** Mango is a DEX mechanism comparison outside the CEX sample. Price moves or ordinary arbitrage alone do not prove an attack. VIA external withdrawals were blocked while some trades remained irreversible.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX010 — Binance VIA 2018 | Sustained phishing obtained customer credentials, which were used to create API keys; trading permissions transferred value across accounts; subsequent withdrawals were blocked | Unknown actor. Thirty-one prefunded accounts sold VIA; some victim buys matched uninvolved parties. Blocked external withdrawal does not mean zero customer loss. | [VIA](https://www.binance.com/en/support/announcement/detail/360001547431) |
| EX050 — 3Commas / exchange accounts 2022 | Supplier database exposed API information; customer trading accounts suffered unauthorized trades | Unknown actor. These were not exchange master-wallet private keys; exposed-record count is not victim count. | [THREEC](https://3commas.io/blog/notice-on-api-data-disclosure-incident) · [THREEFAQ](https://3commas.io/blog/api-security-incident-faq) |

## P5. Spendable balances lack valid settlement

**Sequence:** crediting flaw or double spend → available balance → conversion/withdrawal → asset shortfall.

**Failed control:** the available balance is not backed by assets that have actually settled and remain under the exchange's control. A reorganization may invalidate the deposit after the exchange has paid out.

**Evidence:** original chain events, confirmation/reorganization state; crediting rules, idempotency keys, balance changes; subsequent trading, collateral, borrowing, multichain withdrawal.

**Validation:** replay incomplete deposits, reorgs, and duplicate events. Determine whether the resulting balance remains usable across products and when restrictions actually take effect.

**Limits:** Kraken involves research and disputed authorization; it is not counted as an ordinary criminal-theft event. Extending tests into lending is a proposed validation scenario.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX017 — Gate.io / ETC 2019 | ETC reorganization/double spend removed deposits that had been credited | Unknown actor. Returned funds are not the total attack amount; exchange-server intrusion is not implied. | [GATEETC](https://www.gate.com/ru/announcements/article/16740) |
| EX032 — OKEx / ETC 2020 | ETC majority-hashrate attack/reorganization invalidated deposits after confirmation and payout | Unknown actor. Settlement-finality risk, not a hot-wallet key leak. | [ETC20](https://etccooperative.org/ETC-Coop-Board-Package-August-2020.pdf) |
| EX072 — Kraken 2024 | Crediting implementation created balances without completed real deposits | CertiK Skyfall research team; exploitation scope disputed. Technical mechanism and authorization dispute are separate; no Lazarus attribution. | [KRAKEN](https://blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug) · [CERTIK24](https://www.certik.com/blog/certik-statement-on-kraken-vulnerability) |

## P6. Deceived customers authorize operations

**Sequence:** misuse brand or customer information → fabricate trusted identity → customer accepts a false explanation → customer transfers funds or grants authority.

**Failed control:** the attacker deceives the customer's understanding of the operation. Platform private keys need not be stolen, and not every attempt requires prior data leakage.

**Evidence:** support queries/exports, recovery records, customer reports, and links between exposed customer groups and unusual asset activity.

**Validation:** use authorized exercises to test support-data access/export restrictions and coordinated treatment of recovery, sessions, and fund activity involving exposed customers.

**Limits:** distinguish this from P3, where the attacker takes over and directly withdraws. Customer-side losses do not automatically mean platform custody assets were stolen.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX083 — Coinbase support-personnel incident 2025 | Some outsourced support workers were bribed; customer information enabled social-engineering fraud | Unknown actor. Data access did not itself provide direct withdrawal authority, but supported later fraud. | [COINBASE](https://www.coinbase.com/en-nl/blog/protecting-our-customers-standing-up-to-extortionists) · [COINBASESEC](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm) |

## External mechanism comparisons

- **M01 — Mango Markets 2022 → P4.** The attacker used their own accounts to manipulate prices in a thin market and borrow against inflated unrealized gains. Stolen API credentials were not a prerequisite. This DEX example is excluded from exchange-event and loss counts.
- **M02 — Parity 2017 → P3.** An initialization-permission flaw allowed owners and thresholds to be rewritten, enabling spending without the original keys. This external contract-wallet example is excluded from exchange-event and loss counts.

Case identifiers resolve through the [registry](../../data/case-registry.csv), which lists source identifiers and URLs. The [source index](../../data/sources.json) retains the referenced URLs. Use the [defense matrix](defense-matrix.md) to assign implementation, review, and acceptance responsibilities.

## Sources

- [COINCHECK — coincheckgroup.com](https://www.coincheckgroup.com/sec-filings/all-sec-filings/content/0001213900-25-007203/0001213900-25-007203.pdf)
- [SM9 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange&page=9)
- [CCFAQ — coincheck.com](https://coincheck.com/info/faq_nem)
- [CCUSD — investing.com](https://www.investing.com/news/stock-market-news/exclusive-coincheck-hackers-attempting-to-sell-stolen-cryptocurrency--executive-1171410)
- [BITMART — bitmart.com](https://www.bitmart.com/en-US/support/articles/7922665245339/7923672421147/4411998987419)
- [BITMART26 — bitmart.zendesk.com](https://bitmart.zendesk.com/hc/en-us/articles/56571281537051-Announcement-on-BitMart-s-Initial-Indicative-Proposal-and-Roadmap)
- [ZIL — zilliqa.com](https://www.zilliqa.com/ledger-incident/post-mortem/)
- [ESET — welivesecurity.com](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/)
- [DMM — fbi.gov](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom)
- [DMMREG — lfb.mof.go.jp](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html)
- [BYBIT — sygnia.co](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/)
- [BYFBI — ic3.gov](https://www.ic3.gov/PSA/2025/PSA250226)
- [KILN — kiln.fi](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information)
- [SWISS — swissborg.com](https://swissborg.com/blog/swissborg-security-update-kiln-breach)
- [CB21NOTICE — oag.ca.gov](https://oag.ca.gov/system/files/09-24-2021%20Customer%20Notification.pdf)
- [BIGONE — bigone.zendesk.com](https://bigone.zendesk.com/hc/en-us/articles/48906456010393-Announcement-Regarding-BigONE-Security-Incident-on-16-July-2025)
- [BIGLOGIC — bigoneeurasia.ladesk.com](https://bigoneeurasia.ladesk.com/275817-Temporary-Platform-Maintenance)
- [SM1 — hacked.slowmist.io](https://hacked.slowmist.io/?c=Exchange)
- [BIGUSD — theblock.co](https://www.theblock.co/news/regulation/2025-07-16-bigone-hack-362814)
- [WOO — woox.io](https://woox.io/blog/july-24th-security-incident-post-mortem)
- [BITGET — bitget.com](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)
- [BGAMT — bitget.com](https://www.bitget.com/support/articles/12560603896108)
- [BGCHAIN — chainalysis.com](https://www.chainalysis.com/blog/387m-bitget-theft-2026/)
- [VIA — binance.com](https://www.binance.com/en/support/announcement/detail/360001547431)
- [THREEC — 3commas.io](https://3commas.io/blog/notice-on-api-data-disclosure-incident)
- [THREEFAQ — 3commas.io](https://3commas.io/blog/api-security-incident-faq)
- [GATEETC — gate.com](https://www.gate.com/ru/announcements/article/16740)
- [ETC20 — etccooperative.org](https://etccooperative.org/ETC-Coop-Board-Package-August-2020.pdf)
- [KRAKEN — blog.kraken.com](https://blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug)
- [CERTIK24 — certik.com](https://www.certik.com/blog/certik-statement-on-kraken-vulnerability)
- [COINBASE — coinbase.com](https://www.coinbase.com/en-nl/blog/protecting-our-customers-standing-up-to-extortionists)
- [COINBASESEC — sec.gov](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm)
- [MANGOMECH — chainalysis.com](https://www.chainalysis.com/blog/oracle-manipulation-attacks-rising/)
- [PARITY17 — openzeppelin.com](https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7)
