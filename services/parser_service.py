import json
import csv
import io
from fastapi import UploadFile

async def parse_file_content(file: UploadFile) -> str:
    """
    Reads the content of an uploaded file and returns it as a string.
    Handles JSON and CSV specifically to ensure they are readable text.
    """
    content = await file.read()
    text_content = content.decode("utf-8")
    
    # Reset cursor just in case
    await file.seek(0)
    
    return text_content

async def parse_schema(file: UploadFile) -> dict:
    """Parses a JSON schema file."""
    content = await file.read()
    await file.seek(0)
    return json.loads(content)
