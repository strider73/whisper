from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from fastapi.responses import JSONResponse, RedirectResponse
import whisper
import torch
from tempfile import NamedTemporaryFile

# Check if CUDA (GPU) is available, otherwise use CPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load Whisper model
model = whisper.load_model("base", device=DEVICE)

# Initialize FastAPI app
app = FastAPI()

@app.post("/whisper")
async def handler(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="Only one file is allowed")

    results = []

    for file in files:
        with NamedTemporaryFile(delete=True) as temp:
            with open(temp.name, "wb") as temp_file:
                temp_file.write(await file.read())

            # Perform speech recognition
            result = model.transcribe(temp.name)

            results.append({
                "filename": file.filename,
                "transcript": result["text"]
            })

    return JSONResponse(content={"results": results})

@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"
