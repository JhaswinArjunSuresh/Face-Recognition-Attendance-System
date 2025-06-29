import face_recognition
import numpy as np
from typing import List

registered_encodings = []
registered_names = []

def register_face(name: str, image_bytes: bytes) -> bool:
    image = face_recognition.load_image_file(image_bytes)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return False
    registered_encodings.append(encodings[0])
    registered_names.append(name)
    return True

def recognize_faces(image_bytes: bytes, tolerance=0.6) -> List[str]:
    image = face_recognition.load_image_file(image_bytes)
    unknown_encodings = face_recognition.face_encodings(image)
    recognized = []
    for unknown_encoding in unknown_encodings:
        matches = face_recognition.compare_faces(registered_encodings, unknown_encoding, tolerance)
        face_distances = face_recognition.face_distance(registered_encodings, unknown_encoding)
        best_match_index = np.argmin(face_distances) if face_distances.size > 0 else None
        if best_match_index is not None and matches[best_match_index]:
            recognized.append(registered_names[best_match_index])
    return recognized

