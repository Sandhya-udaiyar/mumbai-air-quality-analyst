# Mumbai Air Quality Analyst

Automated pipeline that fetches Mumbai's PM2.5 and PM10 data daily,
computes daily averages, and saves a chart.

## Tools
Python, Pandas, Matplotlib, Open-Meteo API, GitHub Actions

## How it works
1. Fetch hourly air quality data from API
2. Clean data and calculate daily averages
3. Save daily.csv and chart.png
4. GitHub Actions runs this every day at 7:00 AM IST

## Limitations
- Data includes a few forecast days, not only actual readings
- Today's average can be partly forecast
- Only PM2.5 and PM10 are analysed

## Next steps
 An LLM (Gemini API) writes a short daily report in report.md
