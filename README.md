# Metadata Enhancer

<div align="center">

![CI/CD](https://github.com/akshayshinde1211/Hackathon-Metadata-Enhancer-App/actions/workflows/ci-cd.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![Kubernetes](https://img.shields.io/badge/kubernetes-deployable-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**An Enterprise-Grade Data Governance Tool Powered by Generative AI**

[Features](#-key-features) • [Architecture](#-system-architecture) • [Getting Started](#-getting-started) • [DevOps](#-engineering-excellence)

</div>

---

## 🚀 Project Overview

The **Metadata Enhancer** solves the critical "blank cover" problem in enterprise data catalogs. By leveraging **Google Gemini 2.0**, it automatically analyzes technical schemas, raw data samples, and usage logs to generate rich, business-ready documentation.

This project demonstrates a complete **End-to-End DevOps Lifecycle**, featuring containerization, automated CI/CD pipelines, and Kubernetes orchestration.

## 🏗 System Architecture

```mermaid
graph TD
    User[User] -->|Uploads Files| UI[Frontend (HTML/JS)]
    UI -->|POST /api/generate| API[FastAPI Backend]
    API -->|Parse| Parser[Parser Service]
    API -->|Context| AI[AI Service]
    AI -->|Prompt| Gemini[Google Gemini API]
    Gemini -->|Description| AI
    AI -->|JSON Result| API
    API -->|Response| UI
```

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **🤖 AI-Powered Analysis** | Instantly generates business context and descriptions from raw schemas. |
| **📊 Multi-Source Input** | Combines insights from JSON/DDL schemas, CSV samples, and logs. |
| **🛡️ Data Quality** | Automatically detects missing values, outliers, and format inconsistencies. |
| **💡 Smart Recommendations** | Suggests SQL queries and analytical use cases for the data. |
| **📦 Standardized Exports** | Download metadata in JSON or XML for integration with catalogs like Collibra. |

## 🛠 Tech Stack

*   **Backend**: Python 3.9, FastAPI
*   **Frontend**: Vanilla JS, Tailwind CSS
*   **AI Engine**: Google Gemini 2.0 Flash
*   **Infrastructure**: Docker, Kubernetes
*   **CI/CD**: GitHub Actions

## 🏁 Getting Started

### Option 1: Docker (Recommended)
Run the application in a containerized environment.

```bash
# Build and Run
docker-compose up --build
```
*Access the app at `http://localhost:8000`*

### Option 2: Local Development
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure Environment**:
    Create a `.env` file with your API key:
    ```env
    GEMINI_API_KEY=your_key_here
    ```
3.  **Run Server**:
    ```bash
    uvicorn main:app --reload
    ```

## ⚙️ Engineering Excellence (DevOps)

This project is built with modern DevOps best practices.

### 🔄 CI/CD Pipeline
*   **Automated Testing**: Every push triggers `flake8` linting and unit tests.
*   **Continuous Delivery**: Successful builds are automatically pushed to Docker Hub.
*   **Workflow**: Defined in `.github/workflows/ci-cd.yml`.

### ☸️ Kubernetes Orchestration
Deployable to any K8s cluster with high availability.

```bash
# Deploy to cluster
./scripts/deploy.sh
```
*   **Scalability**: Configured for 2 replicas by default.
*   **Security**: API keys are managed via Kubernetes Secrets.

## 🔒 Security

*   **Secret Management**: No hardcoded keys. Uses `.env` for local and K8s Secrets for production.
*   **Least Privilege**: Docker container runs as a non-root user (configurable).
*   **Image Safety**: Built on official `python:slim` images to reduce vulnerabilities.

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
<div align="center">
    <sub>Built by Akshay Shinde</sub>
</div>
