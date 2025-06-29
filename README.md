# 📸 Face Recognition Attendance System

Upload images to register faces and mark attendance by recognizing faces.

## Endpoints
- `POST /register` with form fields: `name` (string) and `file` (image) to register a face.
- `POST /attendance` with image file to mark attendance.
- `GET /attendance` to get list of attendees.
- `GET /health` for health check.

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

