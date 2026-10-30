import requests, time, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {"latitude": 19.07, "longitude": 72.88,
          "hourly": "pm2_5,pm10", "timezone": "Asia/Kolkata",
          "past_days": 7}

data = None
for attempt in range(4):
    try:
        data = requests.get(url, params=params, timeout=90).json()
        break
    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(10)

if data is None:
    raise SystemExit("API did not respond after 4 tries")
df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])
df = df.dropna()
df["date"] = df["time"].dt.date

daily = df.groupby("date")[["pm2_5", "pm10"]].mean().round(1)
daily.to_csv("daily.csv")

daily["pm2_5"].plot(kind="bar", title="Mumbai daily PM2.5")
plt.tight_layout()
plt.savefig("chart.png")
print(daily)
