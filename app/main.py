from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from models.model import GPT2PPL
import os

app = FastAPI()

model = GPT2PPL()

ACCESS_COUNTER = 0

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/status/")
async def status():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    global ACCESS_COUNTER
    ACCESS_COUNTER += 1
    return {"message": "I am up and running! ",
            "time": current_time,
            "access_counter": ACCESS_COUNTER}

@app.post("/scan/file/")
async def scan_file(file: UploadFile = File(...)):

    if not os.path.exists("temp"):
        os.makedirs("temp")

    # Save the uploaded file
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Load and process the text
    text = ""
    if file.filename.endswith(".txt"):
        with open(file_location, "r") as f:
            text = f.read()
    elif file.filename.endswith(".docx"):
        import docx
        doc = docx.Document(file_location)
        text = "\n".join([p.text for p in doc.paragraphs])

    result, ppls, sentences = model(text)

    # Here, you would pass the text to your GPTZero model
    # For now, return dummy output
    analysis = {"status": "OK",
        "text_length": len(text),
        "result": result,
        "parsed_ppls": ppls,
        "parsed_sentences": sentences}

    # Clean up temporary file
    os.remove(file_location)

    return JSONResponse(content=analysis)

@app.post("/scan/text/")
async def scan_text(request: Request):
    data = await request.json()
    text = data.get("text", "")

    result, ppls, sentences = model(text)

    analysis = {"status": "OK",
        "text_length": len(text),
        "result": result,
        "parsed_ppls": ppls,
        "parsed_sentences": sentences}
    return JSONResponse(content=analysis)
