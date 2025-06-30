from datetime import datetime, timedelta
import re

def get_progress(start, end):
    now = datetime.now()
    total = (end - start).total_seconds()
    elapsed = (now - start).total_seconds()
    return round((elapsed / total) * 100)

def day_progress():
    now = datetime.now()
    start = datetime(now.year, now.month, now.day)
    end = start + timedelta(days=1)
    return get_progress(start, end)

def week_progress():
    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    start = datetime(start.year, start.month, start.day)
    end = start + timedelta(days=7)
    return get_progress(start, end)

def month_progress():
    now = datetime.now()
    start = datetime(now.year, now.month, 1)
    if now.month == 12:
        end = datetime(now.year + 1, 1, 1)
    else:
        end = datetime(now.year, now.month + 1, 1)
    return get_progress(start, end)

def year_progress():
    now = datetime.now()
    start = datetime(now.year, 1, 1)
    end = datetime(now.year + 1, 1, 1)
    return get_progress(start, end)

def build_progress_section():
    dp = day_progress()
    wp = week_progress()
    mp = month_progress()
    yp = year_progress()

    return f"""
<!-- PROGRESS-START -->
| Time  | Progress |
|-------|----------|
| Day   | ![](https://progress-bar.dev/{dp}/?width=200&title=Day&color=40c057) |
| Week  | ![](https://progress-bar.dev/{wp}/?width=200&title=Week&color=fab005) |
| Month | ![](https://progress-bar.dev/{mp}/?width=200&title=Month&color=4dabf7) |
| Year  | ![](https://progress-bar.dev/{yp}/?width=200&title=Year&color=be4bdb) |
<!-- PROGRESS-END -->
""".strip()

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_progress = build_progress_section()

    updated = re.sub(
        r"<!-- PROGRESS-START -->(.|\s)*?<!-- PROGRESS-END -->",
        new_progress,
        content,
        flags=re.MULTILINE
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    update_readme()
