import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("WARNING: GEMINI_API_KEY not found in environment variables.")
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash')

    def generate_description(self, schema_text: str, sample_data_text: str, logs_text: str = "") -> dict:
        """
        Generates a metadata description using Google Gemini.
        """
        
        prompt = f"""
        Act as an Expert Data Engineer. Your task is to analyze the provided dataset schema and sample data to generate a comprehensive metadata description.

        **Input Data:**
        - **Schema:**
        {schema_text}

        - **Sample Data (First few rows):**
        {sample_data_text[:2000]}  # Truncate to avoid token limits if necessary

        - **Usage Logs (Context):**
        {logs_text[:1000]}

        **Output Requirement:**
        You must return a valid JSON object with the following structure. Do NOT include markdown formatting (like ```json) in the response, just the raw JSON string.

        {{
            "overview": "A detailed paragraph describing what this dataset represents, its potential business value, and what entities it contains.",
            "technical_details": {{
                "format": "Inferred format (e.g., CSV, JSON)",
                "key_fields": ["List", "of", "important", "columns"],
                "inferred_grain": "What does one row represent?"
            }},
            "data_quality": [
                {{ "field": "column_name", "issue": "Potential quality issue or observation (e.g., missing values, outlier)" }}
            ],
            "usage_tips": [
                "Specific SQL query idea or analysis suggestion",
                "Another tip"
            ],
            "enriched_schema": [
                {{ "name": "column_name", "type": "inferred_type", "description": "A rich, human-readable description of what this column contains." }}
            ]
        }}
        """

        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Clean up potential markdown formatting from the LLM
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
                
            return json.loads(response_text)
        except Exception as e:
            print(f"AI Generation Error: {e}")
            # Fallback to a simple error message in the UI
            return {
                "overview": f"Error generating metadata: {str(e)}",
                "technical_details": {},
                "data_quality": [],
                "usage_tips": [],
                "enriched_schema": []
            }

ai_service = AIService()
