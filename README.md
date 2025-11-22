# TCS Hackathon Metadata Enhancer App

![CI/CD Pipeline](https://github.com/akshayshinde1211/Hackathon-Metadata-Enhancer-App/actions/workflows/ci-cd.yml/badge.svg)

## 🚀 Project Overview
The **Metadata Description Enhancer** is an intelligent data governance tool designed to solve the "blank cover" problem in enterprise data catalogs. By leveraging Generative AI (Google Gemini), it automatically analyzes technical schemas and raw data samples to generate rich, business-ready documentation, data quality insights, and usage recommendations.

This project was built for the **TCS AI Fridays Hackathon** to demonstrate how GenAI can accelerate data literacy and governance.

## ✨ Key Features
*   **Automated Metadata Generation**: Instantly creates descriptions, business context, and technical summaries.
*   **Multi-Input Analysis**: Combines insights from JSON/DDL schemas, CSV sample data, and usage logs.
*   **Data Quality Assessment**: Automatically detects potential quality issues (missing values, outliers, format inconsistencies).
*   **Usage Recommendations**: Suggests SQL queries and analytical use cases for the data.
*   **Standardized Exports**: Download generated metadata in **JSON** or **XML** formats for easy integration with catalogs (e.g., Collibra, Alation).
*   **Enterprise UI**: A professional, TCS-branded web interface.

## 🛠️ Tech Stack
*   **Backend**: Python 3.10+, FastAPI
*   **Frontend**: HTML5, Tailwind CSS (via CDN), Vanilla JavaScript
*   **AI Engine**: Google Gemini 2.0 Flash (via `google-generativeai` SDK)
*   **Template Engine**: Jinja2

## 📋 Prerequisites
*   Python 3.10 or higher
*   A Google Gemini API Key

## ⚙️ Installation & Setup

1.  **Clone the Repository** (or extract the project folder):
    ```bash
    cd TCS
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    *   **Windows**:
        ```powershell
        .\venv\Scripts\activate
        ```
    *   **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, install manually: `pip install fastapi uvicorn python-multipart jinja2 python-dotenv google-generativeai requests`)*

5.  **Configure Environment Variables**:
    *   Create a `.env` file in the root directory.
    *   Add your Gemini API key:
        ```env
        GEMINI_API_KEY=your_actual_api_key_here
        ```

##  ▶️ Running the Application

1.  **Start the Server**:
    ```bash
    python main.py
    ```
    *Alternatively, use Uvicorn directly:*
    ```bash
    uvicorn main:app --reload
    ```

2.  **Access the Web Interface**:
    *   Open your browser and navigate to: `http://127.0.0.1:8000`

## 🐳 Docker Support

You can also run the application using Docker.

1.  **Build the Container**:
    ```bash
    docker-compose build
    ```

2.  **Run the Container**:
    ```bash
    docker-compose up
    ```
    *The application will be available at `http://localhost:8000`.*

## 🚀 DevOps Guide

This project is equipped with a complete DevOps lifecycle.

### 1. CI/CD Pipeline (GitHub Actions)
The pipeline automatically runs tests and builds the Docker image on every push to `main`.

**Setup:**
1.  Push this code to a GitHub repository.
2.  Go to **Settings > Secrets and variables > Actions**.
3.  Add the following Repository Secrets:
    *   `DOCKER_USERNAME`: Your Docker Hub username.
    *   `DOCKER_PASSWORD`: Your Docker Hub access token.

### 2. Kubernetes Deployment
Deploy the application to any Kubernetes cluster.

**Prerequisites:**
*   `kubectl` installed and configured.
*   A running Kubernetes cluster (e.g., Docker Desktop with Kubernetes enabled).

**Deploy:**
Run the helper script:
```bash
./scripts/deploy.sh
```
*You will be prompted to enter your Gemini API Key, which will be securely stored as a Kubernetes Secret.*

## 📂 Project Structure
```
TCS/
├── main.py                 # FastAPI application entry point
├── services/
│   ├── ai_service.py       # Logic for interacting with Google Gemini
│   └── parser_service.py   # File parsing logic (JSON, CSV)
├── templates/
│   └── index.html          # Main frontend UI (TCS branded)
├── static/
│   ├── js/
│   │   └── app.js          # Frontend logic
│   └── user_logo.png       # TCS Logo
├── test_data/              # Sample files for testing
│   ├── schema.json
│   └── data.csv
├── .env                    # API Key configuration (not committed)
└── README.md               # Project documentation
```

## 🛡️ License
This project is a hackathon prototype created for demonstration purposes.
