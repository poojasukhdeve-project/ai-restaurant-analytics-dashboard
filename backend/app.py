from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

import pandas as pd
import requests
import os
import re

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

# =====================================================
# FLASK APP
# =====================================================

app = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(
    '../data/zomato.csv',
    encoding='latin1'
)

# =====================================================
# INDIA DATA ONLY
# =====================================================

df = df[
    df['Country Code'] == 1
]

# =====================================================
# CLEAN DATA
# =====================================================

df.dropna(inplace=True)

df = df[
    df['Aggregate rating'] > 0
]

# =====================================================
# ALL INDIAN CITIES
# =====================================================

INDIAN_CITIES = sorted(

    df['City']
    .dropna()
    .unique()
    .tolist()
)

# =====================================================
# HOME PAGE
# =====================================================

@app.route('/')
def home():

    return render_template(
        'index.html'
    )

# =====================================================
# DASHBOARD DATA API
# =====================================================

@app.route('/dashboard-data')
def dashboard_data():

    selected_city = request.args.get(
        'city',
        'Bangalore'
    )

    filtered_df = df[
        df['City'] == selected_city
    ]

    total_restaurants = int(
        filtered_df.shape[0]
    )

    avg_rating = round(

        filtered_df[
            'Aggregate rating'
        ].mean(),

        2
    )

    avg_cost = int(

        filtered_df[
            'Average Cost for two'
        ].mean()
    )

    total_votes = int(

        filtered_df[
            'Votes'
        ].sum()
    )

    # =========================================
    # TOP CUISINES
    # =========================================

    top_cuisines = (

        filtered_df['Cuisines']

        .str.split(', ')

        .explode()

        .value_counts()

        .head(5)
    )

    # =========================================
    # RATING DISTRIBUTION
    # =========================================

    rating_distribution = (

        filtered_df[
            'Aggregate rating'
        ]

        .round()

        .value_counts()

        .sort_index()
    )

    # =========================================
# TOP RESTAURANT RATINGS
# =========================================

    top_rated_restaurants = (

    filtered_df[
        [
            'Restaurant Name',
            'Aggregate rating'
        ]
    ]

    .sort_values(

        by='Aggregate rating',

        ascending=False
    )

    .head(10)
)

# =========================================
# CUISINE POPULARITY
# =========================================

    cuisine_popularity = (

    filtered_df['Cuisines']

    .str.split(', ')

    .explode()

    .value_counts()

    .head(5)
)

    # =========================================
    # TOP RESTAURANTS TABLE
    # =========================================

    restaurants = (

        filtered_df[
            [
                'Restaurant Name',
                'City',
                'Cuisines',
                'Aggregate rating',
                'Votes',
                'Average Cost for two'
            ]
        ]

        .sort_values(

            by=[
                'Aggregate rating',
                'Votes'
            ],

            ascending=False
        )

        .head(10)
    )

    response = {

        'total_restaurants':
        total_restaurants,

        'avg_rating':
        avg_rating,

        'avg_cost':
        avg_cost,

        'total_votes':
        total_votes,

        'top_cuisines':
        top_cuisines.to_dict(),

        'rating_distribution':
        rating_distribution.to_dict(),

        'top_rated_restaurants':
        top_rated_restaurants.to_dict(
        orient='records'
       ),

      'cuisine_popularity':
      cuisine_popularity.to_dict(),

        'cities':
        INDIAN_CITIES,

        'restaurants':
        restaurants.to_dict(
            orient='records'
        )
    }

    return jsonify(response)

# =====================================================
# HUGGINGFACE API
# =====================================================

def ask_huggingface(prompt):

    API_URL = (
        "https://router.huggingface.co/v1/chat/completions"
    )

    headers = {

        "Authorization":
        f"Bearer {HF_TOKEN}",

        "Content-Type":
        "application/json"
    }

    payload = {

        "model":
        "meta-llama/Llama-3.1-8B-Instruct",

        "messages": [

            {
                "role": "system",

                "content":
                """
You are an AI Restaurant Analytics Assistant.

Rules:
- Use ONLY provided dataset insights
- Never invent fake restaurants
- Keep answers concise
- Use short bullet points
- Focus on ratings, cuisines, votes, and pricing
- Sound premium and modern
- Avoid long paragraphs
- Respond like a business dashboard AI
"""
            },

            {
                "role": "user",
                "content": prompt
            }
        ],

        "max_tokens": 120,

        "temperature": 0.4
    }

    try:

        response = requests.post(

            API_URL,

            headers=headers,

            json=payload
        )

        result = response.json()

        return result[
            'choices'
        ][0][
            'message'
        ][
            'content'
        ]

    except Exception as e:

        return f"""
❌ AI Error

{str(e)}
"""

# =====================================================
# AI CHAT API
# =====================================================

@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()

    user_message = data.get(
        'message',
        ''
    )

    user_message_lower = user_message.lower()

    # =========================================
    # DETECT CITY
    # =========================================

    selected_city = data.get(
        'city',
        'Bangalore'
    )

    for city in INDIAN_CITIES:

        if city.lower() in user_message_lower:

            selected_city = city
            break

    # =========================================
    # FILTER CITY DATA
    # =========================================

    city_df = df[
        df['City'] == selected_city
    ]

    # =========================================
    # DETECT BUDGET
    # =========================================

    budget = None

    numbers = re.findall(
        r'\d+',
        user_message
    )

    if numbers:

        budget = int(numbers[0])

    # =========================================
    # DETECT RESTAURANT
    # =========================================

    detected_restaurant = None

    for restaurant in city_df[
        'Restaurant Name'
    ].unique():

        if restaurant.lower() in user_message_lower:

            detected_restaurant = restaurant
            break

    # =========================================
    # RESTAURANT ANALYTICS
    # =========================================

    if detected_restaurant:

        restaurant_df = city_df[
            city_df['Restaurant Name']
            == detected_restaurant
        ]

        restaurant = restaurant_df.iloc[0]

        restaurant_name = restaurant[
            'Restaurant Name'
        ]

        restaurant_rating = restaurant[
            'Aggregate rating'
        ]

        restaurant_votes = restaurant[
            'Votes'
        ]

        restaurant_cuisines = restaurant[
            'Cuisines'
        ]

        restaurant_cost = restaurant[
            'Average Cost for two'
        ]

        prompt = f"""
User Question:
{user_message}

Restaurant Analytics:

Restaurant:
{restaurant_name}

City:
{selected_city}

Rating:
{restaurant_rating}

Votes:
{restaurant_votes}

Cuisine:
{restaurant_cuisines}

Average Cost for Two:
₹{restaurant_cost}

Generate:
- concise dashboard response
- short insights
- premium formatting
"""

        ai_reply = ask_huggingface(
            prompt
        )

        return jsonify({

            'reply': ai_reply
        })

    # =========================================
    # BUDGET FILTER
    # =========================================

    filtered_budget_df = city_df.copy()

    if budget:
        
        filtered_budget_df = city_df[
            
            city_df[
            'Average Cost for two'
            ] <= budget
     ]

    # fallback if no restaurants found

    if filtered_budget_df.empty:

        filtered_budget_df = city_df[

            city_df[
                'Average Cost for two'
            ] <= budget + 300
        ]

    # =========================================
    # TOP RESTAURANTS
    # =========================================

    top_restaurants = (

        filtered_budget_df[
            [
                'Restaurant Name',
                'Aggregate rating',
                'Cuisines',
                'Votes',
                'Average Cost for two'
            ]
        ]

        .sort_values(

            by=[
                'Aggregate rating',
                'Votes'
            ],

            ascending=False
        )

        .head(5)
    )

    restaurant_text = ""

    for _, row in top_restaurants.iterrows():

        restaurant_text += f"""

Restaurant:
{row['Restaurant Name']}

Rating:
{row['Aggregate rating']}

Cuisine:
{row['Cuisines']}

Votes:
{row['Votes']}

Cost for Two:
₹{row['Average Cost for two']}
"""

    # =========================================
    # TOP CUISINES
    # =========================================

    top_cuisines = (

        city_df['Cuisines']

        .str.split(', ')

        .explode()

        .value_counts()

        .head(5)
    )

    cuisine_text = ""

    for cuisine, count in top_cuisines.items():

        cuisine_text += f"""
- {cuisine} ({count} restaurants)
"""

    # =========================================
    # CITY ANALYTICS
    # =========================================

    total_restaurants = int(
        city_df.shape[0]
    )

    avg_rating = round(

        city_df[
            'Aggregate rating'
        ].mean(),

        2
    )

    avg_cost = int(

        city_df[
            'Average Cost for two'
        ].mean()
    )

    total_votes = int(

        city_df[
            'Votes'
        ].sum()
    )

    # =========================================
    # PROMPT
    # =========================================

    prompt = f"""
User Question:
{user_message}

City:
{selected_city}

Budget:
₹{budget if budget else "Not Specified"}

Total Restaurants:
{total_restaurants}

Average Rating:
{avg_rating}

Average Cost:
₹{avg_cost}

Total Votes:
{total_votes}

Top Cuisines:
{cuisine_text}

Recommended Restaurants:
{restaurant_text}

Generate:
- premium AI response
- concise insights
- dashboard style
- short bullets
- modern formatting
"""

    ai_reply = ask_huggingface(
        prompt
    )

    return jsonify({

        'reply': ai_reply
    })

# =====================================================
# RUN APP
# =====================================================

if __name__ == '__main__':

    app.run(
        debug=True
    )