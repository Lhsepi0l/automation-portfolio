import requests, json
from datetime import datetime

def report():
    fx=requests.get("https://api.exchangerate.host/latest?base=USD").json()
    eur=fx["rates"]["EUR"]
    krw=fx["rates"]["KRW"]
    rep=f"Report {datetime.now()}\nEUR:{eur}\nKRW:{krw}"
    out="api_report.txt"
    with open(out,"w") as f: f.write(rep)
    print("Saved", out)

if __name__=="__main__":
    report()
