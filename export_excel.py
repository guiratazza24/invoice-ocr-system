import json
import pandas as pd

# read your JSON output
with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# convert to table
df = pd.DataFrame(data)

# export to Excel
df.to_excel("invoices.xlsx", index=False)

print("DONE ✅ Excel file created: invoices.xlsx")