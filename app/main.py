from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="Notes API")

notes = []

@app.get("/")
def root():
    return {"message": "Hello from FastAPI in Docker", "time": datetime.now().isoformat()}

@app.get("/health")
def health():
    return{"status": "OK"}

@app.get("/notes")
def list_notes():
    return notes

@app.post("/notes")
def add_note(text: str):
    note = {"id": len(notes) + 1, "text": text}
    notes.append(note)
    return note