# 🍇 Grape Disease Detection using AI & DevOps 🚀

A complete end-to-end AI-powered web application that leverages **Deep Learning + DevOps + AWS Cloud** to identify diseases in grape leaves. This project integrates **AWS SageMaker**, **Lambda**, **API Gateway**, **Terraform**, and **GitHub Actions** into a fully automated CI/CD pipeline — demonstrating real-world MLOps practices and scalable serverless deployment.

![App Screenshot](assets/screenshot.png) <!-- Replace with real screenshot -->

---

## 📌 Why This Project?

Grape farming is vulnerable to fungal and bacterial infections, leading to huge losses. Manual inspection is time-consuming and error-prone.

This solution provides a **real-time, AI-driven prediction system** deployed on the cloud, allowing farmers or agronomists to upload grape leaf images and receive **instant disease diagnosis** — all through a modern, DevOps-enabled pipeline.

---

## 🌟 Key Highlights

✅ End-to-End ML System (Training → Deployment → UI)  
✅ Real-time disease detection via Flask UI  
✅ Model hosted on **AWS SageMaker**  
✅ Inference served by **AWS Lambda** and **API Gateway**  
✅ Fully automated using **Terraform** and **GitHub Actions**  
✅ Serverless, cost-effective, scalable  

---

## 🧠 AI Capabilities

- **Model Type**: CNN-based deep learning model
- **Framework**: TensorFlow / PyTorch (exported to `.tar.gz`)
- **Training Dataset**: Labeled images of grape leaves
- **Classification Labels**:
  - 🍇 Black Rot  
  - 🍇 Esca (Black Measles)  
  - 🍇 Leaf Blight  
  - ✅ Healthy  

---

## 🧱 Tech Stack

| Layer             | Technology                           |
|------------------|--------------------------------------|
| Frontend UI       | HTML, CSS, Flask (Python)            |
| Backend API       | AWS Lambda + API Gateway             |
| ML Hosting        | AWS SageMaker                        |
| Infrastructure    | Terraform (IaC)                      |
| CI/CD Pipeline    | GitHub Actions                       |
| Artifact Storage  | Amazon S3                            |
| Containerization  | Lambda + ZIP package                 |

---

## 🖥️ User Features

- Upload any grape leaf image
- Get instant prediction from a trained AI model
- Clean, responsive, modern UI
- Works locally or hosted on cloud
- Integrated CI/CD for continuous delivery

---

## ⚙️ Workflow — How It Works

```mermaid
graph TD;
    A[User Uploads Image via Flask UI] --> B[Base64 Encoded & Sent to API Gateway];
    B --> C[API Gateway Triggers Lambda];
    C --> D[Lambda Calls SageMaker Endpoint];
    D --> E[SageMaker Returns Prediction];
    E --> F[Result Displayed on UI];
