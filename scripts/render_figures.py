"""Render the English research figures from the public datasets and documented paths."""
from pathlib import Path
import csv
import json
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "en"
INK, MUTED, BLUE, RED = "#20333F", "#687985", "#376B88", "#BD554A"
LINE, PALE, ROSE = "#DCE4E9", "#F1F5F7", "#FAF0ED"
plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none"})
NAMES = ["loss-concentration", "largest-losses", "known-attack-intervals", "registry-by-year", "loss-distribution", "attack-paths", "defense-architecture", "incident-handoffs", "recovery", "signing-material", "transaction-tampering", "account-takeover", "trading-manipulation", "deposit-finality", "customer-deception", "actor-profiles", "shared-inputs", "intervention-outcomes"]


class Figure:
    def __init__(self, title, subtitle="", height=1000):
        self.height = height
        self.fig = plt.figure(figsize=(12, height / 150), dpi=150, facecolor="white")
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set(xlim=(0, 1800), ylim=(height, 0))
        self.ax.axis("off")
        self.labels = []
        self.text(80, 80, title, 20)
        self.text(80, 143, subtitle, 12, MUTED)

    def text(self, x, y, label, size=13, color=INK, center=False, width=None):
        if width:
            label = "\n".join(textwrap.fill(line, width, break_long_words=False) for line in label.split("\n"))
        obj = self.ax.text(x, y, label, fontsize=size, color=color,
                           ha="center" if center else "left", va="center", linespacing=1.4, parse_math=False)
        self.labels.append(obj)
        return obj

    def box(self, x, y, w, title, detail="", red=False, h=120):
        self.ax.add_patch(Rectangle((x, y), w, h, facecolor=ROSE if red else PALE, edgecolor="none"))
        self.ax.add_patch(Rectangle((x, y), 4, h, facecolor=RED if red else BLUE))
        chars = max(15, int(w / 13))
        self.text(x+w/2, y+(h*.35 if detail else h/2), title, 13, RED if red else INK, True, chars)
        if detail:
            self.text(x+w/2, y+h*.78, detail, 10.5, MUTED, True, int(w/10.8))

    def arrow(self, points, color=BLUE, dashed=False):
        if len(points)>2:
            self.ax.plot(*zip(*points[:-1]), color=color, lw=1.2, linestyle="--" if dashed else "-")
        self.ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>",
            mutation_scale=13, color=color, lw=1.2, linestyle="--" if dashed else "-"))

    def row(self, y, nodes, xs=None, w=365, h=120, arrows=True):
        xs = xs or [80, 505, 930, 1355]
        for x,node in zip(xs,nodes):
            title,detail,*tone=node
            self.box(x,y,w,title,detail, bool(tone and tone[0]),h)
        if arrows:
            for a,b in zip(xs,xs[1:]): self.arrow([(a+w,y+h/2),(b,y+h/2)])

    def save(self, number, note):
        self.ax.plot([80,1720],[self.height-100]*2,color=LINE,lw=.8)
        self.text(80,self.height-52,note,10,MUTED,width=145)
        self.fig.canvas.draw()
        renderer=self.fig.canvas.get_renderer()
        fw,fh=self.fig.canvas.get_width_height()
        for obj in self.labels:
            box=obj.get_window_extent(renderer)
            if box.x0<5 or box.y0<5 or box.x1>fw-5 or box.y1>fh-5:
                raise ValueError(f"Figure {number}: text outside canvas: {obj.get_text()}")
        for i,left in enumerate(self.labels):
            a=left.get_window_extent(renderer)
            for right in self.labels[i+1:]:
                b=right.get_window_extent(renderer)
                if min(a.x1,b.x1)-max(a.x0,b.x0)>3 and min(a.y1,b.y1)-max(a.y0,b.y0)>3:
                    raise ValueError(f"Figure {number}: overlapping text: {left.get_text()} / {right.get_text()}")
        name=f"{number:02}-{NAMES[number-1]}"
        self.fig.savefig(OUT/(name+".png"),dpi=150,facecolor="white")
        self.fig.savefig(OUT/(name+".svg"),facecolor="white")
        svg = OUT/(name+".svg")
        svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines())+"\n")
        plt.close(self.fig)


def numeric_figures(losses, cases, stats):
    f=Figure("Concentration of reported losses", "Each subset is reranked; the source registry retains every case")
    for y,(label,key) in zip([330,520,710],[("Full sample","all"),("Without Binance 2026","without_binance_2026"),("Also without Bybit 2025","without_binance_2026_and_bybit")]):
        s=stats[key]
        f.text(80,y-22,label,14)
        f.text(80,y+25,f"{s['n']} events / ${s['total_usd_million']:,.2f}m",11,MUTED)
        f.ax.plot([700,1650],[y,y],color=LINE,lw=2)
        x=700+950*s["top5_share"]
        f.ax.plot(x,y,"o",color=RED,ms=9)
        f.text(x+22,y,f"{s['top5_share']:.1%}",13,RED)
    f.text(700,240,"Top five share of each subset's losses",13,BLUE)
    f.save(1,"Source: loss-sample.csv. Sensitivity analysis does not remove disclosure bias or establish industry-wide losses.")

    f=Figure("Eight largest reported losses", "Nominal estimates at the time of each incident / USD million")
    top=sorted(losses,key=lambda c:float(c["usd_million"]),reverse=True)[:8]
    for i,c in enumerate(top):
        y=260+i*72; v=float(c["usd_million"])
        f.text(80,y,f"{c['target']} {c['date'][:4]}",12)
        f.ax.add_patch(Rectangle((590,y-15),980*v/6500,30,facecolor=RED if i==0 else BLUE))
        f.text(1600,y,f"{v:,.2f}",12)
    f.save(2,"Source: loss-sample.csv. Freezing, recovery and reimbursement are not deducted. BitMart uses its retrospective estimate.")

    f=Figure("Known intervals in three attacks", "Calendar days between disclosed events; start and end events differ")
    rows=[("Bybit / Safe","Earliest known activity to asset theft",17),("WOO X","Backdoor installation to loss date",16),("Kiln","Signing the authority change to discovery",8)]
    for i,(name,desc,days) in enumerate(rows):
        y=330+i*180
        f.text(80,y-30,name,16);f.text(80,y+46,desc,11,MUTED,width=39)
        end=720+days/20*870
        f.ax.plot([720,end],[y,y],color=BLUE,lw=3)
        f.ax.plot([720,end],[y,y],"o",color=BLUE)
        f.text(end+25,y,f"{days} days",13,BLUE)
    f.save(3,"Sources: Sygnia, WOO X and Kiln. These intervals do not establish total dwell time, available response time, or MTTR.")

    f=Figure("Annual coverage of the incident registry", "98 incidents and leads, including blocked attacks and disputed events")
    ax=f.fig.add_axes([.08,.22,.86,.52])
    years=list(range(2016,2027))
    related=[sum(c["date"].startswith(str(y)) and c["scope"]=="related_service" for c in cases) for y in years]
    main=[sum(c["date"].startswith(str(y)) and c["scope"]!="related_service" for c in cases) for y in years]
    ax.bar(years,main,color=BLUE,label="Exchange / customer")
    ax.bar(years,related,bottom=main,color="#ADC0CD",label="Related service")
    ax.set_xticks(years);ax.set_xticklabels([str(y)+("*" if y==2026 else "") for y in years]);ax.set_ylabel("Registry entries")
    ax.spines[["top","right"]].set_visible(False);ax.legend(frameon=False,loc="upper left")
    f.save(4,"Source: case-registry.csv. Counts describe research coverage, not incident rates. *2026 through November 1.")

    f=Figure("Incident counts and losses by amount band", "41 incidents with loss estimates; separate axes for counts and dollar values")
    vals=[float(c["usd_million"]) for c in losses]
    groups=[("At least $100m",lambda v:v>=100),("$10m to below $100m",lambda v:10<=v<100),("Below $10m",lambda v:v<10)]
    f.text(550,240,"Incidents",13,BLUE);f.text(1150,240,"Losses / USD million",13,BLUE)
    for i,(label,pred) in enumerate(groups):
        y=350+i*170;selected=[v for v in vals if pred(v)];total=sum(selected)
        f.text(80,y,label,13)
        f.ax.add_patch(Rectangle((550,y-20),430*len(selected)/30,40,facecolor=BLUE))
        f.text(550+430*len(selected)/30+18,y,str(len(selected)),13)
        f.ax.add_patch(Rectangle((1150,y-20),430*total/12000,40,facecolor=RED))
        f.text(1150+430*total/12000+18,y,f"{total:,.2f}",12)
    f.save(5,"Source: loss-sample.csv. Public-source selection does not represent the industry's full loss distribution.")


def diagrams():
    f=Figure("Six principal attack paths", "Paths can combine within one incident; actor attribution is recorded separately",1100)
    paths=[("P1 Signing material",["Expose material","Gain signing capability","Sign externally","Transfer assets"]),
           ("P2 Transaction",["Tamper with builder","Replace operation","Obtain approval","Execute altered action"]),
           ("P3 Account authority",["Recovery / backend","Change identity","Withdrawal accepted","Platform pays out"]),
           ("P4 Trading / value",["Trading access","Manipulate trades","Transfer / inflate value","Withdraw / borrow"]),
           ("P5 Crediting",["Flaw / double spend","Available balance","Convert / withdraw","Asset shortfall"]),
           ("P6 Customer fraud",["Impersonate","False explanation","Customer authorizes","Fraudulent recipient"])]
    for i,(name,steps) in enumerate(paths):
        y=240+i*120;f.text(80,y+40,name,12,BLUE,width=22)
        f.row(y,[(s,"",True) for s in steps],xs=[430,760,1090,1420],w=295,h=83)
    f.save(6,"Source: attack-path analysis. Reorganizations can invalidate deposits after payout. Stages do not indicate duration or frequency.")

    f=Figure("Controls across custody, trading, and withdrawals", "Verify each operation where it changes assets or customer balances")
    f.box(80,220,1640,"Independent approval evidence, risk decisions, and restriction versions",h=70)
    nodes=[("Settlement / credit","Asset received; reorgs"),("Trading / lending","Depth; valuation"),("Withdrawal authority","Recovery; anti-fraud"),("Transaction contents","Request; signed bytes"),("Signing / broadcast","Keys; authority changes")]
    f.row(380,nodes,xs=[80,415,750,1085,1420],w=300,h=140)
    f.box(80,660,460,"Leaked key / malicious grant","External execution may remain",True)
    f.arrow([(550,720),(1370,720)],RED)
    f.text(960,670,"Outside the exchange's application path",12,RED,True)
    f.box(1380,660,340,"On-chain assets","Revoke or migrate where possible")
    f.save(7,"Foundation: endpoint, identity, cloud, deployment and audit controls. Existing signatures and external authority require separate handling.")

    f=Figure("Production-access incident handoffs", "Preauthorized targeted restrictions; access isolation and business limits proceed in parallel",1300)
    xs=[140,440,740,1040,1340,1640]
    for x,label in zip(xs,["Security\noperations","Identity / platform\nengineering","Business\nrisk","Withdrawal\norchestration","Wallet","Incident\ncommand"]):
        f.text(x,230,label,12,center=True);f.ax.plot([x,x],[280,1090],color=LINE,ls="--",lw=1)
    messages=[(140,440,350,"Identity / session:\nisolate and revoke",False),(140,740,455,"Accessible services + evidence:\napply temporary limits",False),(440,740,565,"Actual writes / unknown scope:\nmap customers and requests",False),(740,1040,650,"Request + restriction version",False),(1040,1340,750,"Signing request / batch:\nhold signing and broadcast",False),(1340,1040,850,"Transaction stage + evidence:\nfailures and residual capability",True),(1040,740,950,"Aggregate results per request",True),(740,140,1045,"Fund anomalies can trigger intrusion investigation",True)]
    for a,b,y,label,reply in messages:
        f.arrow([(a,y),(b,y)],dashed=reply)
        obj=f.text((a+b)/2,y-35,label,10.5,BLUE,True)
        obj.set_bbox({"facecolor":"white","edgecolor":"none","pad":2})
    f.arrow([(140,1120),(1640,1120)],RED)
    f.text(850,1085,"Escalate failures, timeouts, and any remaining ability to execute transactions externally",10.5,RED,True)
    f.save(8,"Record receipt, execution and verified effect separately. Recovery requires evidence, security review, reconciliation and authorized approval.")

    f=Figure("Containment and staged recovery", "Keep unresolved areas isolated; assess residual signing and on-chain authority",1120)
    f.box(80,215,1640,"Parallel: business limits, identity isolation, evidence preservation, on-chain checks",h=70)
    f.box(80,420,320,"In-flight operations","Signatures, balances, authority")
    f.arrow([(400,480),(515,480)])
    f.box(525,420,330,"External execution?","Assess actual remaining capability")
    for y,title,detail,tone in [(320,"Yes","Check revocation / migration",True),(525,"No","Verify local limits",False),(730,"Unknown","Keep restrictions; investigate",False)]:
        f.box(970,y,340,title,detail,tone)
        f.arrow([(855,480),(910,480),(910,y+60),(970,y+60)],RED if tone else BLUE)
    f.box(1400,440,320,"Recovery review","Access; monitoring;\nasset reconciliation",h=150)
    f.arrow([(1310,380),(1355,380),(1355,480),(1400,480)])
    f.arrow([(1310,585),(1355,585),(1355,530),(1400,530)])
    f.box(1400,740,320,"Approved staged recovery","Scope, limits, observation")
    f.arrow([(1560,590),(1560,740)])
    f.text(80,930,"Keep restrictions where controls remain unverified; reapply them after renewed anomalies or loss of monitoring.",12,MUTED)
    f.save(9,"Recovery reference. Delegation, token allowance and private-key exposure are separate. Broadcast transactions are not guaranteed reversible.")

    f=Figure("P1  Signing-material compromise", "Sufficient material lets an attacker create valid signatures in an external environment")
    f.text(80,230,"ATTACK PATH",12,RED)
    f.row(300,[("Key exposure","Storage or implementation",True),("Signing capability","Enough material",True),("External signing","Attacker's environment",True),("On-chain transfer","Valid signature",True)])
    f.text(80,560,"EXCHANGE'S NORMAL WITHDRAWAL PATH",12,BLUE)
    f.row(620,[("Business approval","Policy and limits"),("Signing service","Exchange controls"),("Broadcast","Platform submission")],xs=[80,505,930])
    f.arrow([(1295,680),(1540,680),(1540,420)])
    f.save(10,"Coincheck and BitMart. The external signing path bypasses the exchange's application approvals, limits and local signing interface.")

    f=Figure("P2  Transaction tampering", "Bybit: supplier frontend compromise influenced a cold-wallet transaction")
    f.row(280,[("Developer endpoint","Safe's environment",True),("Cloud / frontend","Modified resources",True),("Tampered display","Selected wallet",True),("Malicious transaction","Different operation",True)])
    f.row(610,[("Business transfer","Original request"),("Signers approve","Shared display",True),("Execution logic changes","Malicious transaction",True),("Assets transferred","No further multisig approval",True)])
    f.arrow([(1112,400),(1112,505),(687,505),(687,610)],RED,dashed=True)
    f.text(900,475,"Shared approval input",11,RED,True)
    f.save(11,"Source: Sygnia. Dashed link identifies the compromised information used by signers; it is not a second independent check.")

    f=Figure("P3  Account and withdrawal takeover", "Different entry routes can lead the platform to accept an attacker-controlled identity")
    f.text(80,220,"WOO X 2025",13,BLUE)
    f.row(280,[("Developer endpoint","Existing VPN session",True),("Cloud / containers","Backend credentials",True),("Rewrite account","Email, password, MFA",True)],xs=[80,505,930])
    f.text(80,540,"COINBASE 2021",13,BLUE)
    f.row(600,[("Customer credentials","Email access and phone",True),("SMS recovery flaw","Recovery path abused",True),("Authentication token","Account control",True)],xs=[80,505,930])
    f.box(1370,450,350,"Platform withdrawal","Accepted identity; valid signing",True)
    f.arrow([(1295,340),(1330,340),(1330,510),(1370,510)],RED)
    f.arrow([(1295,660),(1330,660),(1330,510),(1370,510)],RED)
    f.save(12,"Sources: WOO X postmortem and Coinbase customer notice. Recovery and backend-write branches need separate tests.")

    f=Figure("P4  Trading and valuation manipulation", "Customer funds can be lost before a withdrawal leaves the exchange",1200)
    f.text(80,230,"BINANCE VIA 2018",13,BLUE)
    f.box(80,290,350,"Victim API keys","Market buy orders",True)
    f.box(80,470,350,"31 prepared accounts","Sell at elevated prices",True)
    f.box(560,380,350,"Harmful trades","Customer value transferred",True)
    f.arrow([(430,350),(495,350),(495,440),(560,440)],RED)
    f.arrow([(430,530),(495,530),(495,440),(560,440)],RED)
    f.box(1050,290,670,"Automatic withdrawal suspension","External payout blocked")
    f.box(1050,470,670,"Some victim trades cannot be reversed","Uninvolved counterparties; damage remains",True)
    f.arrow([(910,440),(980,440),(980,350),(1050,350)])
    f.arrow([(910,440),(980,440),(980,530),(1050,530)],RED)
    f.text(80,735,"MANGO MARKETS 2022 — EXTERNAL DEX COMPARISON",13,BLUE)
    f.row(810,[("Attacker-owned accounts","No stolen API keys needed",True),("Thin-market price","Manipulated input",True),("Inflated collateral","Larger borrowing capacity",True),("Real assets borrowed","Asset shortfall",True)])
    f.save(13,"Sources: Binance and Chainalysis. VIA's blocked withdrawals did not reverse all harmful trades. Mango is outside the CEX loss sample.")

    f=Figure("P5  Erroneous crediting and double spending", "A reorganization may remove the deposit only after the exchange has paid out")
    f.row(300,[("Deposit on-chain","Original history"),("Available balance","Credited by exchange",True),("Convert / withdraw","Real assets paid out",True),("Later reorganization","Original deposit removed",True)])
    f.box(80,630,740,"Kraken: a flaw in deposit crediting","Incomplete deposits created spendable balances",True)
    f.box(980,630,740,"Shared consequence","Payout lacks valid deposit backing",True)
    f.arrow([(820,690),(980,690)],RED)
    f.arrow([(1537,420),(1537,630)],RED)
    f.save(14,"Sources: ETC Cooperative and Kraken. Arrows show sequence, not elapsed time. Kraken's research authorization was disputed.")

    f=Figure("P6  Deceiving customers into transfers", "Coinbase 2025: stolen customer information helped attackers impersonate support staff")
    f.row(280,[("Bribe support staff","Obtain customer data",True),("Real account details","Credible impersonation",True),("False support identity","False purpose or recipient",True),("Customer deceived","Fraudulent explanation",True)])
    f.row(610,[("Customer authenticates","Own credentials"),("Customer confirms","Fraudulent request",True),("Fraudulent recipient","Customer loses funds",True)],xs=[505,930,1355])
    f.arrow([(1537,400),(1537,500),(1112,500),(1112,610)],RED)
    f.save(15,"Source: Coinbase 2025 disclosure. The attackers did not obtain customer passwords or private keys.")

    f=Figure("Attacker profiles", "Disclosed access, selection and outcomes; attribution strength is stated in the article",1200)
    profiles=[("TraderTraitor","Bybit / FBI","Supplier endpoint; cloud; frontend","Specific cold wallet","Tampered transaction approved; wallet control changed"),
              ("UNC1069","Mandiant research","Telegram identity; fake meeting; audio-fix lure","Crypto staff, developers, investment firms","Credentials and sessions; loss unknown"),
              ("Unknown actor","Kiln supplier report","GitHub / CI credentials; running API modification","Withdrawal authority with >150,000 SOL staked","Customer approved authority change; loss"),
              ("Unknown actor","Coinbase disclosure","Bribed support personnel; customer information","Exposed customers; other filters unknown","Customer-authorized fraudulent transfers"),
              ("Predatory Sparrow","Nobitex / actor claim","Initial entry unknown; asset transfer capability","Nobitex; internal selection unknown","Burn-address transfers; destructive motive assessed")]
    for x,label in zip([80,450,900,1350],["Actor / case","Access and control","Target selection","Known outcome"]):f.text(x,225,label,12,BLUE)
    for i,(actor,case,access,target,outcome) in enumerate(profiles):
        y=290+i*150
        f.ax.add_patch(Rectangle((80,y-15),1640,135,facecolor=PALE if i%2==0 else "white"))
        f.text(95,y+25,actor,12);f.text(95,y+77,case,10,MUTED,width=28)
        for x,label,width in [(450,access,29),(900,target,29),(1350,outcome,25)]:f.text(x,y+47,label,11,RED if x==1350 else INK,width=width)
    f.save(16,"Sources: FBI, Sygnia, Mandiant, Kiln, Coinbase and Chainalysis. UNC1069 is not an additional event in the loss sample.")

    f=Figure("After transaction, identity, or balance records change", "Case comparison: the downstream operation can still be approved",1120)
    rows=[("Bybit 2025",("Transaction / display","Tampered frontend"),("Multiple approvals","Altered transaction signed"),("Execution logic changes","Later transfers")),
          ("Kiln 2025",("API transaction","Authority-change instruction"),("Custody signing","Required signatures obtained"),("Authority changes","Subsequent loss")),
          ("WOO X 2025",("Identity records","Email, password, MFA"),("Account takeover","Withdrawal request"),("Platform pays out","9 accounts affected")),
          ("Kraken 2024",("Available balance","Deposit incomplete"),("Withdrawal allowed","Crediting flaw"),("Real assets leave","Research dispute"))]
    for i,(case,*nodes) in enumerate(rows):
        y=250+i*180;f.text(80,y+60,case,13)
        f.row(y,[(a,b,True) for a,b in nodes],xs=[410,865,1320],w=400)
    f.save(17,"Sources: incident disclosures. Compare the final operation with original approval, identity changes, and actual settlement.")

    f=Figure("Intervention stage and financial outcome", "Disclosed process on the left; outcome and residual impact on the right",1120)
    rows=[("Coinbase","2019 / 2023",("Employee / endpoint attack","Exploit or social engineering",True),("Detected and interrupted","Endpoint action / staff contact",False),("No customer-fund loss","Reported in both cases",False)),
          ("Binance VIA","2018",("Abusive trades occur","Customer value affected",True),("Withdrawals suspended","External payout blocked",False),("Some trades irreversible","Uninvolved counterparties",True)),
          ("Binance / WOO / Kraken","2019 / 2025 / 2024",("Funds have left","Before disclosed intervention",True),("Alert / issue detected","Different discovery methods",False),("Suspension / mitigation","Earlier payout not prevented",False)),
          ("Bybit / Kiln","2025",("Malicious transaction approved","Signers approved the request",True),("On-chain control changes","Logic or withdrawal authority",True),("Assets transferred","Authority remains in effect",True))]
    for i,(case,year,a,b,c) in enumerate(rows):
        y=250+i*185;f.text(80,y+35,case,11,width=22);f.text(80,y+92,year,10,MUTED)
        f.row(y,[a,b],xs=[465,900],w=385)
        f.ax.plot([1305,1305],[y,y+120],color=LINE)
        f.row(y,[c],xs=[1335],w=385,arrows=False)
    f.save(18,"Sources: platform postmortems and Sygnia. Outcomes are not an extra timeline step. Kraken involves disputed research authorization.")


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    with (ROOT/"data/loss-sample.csv").open() as f:losses=list(csv.DictReader(f))
    with (ROOT/"data/case-registry.csv").open() as f:cases=list(csv.DictReader(f))
    stats=json.loads((ROOT/"data/statistics.json").read_text())
    numeric_figures(losses,cases,stats)
    diagrams()
    print("Rendered 18 English figures as PNG and SVG.")


if __name__=="__main__":
    main()
