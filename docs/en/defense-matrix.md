# Exchange Defense Lessons from Loss Incidents

**English** | [简体中文](../zh-CN/defense-matrix.md)

This matrix derives defense and acceptance requirements primarily from publicly disclosed exchange losses over the past decade, following how attackers obtained authority, bypassed controls, and moved assets. Successful interventions and related technical cases add validation scenarios. Six attack paths map to 18 defense requirements, with business and security responsibilities, handoffs, and evidence. Items follow business risks and controlled objects. Application security, GRC, and red teams participate as specialist functions; code auditing is an application-security activity. See the [case registry](../../data/case-registry.csv) and [attack-path analysis](attack-paths.md).

## 1. Attack paths and gaps to examine

| Path and historical basis | Attacker capability | Common check | Remaining exposure | Items |
| --- | --- | --- | --- | --- |
| P1 Signing material: Coincheck, BitMart, Zilliqa | Sufficient material to sign, or an implementation defect enabling key recovery | Authorization and logs for local signing calls | Backups, recovery, and historical signatures; continued external signing | D04, D06, D11, D15 |
| P2 Transaction tampering: Bybit, Kiln; possible DMM chain | Modify construction, display, or request content | Signature validity and number of approvals | Approved bytes differ from the original request; approvers share a corrupted display | D07, D12, D16 |
| P3 Account and withdrawal authority: Coinbase recovery, WOO X; external Parity comparison | Rewrite identity, forge internal instructions, or bypass contract permissions | Current authentication and authorization | Recovery, backend writes, and initialization change who can transfer | D02, D05, D06, D08, D10, D12 |
| P4 Trading and valuation: Binance VIA; external Mango comparison | Abuse stolen trading access or manipulate a thin market using own accounts | API order permissions and ledger movements | Harmful trades transfer customer value; inflated values expand borrowing | D10, D13, D14 |
| P5 Crediting and double spending: Kraken, ETC | Create available balances through a flaw or reorganization | Internal ledger consistency and withdrawal authority | An incomplete or revoked deposit has funded conversion, loans, or withdrawals | D09, D10, D13 |
| P6 Customer deception: Coinbase support-personnel incident | Use customer details to impersonate a trusted party and induce action | Customer login and confirmation | Customer misunderstands recipient or purpose; support access continues leaking information | D08, D14, D16 |
| Recovery and retirement: ShapeShift, CoinDCX, Zilliqa | Reach new credentials through an old entry, reuse old authority, or take new funds at an old address | Availability and known-vulnerability fixes | Old sessions, public signatures, recovery environments, and subsequent inflows remain exploitable | D11, D15, D17 |

Coinbase's 2023 MFA blocked direct login; subsequent social engineering still required a human response. Binance VIA external withdrawals were blocked, but some victim trades were irreversible. Record separately whether intrusion continued, assets left, and customer value had already been harmed.

## 2. Fund operations and responsibility

Record the following for each fund path. Cover only products actually offered; mark unused staking or lending functions not applicable.

| Object | Minimum record | Completeness check |
| --- | --- | --- |
| Assets and customer entitlements | Asset, chain, wallet/custodian, source of balance, unlock or redemption conditions | Reconcile addresses and chain assets with internal accounting and external custody; list unresolved differences |
| Operations and states | Deposits, trading, withdrawals, replenishment, authority changes; maintenance, recovery, retirement | Include routine and exception paths; retain request-to-chain-result mappings |
| Human and service identities | Person, role, device, session, service account, token purpose and owner | Identify who operates, changes validation evidence, or restores/reissues authority |
| Controls and dependencies | Independent limits, supplier inputs, logs, revocation methods, recovery conditions | Record controls changeable by one identity, unavailable logs, and authority that cannot be revoked immediately |
| Impact and ownership | Direct assets, transferable reserves, later inflows; business owner, control maintainer, incident executor | Deduplicate assets and state the horizon and assumptions; untested limits cannot establish a maximum loss |

Business and technical teams implement and operate their controls. The security team analyzes risk, defines requirements, and organizes validation. The table below names collaborating parties and roles; specialist security functions follow in 2.1. Roles may be combined, but each task needs an owner and backup. Separately authorize fund actions, policy changes, and effectiveness review; test whether one person or service identity can bypass those arrangements.

| Party or role | Accountable outcome | Handoff |
| --- | --- | --- |
| Management and business owners | Fund-use requirements, resources, authority to limit services, treatment of unresolved risks | Approve restriction and recovery scope; assess liquidity, positions, and customer impact |
| Security team, coordinated by the CSO or designated lead | Risk analysis, design review, detection/response, independent technical validation, unresolved-risk tracking | Assign specialties by risk; agree control, remediation, and acceptance owners with system teams; report residual risk |
| Product, account, and ledger engineering | Recovery, business authorization, crediting, and entitlement rules | Submit designs, code changes, and exceptions for review; share request IDs and state transitions with risk, wallets, and security operations |
| Withdrawal risk and orchestration | Risk defines restrictions; orchestration maps orders, signing requests, batches, and chain results | Carry restrictions through batching, splitting, and retries; aggregate results per order; customer identification remains outside the signing service |
| Wallet team | Signing, parsing, broadcast, on-chain permission checks | Receive approval evidence; report transaction state, residual signatures, and on-chain authority; execute authorized migration |
| Treasury | Balances, replenishment, transfers, and externally held assets | Supply liquidity requirements and available-fund data; reconcile in-flight assets; enforce replenishment limits |
| Trading and credit risk | Abnormal trades, pricing, borrowing capacity, concentration, liquidation | Share account relationships and fund uses with accounting and security; constrain cash-out across products |
| IT, identity platform, SRE | Endpoints, sessions, cloud permissions, deployment, runtime, recovery infrastructure | Return actual revocation and isolation results; disabling a personal account does not establish that derived credentials expired |
| Incident command | Cross-team response, escalation, and temporary restrictions within delegated authority | Resolve timeouts, partial failures, and business conflicts; send restoration approval to the designated business authority and retain the rationale |
| HR and system owners | Role changes, departures, maintenance handover | Give IT and identity teams revocation targets; technical executors report session and related-credential outcomes |
| Customer support and anti-fraud | Customer reports, identity checks, suspicious fund behavior | Supply query records and affected accounts to security operations; separately authorize account recovery and lifting fund restrictions |
| Supplier management, procurement, legal | External access, notification, log support, exit arrangements | Reconcile actual permissions, response contacts, and revocation results with the service owner |

### 2.1 Specialist security functions

These are responsibilities, not a requirement for separate departments. One risk can involve several specialties. Code auditing within application security and attack simulation by a red team are activities. GRC means governance, risk, and compliance.

| Function | Main items | Work and acceptance responsibilities |
| --- | --- | --- |
| Security architecture | D01, D02, D06, D10–D12, D15, D18 | Analyze trust and common administrative access; define boundaries with engineering, wallets, and platforms; test whether one identity can alter requests, approval evidence, and validation records |
| Application security | D05, D07–D10, D12, D13, D16, D18 | Requirements/design review, threat modeling, code audits, dependency review, business-logic tests; bind fixes to versions and retain reproductions, post-fix outcomes, and searches for the same defect elsewhere |
| Infrastructure and identity security | D02–D07, D15–D18 | Review endpoints, network, cloud, and production access with IT, identity, and SRE; test sessions and derived authority remaining after isolation, revocation, or recovery |
| Wallet and contract security | D09–D12, D15, D16 | Review signing implementation, parsing, contract permissions, and key recovery with wallet, chain-integration, and treasury teams; validate control using actual bytes, execution results, and on-chain permissions |
| Data security | D02, D04, D06, D08, D16–D18 | Review sensitive access, export, logging, and supplier use; test bulk and persistent low-volume queries, post-revocation access, and data leakage through agent tools |
| Security operations | D03–D06, D08, D13–D18 | Correlate technical/business signals, hunt, investigate, and respond; verify restricted targets and actual effect with executors; record missed detections, false positives, failed actions, and times |
| GRC | Risk, exceptions, and control checks across D01–D18 | Map applicable requirements to controls and owners; sample actual execution records, track unverified items and expiring exceptions, and review supplier commitments with procurement/legal; authorized business owners accept residual risk |
| Red team | Risk-selected combinations across D02–D18, with impact defined through D01 | Explore authorized cross-system paths, replay historical methods, and test prevention/response; retain initial permissions, exploitation sequence, business results, and coverage gaps; check whether fixes remain bypassable |

Application and wallet security divide work by component and risk: for example, withdrawal-service authorization versus signing and on-chain permissions. Shared paths receive joint validation. Red teams retain independent hypotheses and evidence channels. Independent audit of management and compliance practices belongs to the appropriate audit function, separately from red-team technical testing or GRC self-checks.

### 2.2 Design, development, and risk-exception handoffs

For new products, critical code, or permission changes, the system owner supplies flows, scope, and dependencies. Security architecture and relevant specialties establish risks and test requirements. Engineering implements remediation and supplies versions and test results. Application security checks implementation; high-risk cross-system paths receive red-team or other independent technical verification. Security operations maintains runtime detection and response, with logs and action interfaces supplied by system teams.

When a control cannot be completed on time, GRC records affected business, residual risk, temporary measures, owner, and deadline. An authorized business owner decides acceptance, restriction, or postponement. Approval preserves the original test outcome. Expiry or changing conditions trigger reassessment. Control checks sample real authorization, change, and response records alongside technical tests; policies, interviews, and certificates alone do not establish effectiveness.

### 2.3 Incident signals and departmental handoffs

Session theft, unauthorized production writes, or mismatched transaction contents trigger preauthorized actions against the relevant objects. Unresolved signals meeting predefined high-risk conditions can justify targeted restrictions while investigation proceeds. State scope, review deadline, and release authority. Unresolved expiry escalates instead of automatically releasing. Isolate confirmed compromised devices and sessions while completing business mapping.

Handoffs include incident/action IDs, evidence source, timestamp precision, targets, restriction version, deadline, and owner. Send credential identifiers, not secrets. Receipts distinguish acceptance, execution, and verified effect, with failures and unknowns. When effectiveness time is uncertain, record the interval from last successful operation to first verified rejection. Failures escalate immediately; timeouts go to the incident commander and backup. Work past the last preventable stage moves to residual-signature, on-chain-authority, and asset handling while later work remains restricted.

| Handoff | Signal and content | Action and receipt |
| --- | --- | --- |
| Security operations → identity/platform, risk | Confirmed compromise or predefined high-risk signal; identities, sessions, evidence, known services, mapping gaps | Isolate access and restrict business in parallel within authority; trace derived credentials and reissuance; review temporary limits by deadline and investigate unknown scope |
| Platform/engineering → risk, accounts, accounting | Actual writes, deployments, or residual access; targets, service identities, time range, unknowns | Separate reachable from confirmed affected objects; map customers/orders, adjust limits, escalate unclear scope |
| Risk → orchestration → wallet | Restricted orders, operation, version, scope; orchestration adds signing requests, batch/split relationships, chains/wallets | Stop affected signing, broadcasting, and retries. Hold a batch that cannot safely be split. Reconstructed transactions need renewed validation/authorization; assess external execution of already signed content |
| Wallet → orchestration → risk | Unsigned, signed/unbroadcast, broadcast/unconfirmed, chain-confirmed states; actual restriction version, evidence, residual capability | Map back to orders, identify partial failures, unknowns, and batch impact. Update confirmation with the chain. Queue deletion does not invalidate a signature. Immediately escalate failure, timeout, or external executability |
| Risk/support → security operations | Abnormal recovery, linked fund behavior, fraud report; accounts, orders, access records, times | Correlate backend writes, deployments, employee queries, and sessions; report intrusion findings. Anti-fraud action does not wait for actor attribution |
| Executors → business/incident command | Proposed recovery scope, execution evidence, security review, available funds, reconciliation differences; isolated areas and unresolved issues | Approve specific scope, limits, observation, and re-suspension signals; assign executor/backup. Unverified controls and unexplained differences cannot pass. Track asset recovery separately |

Executors validate instruction origin, authority, and version, preventing duplicate asset actions and stale instructions overriding new restrictions. Lifting a restriction requires separate approval. Verify actual target state and rejection using controlled requests; retain effective, failed, and unreachable instances and signed/broadcast tasks. When the control plane is compromised, use previously tested independent emergency access. Preserve evidence somewhere the affected identity cannot rewrite.

## 3. Defense requirements and acceptance evidence

Bind validation to environment, version, and business scope. Production, customer-asset, and supplier testing requires authorization, scale limits, and stop conditions. Mark test-environment-only results as not yet verified in production.

The lead implements each control; specialist functions perform the specified review and validation. GRC schedules risk-based control checks and exception tracking; red teams select authorized combinations. Neither must attend every routine change. Record implementation owner, reviewer, and result separately, with independent technical verification for high-risk controls. Risk acceptance does not turn failed or unverified controls into passed ones.

### 3.1 Business, people, and infrastructure

| Item | Work | Lead and collaboration | Acceptance evidence |
| --- | --- | --- | --- |
| D01 Fund-operation scope | Map assets, customer balances, states, and modification rights through transfers, maintenance, recovery, retirement | Business owner; treasury, accounting, wallets, security architecture, GRC | Sampled requests trace to accounting and asset outcomes; unresolved reconciliation, ownerless systems, and untested paths listed |
| D02 Human/service identities | Inventory rights to change accounts, deployments, fund rules, keys, and logs; define service purpose, expiry, owner | Identity owner; HR, IT, system owners, infrastructure/identity security | Trace selected privileged users through personal sessions and service identities; record unknown-purpose accounts and retention/revocation outcomes |
| D03 Exposure and vulnerabilities | Inventory external and management interfaces; prioritize exploitation, access conditions, fund impact | Infrastructure/identity security; IT, SRE, owners, application security, security operations | Retest from unauthorized networks/identities; separate fixes, temporary mitigation, and remaining entrances; exceptions have owners and expiry |
| D04 Workstations | Managed production-access devices; isolate untrusted code from production credentials, sessions, and connections | Endpoint/IT owner; engineering, identity, infrastructure/identity security, security operations | Benign probes test files, sessions, network, and credential sharing; independently retest issued cloud sessions and service tokens after endpoint isolation |
| D05 Employee authentication, recovery, sessions | Phishing-resistant authentication; review factor enrollment, helpdesk recovery, emergency accounts, temporary credentials | Identity platform; IT, SRE, infrastructure/identity security, application security, security operations | Test login, recovery, and existing sessions separately; record supplemental controls and actual effect for access surviving password change or account suspension |
| D06 Cloud, containers, production access | Restrict grants, service accounts, escalation, secret reads, database writes; review cross-account and recovery access | SRE/cloud owner; application/database teams, security architecture, infrastructure/identity security | From a selected developer identity, test escalation and lateral access; establish it cannot jointly change requests and validation or erase evidence; include common administrators after service separation |
| D07 Secure development, deployment, runtime | Integrate requirements/design; risk-based code audit, dependency and business-logic testing, related-defect search; constrain CI secrets/releases and verify provenance, approval, runtime content | Engineering lead; application security reviews design/code; platform/SRE implement deployment controls; infrastructure/identity security validates | Requirements link to design, version, and tests; retain pre-fix reproduction and post-fix rejection, dependencies, and gaps. Unauthorized branches cannot release. Test runtime tampering/targeted responses and whether detection/rejection precedes signing or transfer |

### 3.2 Customer, trading, and fund controls

| Item | Work | Lead and collaboration | Acceptance evidence |
| --- | --- | --- | --- |
| D08 Support and customer recovery | Task-scoped data access/export; separate recovery, factor reset, and withdrawal-unlock authority; correlate reports with employee queries | Customer-account product owner; support, application security, data security, anti-fraud | Review recovery/API authorization and query scope; test bulk and low-volume persistent access. One support identity cannot independently release fund restrictions. Link anomalous queries to customers; verify through preregistered channels |
| D09 Deposits and accounting | Validate asset identity, execution, receipt, confirmations/reorgs; handle duplicate events, concurrency, failure compensation | Ledger owner; chain integration, trading, application security, wallet/contract security | Code review and exceptional-state tests cover crediting, reversal, compensation. Incomplete, incorrect, or duplicate deposits create no extra entitlement. Trace reorg impact through trading, lending, and other-chain withdrawals; distinguish restrictions from losses |
| D10 Withdrawal authorization and risk limits | Verify identity, business basis, address, amount, policy; bind release to order, content, expiry, policy version; maintain mappings and shared-quota reservation/settlement/release | Withdrawal owner; accounts, risk, orchestration, wallets, security architecture, application security | Review authorization/quota implementation. Test forgery, replay, stale release, changed content, timeout, and concurrent quota use. Batches/splits/retries retain current limits. Local timeout does not release capacity for an unresolved signed transaction. Old approval cannot undo new restriction; record pre-block spending and false restrictions |
| D11 Key lifecycle | Generation, storage, use, backup, recovery, retirement; distinguish one material share from complete signing capability | Wallet-system owner; treasury, IT, wallet/contract security, independent technical reviewer | Test remaining thresholds in the actual architecture. For exposed complete capability, verify migration, future deposits to old addresses, and related-authority handling. Disabling only the local API is insufficient |
| D12 Transaction contents and on-chain authority | Verify request origin/business approval; parse final bytes and simulate asset/authority effects before signing; recheck release before broadcast and actual outcome afterward | Wallet owner; orchestration, business approvers, application security, wallet/contract security, independent reviewer | Review parsing, approval, and contract-permission code. Test targeted returns, initialization, permissions, state changes, delegation/upgrades, forged approvals, external submission, authority surviving failed execution, and token allowance after delegation removal. Retest chain-independent authorizations on applicable chains with nonce conditions |
| D13 Execution, valuation, collateral | Combine API behavior, related accounts, depth, prices, concentration, loans, liquidation; protect feeds/configuration and separate position/loan/withdrawal restrictions from existing-position handling | Trading/credit risk; matching, accounts, accounting, application security, security operations | Risk tests valuation/quota rules; application security tests implementation and change rights. Separately test stolen trading access and own-account manipulation, tracing counterparties, loans, withdrawals. Test stale/divergent prices, backend investigations triggered by fund anomalies, false positives, and business impact |

### 3.3 Operations, coordination, and continuing validation

| Item | Work | Lead and collaboration | Acceptance evidence |
| --- | --- | --- | --- |
| D14 Detection and containment | Correlate technical/business evidence; define high-risk signals, temporary restrictions, review/release authority, failure escalation, backups | Security operations; incident command, control owners, risk, treasury | Record send, receipt, execution, and verified-effect times. Test target mismatch, reordering, partial failure, false-success receipts, independent emergency access, expiry review, and re-restriction |
| D15 Recovery and old addresses | Review entrances, access, monitoring, signing, later inflows; explain reconciliation and funds; list nonrevocable/nonmigratable assets/authority | Affected business owner; incident command, SRE, identity, accounting, treasury, wallets, relevant security specialties; independent review | Retest old credentials, sessions, signatures, delegation, allowance. Treat leaked-key retirement and future deposits separately from delegation removal. Test isolation from unresolved areas, high-value/targeted cases, and renewed limits after anomalies or monitoring failure |
| D16 Suppliers and outsourcing | Review external inputs/write privileges; agree logs, notice, emergency revocation, exit/handover | Service owner; procurement/legal, GRC, supplier; relevant application, infrastructure, data, or wallet specialists | GRC checks commitments against actual access, notice, and log support. Technical teams test malicious output, timeout, post-revocation behavior, refusal, failover, interruption. Handle existing signatures/on-chain grants separately |
| D17 Join/move/leave and handover | Align role and personal/service-identity changes with maintenance; transfer path explanations, exceptions, exercise records without copying secrets | System owner; HR, IT, identity platform, infrastructure/identity security, GRC | Successor independently completes a defined response/validation task; retest former access and rotated credentials; production dependencies have owners. GRC samples exception and control-maintenance handover |
| D18 Security and business agents | Separate read, analysis, production execution; constrain tool objects, actions, cumulative impact outside the model | Agent-system owner; business, data, cloud; application security reviews tool/permission implementation; red team tests within authority | Benign injection, false evidence, and tool-failure tests cover overreach/misresponse. Agent cannot relax rules or approve itself. Record stopping, compensation, irreversible actions, and independent logs |

## 4. Joint validation scenarios

Record business scope, environment/version, initial permissions, expected stop point, actual outcome, and chronology from first detectable behavior through detection, effective restriction, eradication, and recovery. Include asset/ledger changes, gaps, executor, and reviewer. Mark unsupported timestamps unknown and state why.

Red teams or independent technical reviewers organize cross-system testing. Application, infrastructure, data, and wallet specialists analyze relevant components; business/technical owners supply actual state and fixes. Security operations checks signals, correct business mapping, and effective response. GRC tracks failures and uncovered areas. A failed exploitation attempt establishes only the result under its recorded conditions.

| Scenario | Items | What to test |
| --- | --- | --- |
| Compromised developer endpoint uses existing sessions to approach production | D02, D04–D07, D14 | Cloud sessions and derived service tokens after endpoint isolation; continued deployment or production database writes |
| Supplier returns a wallet-specific malicious transaction | D07, D12, D16 | Relevant wallet, amount, authority; final bytes against original request; separate pre-signing, pre-broadcast, post-execution checks |
| External authorization submission, failed execution, later delegation removal | D10–D12, D14, D15 | All signing entrances; successfully processed EIP-7702 delegation can survive execution failure; removing it leaves token allowances. Chain ID 0 authorization may work on other supporting chains subject to nonce/other conditions; test by chain |
| Support identity accesses data and starts recovery | D05, D08, D10, D14 | Separate employee/customer recovery; query access must not automatically unlock withdrawals |
| False deposit or valuation moves through spot, collateral, lending, another asset | D09, D10, D13 | Source and use of entitlement; restrictions extend beyond the original asset or wallet |
| Security or financial-risk anomaly starts the response | D08, D10, D13, D14 | Confirmed compromise and threshold-crossing uncertain signals; temporary limits, reviews, false-positive release, escalation; backend/deployment investigation from fund patterns |
| Risk service, price source, or node fails | D09, D10, D13, D14 | Timeouts, stale input, node disagreement; handling existing positions, appeals, queued work |
| Concurrent releases, changed transactions, batching/retries during suspension | D10, D12, D14 | Shared quota across instances/chains; no excess cumulative use or duplicate reservation; unresolved transactions retain exposure. Bidirectional order/signature traceability, current limits through batches/splits, no stale approval for new contents; query existing outcome before retry |
| Lost, reordered, mismatched, partially failed handoff | D10, D14, D15 | Stale instructions cannot supersede restrictions; duplicate instructions do not repeat asset actions; distinguish API success from actual rejection; escalate by deadline to on-call and backup |
| Reuse old access and addresses after response | D11, D14–D17 | Sessions, derived credentials, signed transactions, on-chain grants, recovery environment, future deposits; isolate unknown areas, verify recovery scope separately, re-restrict on monitoring loss |

Retain successful and failed results. Not-applicable means the business is unused or retired. Missing logs, authorization, or safe test conditions means unverified.

## 5. Implementation priorities and evaluation

Contain leaked credentials, active exploitation, and confirmed unauthorized access first. D01–D06 establish assets, identities, entrances, and production access, with D14 providing detection, restrictions, and handovers in parallel. Separate common control over fund requests and their validation rules. Where independent blocking exists, examine detection latency, remaining assets, and recovery gaps.

D07–D13 proceed in parallel according to offered products. Lower online balances require more transfers; parsing gaps constrain new products; customer recovery review creates delay; restricting positions, loans, or liquidation creates different exposure. Business owners and control maintainers agree scope/resources and retain before/after verification. Test recovery separately from deceived customer actions. For self-custodied funds outside the platform, record actions still available to the exchange.

D15–D18 cover recovery, suppliers, people, and automation. New chains, products, important permissions, or suppliers trigger path updates and retesting. Assign implementation and review separately; unresolved items retain deadlines and business decisions.

When the security team uses agents, specialties retain responsibility for work quality. Application security maintains design/code/fix tests; security operations maintains investigation and response tasks; GRC checks control evidence and exceptions; red teams explore bypasses. Investigation findings become engineering tasks, with fixed versions and retest results linked to the incident. Real-time execution handles events and schedules; experts challenge evidence and add context, and authorized people approve actions beyond delegation. Enforce tool access, cumulative effect, and preauthorized limits outside the model. Verify actual identity, ledger, and chain state. Keep cases, evidence, policy, skills, and evaluations under enterprise control.

Wallet, recovery, and orchestration changes rerun related attacks; record change-to-retest latency. Red teams separately explore unseen paths with independent assumptions and evidence. Agents sharing models, context, or rules do not automatically provide independent validation. Test altered security policy, long-term memory, evaluation data, and malicious tickets/code that induce overreach.

Before widening execution, replay historical cases and run shadow tasks, comparing false releases, false restrictions, human takeovers, and repeated failures. After enabling execution, keep detection, effective restriction, repair, and retest times. Ground answers in actual outcomes and expert review, with human sampling and takeover exercises. Correct skills, policies, and evaluations with owner/version/scope; retest after model changes. Urgent blocking continues under existing preauthorization. The [research article](research.md) explains the attack evidence.

| Evaluation | Record | Conditions |
| --- | --- | --- |
| Fund-path coverage | Verified / known applicable paths; uninventoried business and unknown dependencies separately | Versioned denominator; configured but untested controls are not verified |
| Identity/dependency coverage | Owners, purpose, permission-validation status for people, services, suppliers | Retain unknown-purpose, ownerless, unverified counts |
| Effectiveness | Not applicable, unverified, failed, verified; version, time, scope | Separate partial pass; recheck environmental/key-dependency changes |
| Secure development/remediation | High-risk review, code-audit scope, reproduced flaws, fixed versions, regressions | Count against applicable changes/risks; scanning, reporting, and fixing are distinct |
| Risk exceptions/review | Business, temporary measures, approver, expiry, latest review | Separate expired, changed-condition, unsupported exceptions; acceptance is not a passed control test |
| Detection/containment | TTD from established compromise; TTC from detection to verified specified restriction | Unknown initial compromise separately uses known behavior; retain incomplete response; distinguish containment/eradication |
| Recovery/residual exposure | Per-service restoration, old-access retest, later inflows, unresolved issues | Plans differ from actual recovery; reimbursement/replenishment is not technical recovery |
| Reachable assets | Deduplicated assets, later inflows, pre-block outcomes within stated horizon/assumptions | Count only verified limits; distinguish harmed entitlements, reachable assets, actual loss |

## References

- Secure development and remediation: [NIST SSDF](https://csrc.nist.gov/projects/ssdf).
- Roles and jobs: [NIST NICE](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/resources/occupations-jobs-and-work).
- Governance and risk: [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework).
- Historical mechanisms and response evidence: [attack paths](attack-paths.md), [research](research.md).
- Targeted employee contact: [FBI advisory](https://www.ic3.gov/PSA/2024/PSA240903).
- [NIST authentication](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/) and [session management](https://pages.nist.gov/800-63-4/sp800-63b/session/).
- Organizational checks and supplier evaluation: [DMM regulatory findings](https://lfb.mof.go.jp/kantou/kinyuu/pagekthp0270000030.html).
- [OWASP transaction authorization](https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html) and [business-logic security](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html).
- [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) and [ERC-20](https://eips.ethereum.org/EIPS/eip-20).

This is an implementation and validation reference, not evidence of a production acceptance test. Adopters determine roles, thresholds, and response authority for their own business.
