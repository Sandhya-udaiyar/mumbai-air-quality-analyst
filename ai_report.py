import os, requests, pandas as pd
from datetime import date

today = date.today()
daily = pd.read_csv("daily.csv")
key = os.environ["GEMINI_API_KEY"]

prompt = f"""You are a data analyst.
Today is {today}. Mumbai daily PM2.5 and PM10 (ug/m3):
{daily.to_string(index=False)}

Rules:
- Dates after today are forecast, not actual readings. Say so.
- Do not guess causes. Use only this data.
Write: 1) most polluted day, 2) trend,
3) a 2-line recommendation. Keep it short."""

url = ("https://generativelanguage.googleapis.com/"
       "v1beta/models/gemini-3.5-flash:generateContent")
r = requests.post(
    url,
    headers={"x-goog-api-key": key},
    json={"contents": [{"parts": [{"text": prompt}]}]},
    timeout=60,
)
r.raise_for_status()

parts = r.json()["candidates"][0]["content"]["parts"]
text = "".join(p.get("text", "") for p in parts)

with open("report.md", "w", encoding="utf-8") as f:
    f.write(f"# Mumbai Air Quality Report ({today})\n\n{text}\n")
print(text)
