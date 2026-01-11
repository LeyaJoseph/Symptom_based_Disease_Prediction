# Disease Prediction ML System with XGBoost on AWS

This project demonstrates an **end-to-end machine learning system** for predicting diseases based on a patient’s symptoms. The system is designed, developed, tested, and deployed on AWS, covering the complete ML lifecycle including data processing, model training, evaluation, monitoring, CI/CD, model registry, and deployment.

The model predicts **41 different disease classes** using patient symptom data. An **XGBoost classifier** was trained and evaluated, achieving **97% test accuracy**. The project emphasizes building **production-ready ML workflows** for real-world predictive analytics.

---

## 🚀 Features
- **End-to-End ML Pipeline**: From EDA and feature store creation to model training, evaluation, and deployment  
- **High Accuracy Model**: XGBoost model achieving 97% test accuracy for multi-class disease classification  
- **Real-Time Inference**: Deployed model endpoint for live predictions  
- **Batch Predictions**: Batch transform jobs for large-scale inference  
- **Monitoring & Alerts**: Model monitors and CloudWatch alarms with artificial traffic testing  
- **Automated CI/CD**: AWS Lambda and EventBridge trigger pipelines on dataset updates  
- **Model Registry Integration**: Pipeline automatically adds approved models to the SageMaker Model Registry  
- **Parameterizable SageMaker Pipeline**: Controls accuracy thresholds, dataset URIs, instance type/count, and model approval status  

---

## 🧠 System Architecture

### ML Pipeline Overview
1. **Exploratory Data Analysis (EDA)** – Understanding and preprocessing symptom datasets  
2. **Feature Store Creation** – Centralized storage of features for consistent model input  
3. **Model Training & Testing** – XGBoost classifier trained on labeled symptom data  
4. **Evaluation** – Test dataset used to calculate performance metrics, achieving **97% accuracy**  
5. **Batch Transform** – Predict outputs for test or new datasets  
6. **Model Registry** – Pipeline adds the trained and approved model to the SageMaker Model Registry  
7. **Real-Time Endpoint Deployment** – Enables live predictions  
8. **Monitoring & Alerts** – Model monitors track performance; CloudWatch alarms notify anomalies  

### CI/CD & Automation
- **SageMaker Pipeline**: Combines preprocessing, training, evaluation, model registry addition, and batch transform steps  
- **Condition Step**: Checks model accuracy against a threshold before adding the model to the registry and proceeding  
- **Pipeline Parameters**: Accuracy threshold, training/testing dataset URIs, instance count/type, and model approval status  
- **Automation**: New dataset in S3 triggers EventBridge → Lambda → SageMaker Pipeline (preprocessing, model training, model evaluation, performance criteria checks, registry addition, batch transform)  

This ensures **automated, reliable, and reproducible ML workflows** for production.

---

## 🛠️ Tech Stack
- **AWS Services**: SageMaker, Lambda, EventBridge, CloudWatch, S3, SageMaker Feature Store, Model Registry  
- **Machine Learning**: XGBoost, Python (scikit-learn, pandas, numpy)  
- **CI/CD & Automation**: SageMaker Pipelines, Lambda functions, EventBridge triggers  
- **Monitoring**: SageMaker Model Monitors, CloudWatch alarms  

---

## 📌 Use Cases
- Predicting disease prognosis based on patient symptoms  
- Rapid and accurate multi-class classification for healthcare analytics  
- Demonstration of end-to-end ML deployment and automation on cloud  
- Production-ready predictive pipelines for healthcare or research environments  

---

## 💡 Highlights
- Multi-class classification with **41 disease categories**  
- High-performing XGBoost model with **97% test accuracy**  
- Fully automated pipeline including **preprocessing, training, evaluation, model registry, deployment, and monitoring**  
- Real-time and batch predictions for operational use  
- CI/CD setup ensures **automatic retraining, registry addition, and redeployment** upon dataset updates  

---
