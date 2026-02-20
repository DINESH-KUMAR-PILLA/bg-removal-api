from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove, new_session
import os

app = FastAPI()

# ✅ ADD THIS CORS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# lightweight model
session = new_session(model_name="u2netp")

@app.get("/")
def root():
    return {"message": "BG Removal API running 🚀"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes, session=session)
    return Response(content=output_bytes, media_type="image/png")