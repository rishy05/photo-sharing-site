from retinaface import RetinaFace
from PIL import Image
from pprint import pprint
import os


def cut_user(fol, named):

    print(f"people_temp/{named}")
    resp = RetinaFace.detect_faces(f"people_temp/{named}")
    print("Detected")
    # pprint(resp)
    face_coor = []
    image = Image.open(f".\people_temp\{named}")
    for i in range(1, len(resp) + 1):
        face_coor.append(resp[f"face_{i}"]["facial_area"])

        y1 = face_coor[i - 1][1]
        x1 = face_coor[i - 1][0]
        y2 = face_coor[i - 1][3]
        x2 = face_coor[i - 1][2]
        cropped_image = image.crop((x1, y1, x2, y2))
        output_folder = f"people/{fol}"
        os.makedirs(output_folder, exist_ok=True)
        cropped_image.save(f"{output_folder}/{fol}_u_{i}.jpg")
