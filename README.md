# 🍇 Grape Disease Detection using AI, Bedrock & DevOps 🚀

A complete end-to-end AI-powered web application that uses **Deep Learning + AWS Bedrock + DevOps + Cloud** to detect diseases in grape leaves. This project integrates **AWS SageMaker**, **Lambda**, **API Gateway**, **Bedrock**, **Terraform**, and **GitHub Actions** into a fully automated CI/CD pipeline — showcasing real-world MLOps practices with serverless infrastructure and GenAI explainability.

![App Screenshot](assets/screenshot.png) <!-- Replace with real screenshot -->

---

## 📌 Why This Project?

Grape crops are highly vulnerable to fungal diseases that drastically reduce yield and quality. Manual inspection is tedious and inaccurate.

This system provides a **real-time, AI-based diagnosis and GenAI explanation**, allowing farmers or researchers to upload an image and get:
- The **predicted disease name**
- An **explanation and treatment** generated using **AWS Bedrock (Claude / Titan)**

---

## 🌟 Key Highlights

✅ End-to-End MLOps Project: Train → Deploy → Explain  
✅ Real-time predictions with AI explainability via GenAI  
✅ Model hosted on **AWS SageMaker Endpoint**  
✅ Predictions served through **AWS Lambda + API Gateway**  
✅ Explanations generated via **AWS Bedrock (Claude/Titan)**  
✅ Infrastructure managed by **Terraform (IaC)**  
✅ CI/CD powered by **GitHub Actions**  
✅ Lightweight frontend using Flask (can be containerized)

---

## 🧠 AI & GenAI Capabilities

- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: PyTorch  
- **Trained On**: Grape leaf image dataset (labeled)
- **Prediction Classes**:
  - 🍇 Black Rot  
  - 🍇 Esca (Black Measles)  
  - 🍇 Leaf Blight  
  - ✅ Healthy  

- **GenAI Explanation**:  
  After predicting the disease, a prompt is sent to **AWS Bedrock** using **Claude v2 / Titan Text Lite**, generating actionable disease explanation and treatment steps.

---

## 🧱 Tech Stack Overview

| Layer              | Technology                            |
|-------------------|----------------------------------------|
| Frontend UI        | HTML + CSS + Flask (Python)           |
| Backend API        | AWS Lambda + API Gateway              |
| ML Model Hosting   | AWS SageMaker                         |
| GenAI Integration  | AWS Bedrock (Claude / Titan)          |
| Infrastructure     | Terraform (Infrastructure as Code)    |
| CI/CD              | GitHub Actions                        |
| Artifact Storage   | Amazon S3                             |
| Packaging          | Lambda ZIP Deployment                 |

---

## 🖥️ Features for Users

- Upload grape leaf image via a simple UI
- Receive:
  - Predicted disease name  
  - GenAI-generated explanation + treatment
- Scalable, secure, and serverless
- Can be run locally or fully cloud-hosted
- Re-deployable with one command (`terraform apply`)

---

## ⚙️ Workflow — How It Works

```mermaid
graph TD;
    A[User uploads grape leaf image via Flask UI] --> B[Base64 image sent to API Gateway];
    B --> C[API Gateway triggers Lambda function];
    C --> D[Lambda sends image to SageMaker Endpoint];
    D --> E[Model returns disease prediction];
    E --> F[Lambda sends prompt to Bedrock with disease name];
    F --> G[Bedrock returns explanation];
    G --> H[UI displays disease + treatment];
