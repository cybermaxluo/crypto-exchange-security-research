# Crypto Exchange Security Research

**English** | [简体中文](README.zh-CN.md)

An investigation of exchange attacks from 2016 to November 1, 2026: how attackers reach funds, why controls fail, and how exchanges can test their defenses.

The research follows six routes to financial harm: signing-material compromise, transaction tampering, account takeover, trading and valuation manipulation, erroneous crediting and double spending, and customer deception. It connects technical failure to wallet operations, accounting, risk controls, engineering, and security responsibilities.

## Read the research

| Document | What it provides | Languages |
| --- | --- | --- |
| From Bybit to Binance: How Attackers Breach Crypto Exchanges | Five-part investigation, cross-case comparisons, actor attribution, response analysis, defense priorities, and 15 illustrations | [English](docs/en/research.md) · [中文](docs/zh-CN/research.md) |
| Exchange Defense Lessons from Loss Incidents | Eighteen defense requirements, specialist responsibilities, departmental handoffs, and acceptance evidence | [English](docs/en/defense-matrix.md) · [中文](docs/zh-CN/defense-matrix.md) |
| Six Attack Paths Against Crypto Exchanges | Attack mechanisms, case-level evidence, investigation records, and validation scenarios | [English](docs/en/attack-paths.md) · [中文](docs/zh-CN/attack-paths.md) |
| Exchange Security Case Catalogue | All 98 records, with losses, attack sequences, attribution, evidence limits, and source links | [English](docs/en/case-catalogue.md) · [中文](docs/zh-CN/case-catalogue.md) |
| Methodology and data | Sample boundaries, monetary estimates, response metrics, data schema, and reproducibility | [English](docs/en/methodology.md) · [中文](docs/zh-CN/methodology.md) |

Start with the investigation for the findings, then use the defense matrix to examine your own operations. The attack-path reference supplies technical detail for application security, security operations, wallet security, and red-team work.

## Dataset

| Material | Scope |
| --- | --- |
| [Case registry](data/case-registry.csv) | 98 public incidents and leads; includes 38 index-only records |
| [Monetary sample](data/loss-sample.csv) | 41 incidents included in the loss calculation; total $11,582.86 million |
| [Statistics](data/statistics.json) | Sample distribution, annual counts, and sensitivity calculations |
| [Source index](data/sources.json) | 113 source URLs used in the underlying research |

The article compares 15 cases and examines attribution and response in 12. Seven disclosed time observations are retained separately; their endpoints do not support a combined MTTR. Monetary values are incident-time nominal estimates, not audited net losses. See the methodology before reusing the data.

The registry is a public-source research sample, not a census of all attacks or a claim that every record has a complete forensic investigation. Defense requirements are recommendations for validation, not completed production assessments.

## Reproduce and check

Python 3.11 or later is sufficient for the document and data checks:

```bash
python3 scripts/check.py
```

English figures can be regenerated with Matplotlib:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/render_figures.py
```

Chinese illustrations retain the source article's figures. Both language editions use repository-relative links and locally stored images. No account credentials, internal-system records, drafting logs, or publishing state are included.

## Authors and corrections

- **Max Luo** — AI Security and Automation Lead, Crypto Exchange; [cybermaxluo](https://github.com/cybermaxluo).
- **Morgan Chen** — AI SOC Platform Lead, Crypto Exchange; [Extrader-home](https://github.com/Extrader-home).

To propose a correction, open an issue with the case ID, relevant passage, source URL, and the specific change supported by that source. Keep confirmed facts, investigative assessments, and proposed validation scenarios distinct. Third-party sources remain the work of their respective publishers.
