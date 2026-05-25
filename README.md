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

"Best restaurants in Bangalore under ₹500"
"Which cuisine is most popular in Hyderabad?"
"Top-rated restaurants in Pune"
"Recommend budget-friendly options in Nagpur"
"What are the highest-rated North Indian restaurants?"

---

## 📂 Project Structure
```text
ai-restaurant-analytics-dashboard/
│
├── backend/
│   ├── app.py                  # Flask application entry point
│   ├── preprocess.py           # Data cleaning and transformation
│   ├── ml_model.py             # Hugging Face LLM integration
│   └── sentiment_model.py      # Sentiment analysis (future)
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Dashboard styling
│   │   ├── js/
│   │   │   ├── dashboard.js    # Chart.js visualizations
│   │   │   └── ai-assistant.js # AI chat interface
│   │   └── images/
│   │       └── logo.png
│   │
│   └── templates/
│       └── index.html          # Main dashboard template
│
├── data/
│   ├── zomato.csv              # Primary restaurant dataset
│   ├── reviews.csv             # Customer reviews (optional)
│   └── Country-Code.xlsx       # Country code mapping
│
├── assets/
│   └── dashboard-preview.png   # README screenshots
│
├── .env.example                # Environment variables template
├── .gitignore
├── requirements.txt            # Python dependencies
├── README.md
└── LICENSE
```
---


## 🔌 API Endpoints

### GET `/api/restaurants`
Fetch all restaurants with optional filters.

**Query Parameters:**
- `city` (optional): Filter by city name
- `cuisine` (optional): Filter by cuisine type

**Response:**
```json
{
  "total": 9551,
  "restaurants": [
    {
      "name": "Empire Restaurant",
      "city": "Bangalore",
      "cuisine": "North Indian, Chinese",
      "rating": 4.1,
      "votes": 10934,
      "cost": 800
    }
  ]
}
```

### POST `/api/ai-query`
Send natural language query to AI assistant.

**Request Body:**
```json
{
  "query": "Best restaurants in Bangalore under 500"
}
```

**Response:**
```json
{
  "response": "Here are the top budget-friendly restaurants...",
  "recommendations": [...]
}
```

---

## 📊 Insights & Analytics

Key findings from the dataset analysis:

| Metric | Value |
|--------|-------|
| **Total Restaurants** | 9,551 |
| **Cities Covered** | 15+ |
| **Average Rating** | 3.7/5 |
| **Price Range** | ₹50 - ₹6,000 |
| **Most Popular Cuisine** | North Indian (30.3%) |
| **Highest Rated City** | Bangalore (avg 3.9) |
| **Most Active Users** | 1.2M+ votes |

### Top 5 Cuisines
1. North Indian - 2,890 restaurants
2. Chinese - 1,854 restaurants
3. Fast Food - 1,421 restaurants
4. South Indian - 1,230 restaurants
5. Continental - 987 restaurants

---

## 📸 Screenshots

### Main Dashboard
![Dashboard](assets/dashboard.png)

### AI Assistant
![AI Chat](assets/ai-assistant.png)

### Charts & Visualizations
![Charts](assets/charts.png)

---

## 🎯 Future Enhancements

- [ ] **Map Integration**: Leaflet.js for restaurant locations
- [ ] **Sentiment Analysis**: Analyze customer reviews with NLP
- [ ] **User Authentication**: Save preferences and favorites
- [ ] **Advanced Filters**: Dietary restrictions, ambiance, parking
- [ ] **Mobile App**: React Native companion app
- [ ] **Real-time Updates**: Live restaurant data integration
- [ ] **Recommendation Engine**: Collaborative filtering
- [ ] **Cloud Deployment**: AWS/Heroku hosting

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Pooja Sukhdeve**  
Master's in Computer Science | Boston University Metropolitan College

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](YOUR_LINKEDIN)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-green)](YOUR_PORTFOLIO)
[![Email](https://img.shields.io/badge/Email-Contact-red)](mailto:your.email@example.com)

---

## 🙏 Acknowledgments

- [Zomato](https://www.zomato.com/) for the dataset
- [Hugging Face](https://huggingface.co/) for LLM API
- [Chart.js](https://www.chartjs.org/) for visualization library
- [Flask](https://flask.palletsprojects.com/) community

---

<div align="center">

**If you found this project helpful, please consider giving it a ⭐!**

Made with ❤️ by Pooja Sukhdeve

</div>

