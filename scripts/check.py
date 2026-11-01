"""Check reader-facing documents, references, sample statistics, and bilingual coverage."""
from pathlib import Path
from decimal import Decimal
from statistics import median
from urllib.parse import unquote, urlsplit
import csv
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]


def rows(name):
    with (ROOT/"data"/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))


def summary(values):
    values=sorted(values,reverse=True)
    total=sum(values)
    return {"n":len(values),"total_usd_million":float(total),
            "median_usd_million":float(median(values)),
            "mean_usd_million":float(total/len(values)),
            "top1_share":float(values[0]/total),
            "top5_share":float(sum(values[:5])/total),
            "ge_100m_count":sum(v>=100 for v in values),
            "ge_100m_share":float(sum(v for v in values if v>=100)/total)}


def main():
    cases=rows("case-registry.csv"); losses=rows("loss-sample.csv")
    sources=json.loads((ROOT/"data/sources.json").read_text())
    stats=json.loads((ROOT/"data/statistics.json").read_text())
    byid={r["case_id"]:r for r in cases}
    assert len(byid)==len(cases)==98
    assert len(losses)==41 and len({r["case_id"] for r in losses})==41
    assert len(sources)==113
    assert sum(r["evidence"]=="C" for r in cases)==38
    assert sum(r["scope"]=="related_service" for r in cases)==8
    for r in cases:
        expected=[sources[k]["url"] for k in r["source_ids"].split(";")]
        assert r["source_urls"].split(";")==expected,r["case_id"]
    for r in losses:
        assert r["case_id"] in byid
        assert r["amount_source_url"]==sources[r["amount_source_id"]]["url"]
    amounts={r["case_id"]:Decimal(r["usd_million"]) for r in losses}
    alt={r["case_id"]:Decimal(r["usd_million"]) for r in rows("alternative-estimates.csv")}
    assert set(alt)<=set(amounts)
    groups={"all":amounts,
            "without_binance_2026":{k:v for k,v in amounts.items() if k!="EX095"},
            "without_binance_2026_and_bybit":{k:v for k,v in amounts.items() if k not in {"EX095","EX081"}},
            "alternative_estimates_scenario":amounts|alt,
            "bitmart_196m_scenario":amounts|{"EX042":Decimal("196")}}
    for label,data in groups.items():
        for key,value in summary(list(data.values())).items():
            assert math.isclose(value,stats[label][key],rel_tol=1e-10,abs_tol=1e-8),(label,key,value,stats[label][key])
    for annual in stats["annual"]:
        year=str(annual["year"])
        subset=[r for r in losses if r["date"].startswith(year)]
        assert sum(r["date"].startswith(year) for r in cases)==annual["registry_count"]
        assert len(subset)==annual["amount_count"]
        assert math.isclose(sum(float(r["usd_million"]) for r in subset),annual["usd_million"],abs_tol=1e-8)
    observations=rows("response-observations.csv")
    assert len(observations)==7 and len({r["case_id"] for r in observations})==5
    for r in observations:assert r["case_id"] in byid

    docs=["research.md","defense-matrix.md","attack-paths.md","case-catalogue.md","methodology.md"]
    for name in docs:
        en=ROOT/"docs/en"/name;zh=ROOT/"docs/zh-CN"/name
        assert en.exists() and zh.exists(),name
        assert "../zh-CN/"+name in en.read_text() and "../en/"+name in zh.read_text(),name
    for language in ["en","zh-CN"]:
        article=(ROOT/"docs"/language/"research.md").read_text()
        assert len(re.findall(r"^## ",article,re.M))==5,language
        assert len(re.findall(r"^### ",article,re.M))==27,language
        assert len(re.findall(r"!\[",article))==15,language
        matrix=(ROOT/"docs"/language/"defense-matrix.md").read_text()
        assert re.findall(r"^\| (D\d{2}) ",matrix,re.M)==[f"D{i:02}" for i in range(1,19)],language
        paths=(ROOT/"docs"/language/"attack-paths.md").read_text()
        assert len(re.findall(r"^## P[1-6]",paths,re.M))==6,language
        catalogue=(ROOT/"docs"/language/"case-catalogue.md").read_text()
        catalogue_ids=re.findall(r"^\| (EX\d{3})<br>",catalogue,re.M)
        assert len(catalogue_ids)==98 and set(catalogue_ids)==set(byid),language
        anchors=set(re.findall(r'<a id="([^"]+)"',catalogue))
        for anchor in re.findall(r"\]\(#([^)]+)\)",catalogue):
            assert anchor in anchors,(language,anchor)
        catalogue_urls=set(re.findall(r"https?://[^\s)]+",catalogue))
        assert catalogue_urls=={s["url"] for s in sources.values()},language
    en_urls=set(re.findall(r"https?://[^\s)]+",(ROOT/"docs/en/research.md").read_text()))
    zh_urls=set(re.findall(r"https?://[^\s)]+",(ROOT/"docs/zh-CN/research.md").read_text()))
    assert en_urls==zh_urls and len(en_urls)==49

    checked=0
    for p in ROOT.rglob("*.md"):
        text=p.read_text()
        assert not re.search(r"/Users/|file://|\.wechat-build|\.wechat-state",text),p
        for target in re.findall(r"\]\(([^)]+)\)",text):
            if urlsplit(target).scheme or target.startswith("#"):continue
            local=(p.parent/unquote(target.split("#",1)[0])).resolve()
            assert local.is_relative_to(ROOT) and local.is_file(),(p,target)
            checked+=1
    for language in ["en","zh-CN"]:
        for suffix in ["png","svg"]:
            assert len(list((ROOT/"assets"/language).glob("*."+suffix)))==18,(language,suffix)
    print(f"PASS: 98 records; 41 losses; 5 statistical scenarios; 7 timing observations; 5 bilingual documents; {checked} local links; 36 figure pairs.")


if __name__=="__main__":
    main()
