from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from .face_utils import register_face, recognize_faces

app = FastAPI()

attendance = set()

@app.post("/register")
async def register(name: str = Form(...), file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    image_bytes = await file.read()
    success = register_face(name, image_bytes)
    if not success:
        raise HTTPException(status_code=400, detail="No face found in image")
    return {"status": f"Registered {name} successfully"}

@app.post("/attendance")
async def mark_attendance(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    image_bytes = await file.read()
    names = recognize_faces(image_bytes)
    if not names:
        return {"status": "No recognized faces"}
    for name in names:
        attendance.add(name)
    return {"recognized": names, "attendance_count": len(attendance)}

@app.get("/attendance")
def get_attendance():
    return {"attendance": list(attendance)}

@app.get("/health")
def health():
    return {"status": "ok"}

