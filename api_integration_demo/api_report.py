import requests
from datetime import datetime


FX_URL = "https://open.er-api.com/v6/latest/USD"  # 공개 환율 API


def get_rates():
    resp = requests.get(FX_URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # 기대하는 구조: {"rates": {"EUR": ..., "KRW": ...}, ...}
    if "rates" not in data:
        print("Unexpected FX response:", data)
        return None, None

    eur = data["rates"].get("EUR")
    krw = data["rates"].get("KRW")
    return eur, krw


def build_report():
    eur, krw = get_rates()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"FX Report - {now}", ""]

    if eur is None or krw is None:
        lines.append("Failed to fetch FX rates.")
    else:
        lines.append("💱 FX (USD base):")
        lines.append(f" - EUR: {eur}")
        lines.append(f" - KRW: {krw}")

    return "\n".join(lines)


def report():
    text = build_report()
    out = "api_report.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print("Saved", out)


if __name__ == "__main__":
    report()
