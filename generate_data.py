import pandas as pd
import random
from datetime import datetime, timedelta

# Rich review templates
positive_reviews = [
    "Amazing food and excellent service",
    "Loved the ambiance and friendly staff",
    "Delicious meals and quick service",
    "Great experience, will visit again",
    "Outstanding food quality and cleanliness",
]

negative_reviews = [
    "Service was very slow and disappointing",
    "Food was cold and tasteless",
    "Dirty tables and rude staff",
    "Wait time was too long",
    "Overpriced and not worth it",
]

neutral_reviews = [
    "Food was okay, nothing special",
    "Average experience overall",
    "Service was decent but slow",
    "Prices are reasonable",
    "Not bad, not great",
]

def generate_review():
    sentiment = random.choice(["Positive", "Negative", "Neutral"])

    if sentiment == "Positive":
        review = random.choice(positive_reviews)
        food = random.randint(4, 5)
        service = random.randint(4, 5)
        price = random.randint(3, 5)
        cleanliness = random.randint(4, 5)

    elif sentiment == "Negative":
        review = random.choice(negative_reviews)
        food = random.randint(1, 3)
        service = random.randint(1, 3)
        price = random.randint(1, 3)
        cleanliness = random.randint(1, 3)

    else:
        review = random.choice(neutral_reviews)
        food = random.randint(2, 4)
        service = random.randint(2, 4)
        price = random.randint(2, 4)
        cleanliness = random.randint(2, 4)

    overall = round((food + service + price + cleanliness) / 4, 1)

    date = datetime.now() - timedelta(days=random.randint(0, 60))

    return [
        review,
        food,
        service,
        price,
        cleanliness,
        overall,
        sentiment,
        date.strftime("%Y-%m-%d")
    ]


# Generate dataset
data = [generate_review() for _ in range(1000)]

df = pd.DataFrame(data, columns=[
    "review",
    "food_rating",
    "service_rating",
    "price_rating",
    "cleanliness_rating",
    "overall_rating",
    "sentiment",
    "date"
])

# Save
df.to_csv("data/reviews.csv", index=False)

print("✅ Dataset generated with 1000 rows!")