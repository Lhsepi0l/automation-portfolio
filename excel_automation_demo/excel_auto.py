import pandas as pd
from datetime import datetime

def automate():
    df=pd.DataFrame({
        "product":["A","B","C","A","B"],
        "amount":[10,20,30,5,15]
    })
    total=df["amount"].sum()
    avg=df["amount"].mean()
    summary=pd.DataFrame([["Total",total],["Average",avg]],columns=["Metric","Value"])
    out=f"excel_report_{datetime.now().strftime('%Y%m%d')}.xlsx"
    with pd.ExcelWriter(out, engine="openpyxl") as w:
        df.to_excel(w, sheet_name="Raw", index=False)
        summary.to_excel(w, sheet_name="Summary", index=False)
    print("Saved", out)

if __name__=="__main__":
    automate()
