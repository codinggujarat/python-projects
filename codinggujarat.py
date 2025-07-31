import json
import re
from datetime import datetime, timedelta
from collections import defaultdict

# 1) Load raw JSON from file (may contain back-to-back arrays)
with open("data.json", "r", encoding="utf-8") as f:
    raw_data = f.read()

# 2) Extract all JSON array blocks
json_arrays = re.findall(r'\[\s*{.*?}\s*\]', raw_data, re.DOTALL)
all_items = []

# 3) Date sequence setup: start 29 Nov 2022, increment 2 days
start_date = datetime.strptime("2022-11-29", "%Y-%m-%d")
interval = timedelta(days=2)
counter = 0

# 4) Category counter
category_counts = defaultdict(int)

# 5) Parse and normalize every entry
for array in json_arrays:
    try:
        items = json.loads(array)
        for item in items:
            title = item.get("title", "").strip()
            link = item.get("link") or item.get("url", "")
            image = item.get("image", "")
            author = item.get("author") or item.get("published_by", "CodingGujarat")

            # Normalize author
            if author.strip().lower() == "letscode":
                author = "CodingGujarat"

            # Assign category based on title content
            title_lower = title.lower()
            if any(kw in title_lower for kw in ["html", "css", "JavaScript"]):
                category = "frontend"
            elif "python" in title_lower:
                category = "python"
            elif "php" in title_lower:
                category = "php"
            elif "reactjs" in title_lower:
                category = "reactjs"
            else:
                category = "other"

            category_counts[category] += 1

            # Assign date (2 days apart)
            new_date = start_date + counter * interval
            formatted_date = new_date.strftime("%B %#d, %Y")  # For Windows

            all_items.append({
                "title": title,
                "link": link,
                "image": image,
                "date": formatted_date,
                "author": author.strip(),
                "category": category
            })

            counter += 1

    except json.JSONDecodeError:
        continue

# 6) Remove duplicates by title OR link
seen_titles = set()
seen_links = set()
unique_items = []
duplicates = 0

for item in all_items:
    title_key = item["title"].lower()
    link_key = item["link"].lower()
    if title_key in seen_titles or link_key in seen_links:
        duplicates += 1
    else:
        seen_titles.add(title_key)
        seen_links.add(link_key)
        unique_items.append(item)

# 7) Report counts
print(f"Total raw entries:      {len(all_items)}")
print(f"Duplicates removed:     {duplicates}")
print(f"Total unique entries:   {len(unique_items)}")

print("\n📊 Category Breakdown:")
final_category_counts = defaultdict(int)
for item in unique_items:
    final_category_counts[item['category']] += 1

for cat, count in sorted(final_category_counts.items()):
    print(f"- {cat}: {count} entries")

# 8) Save output
with open("standardized_projects.json", "w", encoding="utf-8") as f:
    json.dump(unique_items, f, indent=2)

print("\n✅ Cleaned data with categories saved to standardized_projects.json")
