# Fraud-detection-system
# 🛡️ Financial Fraud Detection System

An end-to-end Machine Learning web application designed to detect fraudulent financial transactions in real-time[cite: 1, 2, 8]. Built with a scikit-learn pipeline, Flask backend, and a modern cyber-styled glassmorphism frontend interface[cite: 1, 2, 8].


## 📌 Project Overview

Online financial fraud accounts for billions of dollars in losses annually. This project demonstrates an automated transaction monitoring solution trained on over 6.3 million transactions (Paysim financial dataset) to classify transactions as Fraudulent or Legitimate and compute confidence probabilities[cite: 1, 2, 7, 8].

### Key Highlights:
- Trained on 6.36M+ Records: Rigorous data exploration, handling extreme class imbalance (~0.13% fraud cases).
- Production Pipeline: Unified scikit-learn Pipeline integrating StandardScaler for numeric values, OneHotEncoder for transaction types, and class-balanced LogisticRegression.
- Lightweight & Fast: RESTful Flask API capable of serving real-time inferences with low latency.
- Modern Cyber UI: Responsive web application styled with pure CSS (DM Mono & Syne fonts), real-time probability progress indicator, and validation.
- Deploy Ready: Includes configuration (Procfile, gunicorn) for deployment on platforms like Render, Railway, or Heroku[cite: 1, 4, 8].
