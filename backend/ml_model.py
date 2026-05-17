from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model(data):
    # Features & Labels
    X = data["clean_review"]
    y = data["sentiment"]

    # ✅ Train-Test Split (stratified = balanced classes)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # ✅ TF-IDF (improved)
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),   # unigram + bigram
        stop_words="english"
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # ✅ Logistic Regression (balanced)
    model = LogisticRegression(
        max_iter=300,
        class_weight="balanced"
    )

    model.fit(X_train_vec, y_train)

    # ✅ Evaluation on unseen data
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)

    return model, vectorizer, accuracy


def predict_sentiment(model, vectorizer, text):
    return model.predict(vectorizer.transform([text]))[0]