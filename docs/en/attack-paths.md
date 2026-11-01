# Six Attack Paths Against Crypto Exchanges

[Repository home](../../README.md) · **English** | [简体中文](../zh-CN/attack-paths.md)

[Research](research.md) · **Attack paths** · [Defense matrix](defense-matrix.md) · [Case catalogue](case-catalogue.md) · [Methodology](methodology.md)

These six paths describe how attackers bypass or compromise controls over funds. Initial access methods, tools, and actor attribution are recorded separately. P1–P5 concern platform funds and accounts; P6 extends to customers. One incident may involve several paths. The categories therefore overlap and do not cover every type of cyber risk.

## Classification and coverage

Each case records the initial access method, subsequent permission changes, attacker attribution, and source types. Do not add path-level case counts as though they were distinct incidents.

| Risk | Path | Coverage |
| --- | --- | --- |
| Private keys, backups, signing nonce defects | P1 | Check both stolen keys and signing flaws that allow a key to be recovered |
| Malicious frontend, API output, request display | P2 | Verify approval of the intended operation separately from the custody signature |
| Account theft, recovery flaws, MFA bypass, production instructions, wallet permissions | P3 | Includes flaws in account recovery, production write access, and wallet permission checks |
| Stolen trading API credentials; price or collateral manipulation using attacker-owned accounts | P4 | An authenticated trade can still cause losses through manipulation |
| False deposits, erroneous credits, replay, reorganization, double spending | P5 | Test internal accounting flaws separately from external settlement changes |
| Deception that induces customers to transfer funds or grant permissions | P6 | Targets customers; does not necessarily compromise an exchange wallet |
| Contract permissions and collateral protocols: Parity and Mango | P3 / P4 | These two cases illustrate attack mechanisms and are excluded from the CEX sample; other protocols require separate analysis |
| Ransomware, DDoS, data exposure without fund impact | Outside this model | Still part of the threat model, but outside these six paths to financial loss |

## P1. Signing-material compromise

**Sequence:** exposed key storage or a signing-implementation flaw → attacker obtains enough material to sign → valid signature → transfer outside the exchange's approval workflow.

**Failed control:** failures in key protection, backup isolation, or the signing implementation allow the attacker to produce valid signatures independently.

**Evidence:** key-generation, access, export, backup, and recovery records; nonce behavior and implementation versions; correspondence between on-chain transactions, business requests, and signing records. On-chain data alone does not identify the broadcaster.

**Validation:** within the actual architecture, simulate compromise of one host, backup, or one party's signing material, then test which additional requirements still prevent signing. Where a complete private key is exposed, separately test asset migration and key retirement. Suspending the exchange's own signing service does not establish that the key is unusable.

**Case notes:** BitMart confirmed private-key theft but did not fully disclose the initial intrusion method. In the Zilliqa incident, a nonce-handling flaw in a legacy signing application allowed private keys for affected accounts to be recovered from public signatures.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX008 — Coincheck 2018 | Platform assessment: malware on an employee endpoint enabled access to the internal network and theft of keys from the NEM server; assets left a hot wallet | Unknown actor. Coin amounts, dollar estimates, and reimbursement figures differ and must be kept separate. | [COINCHECK](https://www.coincheckgroup.com/sec-filings/all-sec-filings/content/0001213900-25-007203/0001213900-25-007203.pdf) · [SM9](https://hacked.slowmist.io/?c=Exchange&page=9) · [CCFAQ](https://coincheck.com/info/faq_nem) · [CCUSD](https://www.investing.com/news/stock-market-news/exclusive-coincheck-hackers-attempting-to-sell-stolen-cryptocurrency--executive-1171410) |
| EX042 — BitMart 2021 | Confirmed private-key theft; initial entry not fully disclosed; Ethereum and BSC hot wallets affected | Unknown actor. The loss sample uses a later platform retrospective, with $196 million used as an alternative estimate in the sensitivity analysis. The revised total was not independently audited. | [BITMART](https://www.bitmart.com/en-US/support/articles/7922665245339/7923672421147/4411998987419) · [BITMART26](https://bitmart.zendesk.com/hc/en-us/articles/56571281537051-Announcement-on-BitMart-s-Initial-Indicative-Proposal-and-Roadmap) |
| EX092 — KuCoin / Zilliqa Ledger application 2026 | A nonce-handling flaw in the legacy signing flow allowed private keys for affected accounts to be recovered from public signatures | Unknown actor. Zilliqa said a KuCoin cold-wallet anomaly triggered reporting. The approximately 683 million ZIL ecosystem figure includes later flows and is not a CEX net-loss estimate. | [ZIL](https://www.zilliqa.com/ledger-incident/post-mortem/) |

## P2. Transaction tampering

**Sequence:** transaction builder or display is tampered with → intended operation is replaced → the malicious operation is approved or signed → an unauthorized operation involving assets is executed.

**Failed control:** output from an upstream service is accepted as proof that the requested operation was approved; the change in transaction semantics or permissions is not rejected.

**Evidence:** CI/deployment identities; differences between deployed resources, live API responses, and release artifacts; approved purpose, signed bytes, and resulting authority.

**Validation:** replace a response used in the actual business workflow and verify the request source, business approval, final transaction bytes, and state at execution. Test whether the transaction builder can forge approval records, including wallet-specific triggers and authority changes. Record whether the approval and signing checks each reject the substituted operation, and at which stage.

**Case notes:** The Gate.io attack modified requests on the customer withdrawal page. The joint DMM investigation assessed that a legitimate transaction request was likely manipulated; the full sequence has not been disclosed.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX016 — Gate.io / StatCounter 2018 | Compromised analytics JavaScript selectively changed transaction information on the withdrawal page | Unknown actor. Triggers included page path, amount, or balance. ESET confirmed withdrawal-page request tampering but did not establish a reliable theft total. | [ESET](https://www.welivesecurity.com/2018/11/06/supply-chain-attack-cryptocurrency-exchange-gate-io/) |
| EX070 — DMM Bitcoin 2024 | Recruitment-test lure compromised a Ginco employee endpoint/session; supplier communications were likely used to manipulate a legitimate request | TraderTraitor, attributed jointly by FBI/DC3/Japanese police. Request manipulation remains an assessment of what likely happened. Regulatory deficiencies do not themselves prove exploitation. | [DMM](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom) · [DMMREG](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html) |
| EX081 — Bybit 2025 | Safe developer endpoint and AWS session compromised; frontend tampering affected the transaction signed from a cold wallet | TraderTraitor, FBI attribution. The tampered transaction received valid signatures. | [BYBIT](https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/) · [BYFBI](https://www.ic3.gov/PSA/2025/PSA250226) |
| EX089 — SwissBorg / Kiln 2025 | A stolen GitHub token led through CI to infrastructure credentials; the transaction-building API returned a malicious transaction that changed withdrawal authority after the customer signed it | Unknown actor. August 31 signing and September 8 discovery are distinct events. | [KILN](https://www.kiln.fi/post/re-enablement-of-kiln-services-and-security-incident-information) · [SWISS](https://swissborg.com/blog/swissborg-security-update-kiln-breach) |

## P3. Account or withdrawal-authorization takeover

**Sequence:** account recovery or backend controls are compromised → the attacker impersonates an authorized identity or rewrites its records → the platform accepts the withdrawal authorization → funds are paid out.

**Failed control:** a flaw in account recovery, backend authorization, or wallet permission checks grants the attacker financial authority they should not have.

**Evidence:** login, recovery, MFA changes, sessions; production/database writes, service identities, withdrawal instructions; wallet owner, module, threshold, and execution-authority changes.

**Validation:** test customer recovery, forged instructions from production identities, and wallet permission checks separately. Check whether either the normal workflow or account recovery can bypass the intended control.

**Case notes:** In Coinbase 2021, attackers used an SMS account-recovery flaw to obtain authentication tokens. At WOO X, production write access let attackers change customer identity records. Parity illustrates wallet-permission risk: an initialization flaw allowed the wallet owners and signing threshold to be changed.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX098 — Coinbase SMS recovery 2021 | Attackers already had customers' email addresses, passwords, phone numbers, and email access; initial acquisition is unknown. The SMS-recovery flaw yielded authentication tokens, enabling account access and fund transfers | Unknown actor. The disclosed flaw does not establish a bypass of other MFA methods. Precise detection, remediation, and recovery times were not given. | [CB21NOTICE](https://oag.ca.gov/system/files/09-24-2021%20Customer%20Notification.pdf) |
| EX085 — BigONE 2025 | Third-party attack affected production; account and risk logic manipulated; platform stated keys remained safe | Unknown actor. Disclosure is not a complete independent forensic report. | [BIGONE](https://bigone.zendesk.com/hc/en-us/articles/48906456010393-Announcement-Regarding-BigONE-Security-Incident-on-16-July-2025) · [BIGLOGIC](https://bigoneeurasia.ladesk.com/275817-Temporary-Platform-Maintenance) · [SM1](https://hacked.slowmist.io/?c=Exchange) · [BIGUSD](https://www.theblock.co/news/regulation/2025-07-16-bigone-hack-362814) |
| EX087 — WOO X 2025 | Malicious external collaboration project compromised a developer endpoint; development, Kubernetes, and database access extended into account/withdrawal control | Platform assessed North Korea-linked UNC4899/UNC5565 activity. The report uses different UNC labels; these are not assumed to identify the same group. | [WOO](https://woox.io/blog/july-24th-security-incident-post-mortem) |
| EX093 — Bitget 2026 | Third-party security-product vulnerability exposed privileged internal credentials; forged withdrawal commands executed through the wallet system | Chainalysis attributed North Korea-linked activity. The platform ruled out private-key exposure. The revised amount reflected additional accounting, not continuing theft. | [BITGET](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response) · [BGAMT](https://www.bitget.com/support/articles/12560603896108) · [BGCHAIN](https://www.chainalysis.com/blog/387m-bitget-theft-2026/) |

## P4. Trading and valuation manipulation

**Sequence:** stolen trading credentials or attacker-owned accounts → abusive trades or price manipulation → value transferred to other accounts or collateral overvalued → withdrawal or borrowing of real assets.

**Failed control:** trading or valuation controls allow harmful trades or inflated prices to transfer value or increase borrowing capacity. The accounts and signatures involved may be valid.

**Evidence:** API-key creation, request origins, and deviations from normal use; order-book depth, concentrated trading, linked accounts, and valuation sources; positions, unrealized gains, borrowing limits, and actual liquidation capacity.

**Validation:** separately test harmful trades using stolen API credentials and price manipulation using attacker-owned accounts in thin markets. Follow value across spot trading, collateral, lending, and withdrawals.

**Case notes:** In the VIA incident, the platform blocked external withdrawals, but some victim trades could not be reversed. Mango illustrates collateral-valuation manipulation and is excluded from the CEX sample. Assessing manipulation also requires examination of orders, account relationships, and fund flows.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX010 — Binance VIA 2018 | Sustained phishing obtained customer credentials, which were used to create API keys; attackers used trading access to transfer value across accounts; subsequent withdrawals were blocked | Unknown actor. Thirty-one prefunded accounts sold VIA; some buy orders from victim accounts matched orders from uninvolved counterparties. Blocked external withdrawal does not mean zero customer loss. | [VIA](https://www.binance.com/en/support/announcement/detail/360001547431) |
| EX050 — 3Commas / exchange accounts 2022 | Supplier database exposed API information; customer trading accounts suffered unauthorized trades | Unknown actor. These were not exchange master-wallet private keys; exposed-record count is not victim count. | [THREEC](https://3commas.io/blog/notice-on-api-data-disclosure-incident) · [THREEFAQ](https://3commas.io/blog/api-security-incident-faq) |

## P5. Erroneous crediting and double spending

**Sequence:** crediting flaw or double spend → available balance → conversion/withdrawal → asset shortfall.

**Failed control:** the available balance is not backed by assets that have actually settled and remain under the exchange's control. A reorganization may invalidate the deposit after the exchange has paid out.

**Evidence:** original chain events, confirmation/reorganization state; crediting rules, idempotency keys, balance changes; subsequent trading, collateral, borrowing, multichain withdrawal.

**Validation:** replay incomplete deposits, reorgs, and duplicate events. Determine whether the resulting balance remains usable across products and when restrictions actually take effect.

**Case notes:** The Kraken incident arose from researcher testing, with authorization disputed by the parties; it is recorded separately from criminal theft. Testing whether an inflated balance can support borrowing extends the deposit-flaw scenario beyond the disclosed incident.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX017 — Gate.io / ETC 2019 | ETC reorganization/double spend removed deposits that had been credited | Unknown actor. Returned funds are not the total attack amount; exchange-server intrusion is not implied. | [GATEETC](https://www.gate.com/ru/announcements/article/16740) |
| EX032 — OKEx / ETC 2020 | ETC majority-hashrate attack/reorganization invalidated deposits after confirmation and payout | Unknown actor. Settlement-finality risk, not a hot-wallet key leak. | [ETC20](https://etccooperative.org/ETC-Coop-Board-Package-August-2020.pdf) |
| EX072 — Kraken 2024 | Crediting implementation created balances without completed deposits | CertiK Skyfall research team; exploitation scope disputed. Technical mechanism and authorization dispute are separate; no Lazarus attribution. | [KRAKEN](https://blog.kraken.com/product/security/kraken-bug-bounty-program-patches-isolated-bug) · [CERTIK24](https://www.certik.com/blog/certik-statement-on-kraken-vulnerability) |

## P6. Deceived customers authorize operations

**Sequence:** misuse brand or customer information → fabricate trusted identity → customer accepts a false explanation → customer transfers funds or grants authority.

**Failed control:** the customer believes a false claim about the recipient or purpose and authorizes the operation. Leaked customer details may make the deception more convincing.

**Evidence:** support queries/exports, recovery records, customer reports, and links between exposed customer groups and unusual asset activity.

**Validation:** use authorized exercises to test support-data access/export restrictions and coordinated checks of account recovery, sessions, and fund activity for customers whose data was exposed.

**Scope:** In P3, the attacker takes over the account and operates it directly. In P6, the deceived customer transfers funds or grants authority. Loss records should identify where the assets were held and who initiated the operation.

| Case | Disclosed access and failure | Attribution and limits | Sources |
| --- | --- | --- | --- |
| EX083 — Coinbase support-personnel incident 2025 | Some outsourced support workers were bribed; customer information enabled social-engineering fraud | Unknown actor. Data access did not itself provide direct withdrawal authority, but supported later fraud. | [COINBASE](https://www.coinbase.com/en-nl/blog/protecting-our-customers-standing-up-to-extortionists) · [COINBASESEC](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm) |

## External mechanism comparisons

- **M01 — Mango Markets 2022 → P4.** The attacker used their own accounts to manipulate prices in a thin market and borrow against inflated unrealized gains. Stolen API credentials were not a prerequisite. This DEX example is excluded from exchange-event and loss counts.
- **M02 — Parity 2017 → P3.** An initialization-permission flaw allowed owners and thresholds to be rewritten, enabling spending without the original keys. This external contract-wallet example is excluded from exchange-event and loss counts.

Case IDs link to the [registry](../../data/case-registry.csv), which lists source identifiers and URLs. The [source index](../../data/sources.json) retains the referenced URLs. Use the [defense matrix](defense-matrix.md) to assign implementation, review, and acceptance responsibilities.

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
