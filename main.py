from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
import uvicorn
import json
import xml.etree.ElementTree as ET

from services.parser_service import parse_file_content
from services.ai_service import ai_service

app = FastAPI(title="Metadata Enhancer")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# In-memory store for the last generated result (for demo purposes)
last_generated_result = {}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/generate")
async def generate_metadata(
    schema_file: UploadFile = File(...),
    sample_data_file: Optional[UploadFile] = File(None),
    logs_file: Optional[UploadFile] = File(None)
):
    global last_generated_result
    
    # Parse files
    schema_text = await parse_file_content(schema_file)
    data_text = await parse_file_content(sample_data_file) if sample_data_file else ""
    logs_text = await parse_file_content(logs_file) if logs_file else ""
    
    # Generate description
    result = ai_service.generate_description(schema_text, data_text, logs_text)
    
    # Store for export
    last_generated_result = result
    
    return JSONResponse(result)

@app.get("/api/export/json")
async def export_json():
    return JSONResponse(last_generated_result, headers={"Content-Disposition": "attachment; filename=metadata.json"})

@app.get("/api/export/xml")
async def export_xml():
    # Simple XML conversion
    root = ET.Element("metadata")
    
    overview = ET.SubElement(root, "overview")
    overview.text = last_generated_result.get("overview", "")
    
    # Add more fields as needed...
    # For hackathon speed, just dumping the overview and a few key fields
    
    xml_str = ET.tostring(root, encoding="utf-8", method="xml")
    return Response(content=xml_str, media_type="application/xml", headers={"Content-Disposition": "attachment; filename=metadata.xml"})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
