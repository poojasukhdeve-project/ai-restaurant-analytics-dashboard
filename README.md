# 🍽️ AI-Powered Restaurant Analytics Dashboard

An intelligent full-stack analytics platform that analyzes **9,551 restaurants** across 15+ Indian cities using the Zomato dataset. Built with Flask, Chart.js, and Hugging Face LLM API for conversational business intelligence.

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](YOUR_DEMO_LINK)
[![GitHub](https://img.shields.io/badge/github-repo-blue)](YOUR_GITHUB_LINK)

![Dashboard Preview](assets/dashboard-preview.png)

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Insights & Analytics](#insights--analytics)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## ✨ Features

### 📊 Interactive Analytics Dashboard
- **Real-time KPI Cards**: Total restaurants, average ratings, cost, and votes
- **Dynamic Visualizations**: Rating distribution, cuisine popularity, top restaurants
- **City Filtering**: Analyze data across 15+ Indian cities
- **Responsive Design**: Modern dark-themed UI

### 🤖 AI Restaurant Assistant
- **Natural Language Queries**: Ask questions in plain English
- **Smart Recommendations**: Budget-based and cuisine-specific suggestions
- **Instant Insights**: Powered by Hugging Face LLM API
- **Context-Aware Responses**: Understands restaurant domain

### 📈 Business Intelligence
- Cuisine trend analysis across cities
- Budget distribution and pricing patterns
- Customer engagement metrics (ratings & votes)
- Top-performing restaurants identification

---

## 🛠️ Tech Stack

**Backend**
- Python 3.8+
- Flask (REST API)
- Pandas (Data processing)

**Frontend**
- HTML5, CSS3, JavaScript
- Chart.js (Data visualization)
- Responsive design

**AI/ML**
- Hugging Face Inference API
- Natural Language Processing

**Dataset**
- Zomato India Dataset (9,551 restaurants)

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Hugging Face API key ([Get it here](https://huggingface.co/settings/tokens))

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-restaurant-analytics-dashboard.git
cd ai-restaurant-analytics-dashboard
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory:
```env
HUGGINGFACE_API_KEY=your_api_key_here
FLASK_ENV=development
```

### Step 5: Run the Application
```bash
python backend/app.py
```

Visit **http://127.0.0.1:5000** in your browser.

---

## 💡 Usage

### Dashboard Navigation
1. **Select City**: Use dropdown to filter restaurants by city
2. **View Analytics**: Explore KPI cards and interactive charts
3. **Browse Restaurants**: Scroll through top-rated establishments

### AI Assistant Queries
Try these example questions:









---

# 🚀 Features

## 📊 Interactive Analytics Dashboard
- KPI Cards
  - Total Restaurants
  - Average Rating
  - Average Cost
  - Total Votes

- Interactive Charts
  - Rating Distribution
  - Top Cuisines
  - Top Restaurant Ratings
  - Cuisine Popularity

- Dynamic Restaurant Table
  - Top 10 restaurants
  - Ratings
  - Votes
  - Cuisine information

---

# 🤖 AI Restaurant Assistant

Integrated AI-powered restaurant assistant using **Hugging Face LLM API**.

The AI assistant can answer questions like:
- Best restaurants in Bangalore
- Budget-friendly restaurants
- Popular cuisines in a city
- Highest-rated restaurants
- Restaurant recommendations
- Cost analysis
- Customer insights

---

# 🏙️ Supported Indian Cities

The dashboard supports multiple Indian cities including:

- Bangalore
- Chennai
- Goa
- Hyderabad
- Kolkata
- Lucknow
- Mohali
- Panchkula
- Pune
- Secunderabad
- Ahmedabad
- Chandigarh
- Nagpur
- Mumbai
- Delhi
- Jaipur
- Surat
- Vadodara
- Kochi
- Coimbatore

and more.

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

## Backend
- Python
- Flask

## AI Integration
- Hugging Face Inference API

## Dataset
- Zomato India Dataset

---

# 📈 Dashboard Preview

## Main Dashboard
- Modern dark-themed analytics interface
- Interactive charts and filters
- AI-powered insights

## AI Assistant
- Smart restaurant recommendations
- Budget analysis
- Cuisine insights
- Natural language interaction

---

# 📂 Project Structure

```bash
ai-restaurant-analytics-dashboard/
│
├── backend/
│   ├── app.py
│   ├── preprocess.py
│   ├── ml_model.py
│   └── sentiment_model.py
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── templates/
│       └── index.html
│
├── data/
│   ├── zomato.csv
│   ├── reviews.csv
│   └── Country-Code.xlsx
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-restaurant-analytics-dashboard.git
```

---

## 2️⃣ Navigate to Project

```bash
cd ai-restaurant-analytics-dashboard
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add Hugging Face API Key

Create a `.env` file:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

---

## 5️⃣ Run Application

```bash
python backend/app.py
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

# 📊 Example AI Questions

Try asking:

- Best restaurants in Bangalore
- Popular cuisines in Goa
- Recommend restaurants under ₹500
- Highest rated restaurants in Pune
- Which cuisine is most popular in Hyderabad?
- Budget-friendly restaurants in Nagpur
- Top cafes in Bangalore
- Restaurants with highest customer votes

---

# 🎯 Project Goals

This project was designed to:
- Analyze restaurant business trends
- Visualize customer preferences
- Build an AI-powered analytics dashboard
- Demonstrate full-stack development skills
- Integrate LLM APIs into business applications

---

# 💡 Key Highlights

✅ Full-Stack Dashboard  
✅ Interactive Data Visualization  
✅ AI-Powered Assistant  
✅ Business Intelligence Insights  
✅ Real Dataset Analysis  
✅ Dynamic Filtering  
✅ Modern UI/UX  
✅ Recruiter-Friendly Portfolio Project

---

# 📌 Future Improvements

- Live Maps Integration
- Restaurant Sentiment Analysis
- User Authentication
- Cloud Deployment
- Real-time Data Updates
- Recommendation Engine
- Advanced NLP Insights
- Mobile Responsive Optimization

---

# 👩‍💻 Author

### Pooja Sukhdeve

Master's Student in Computer Science  
Boston University Metropolitan College

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!
