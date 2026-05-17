import pandas as pd

# Load TSV file
df = pd.read_csv("data/Restaurant_Reviews.tsv", sep="\t")

# Save as CSV inside data folder
df.to_csv("data/reviews.csv", index=False)

print("✅ Converted successfully to CSV!")