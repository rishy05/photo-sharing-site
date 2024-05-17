from retinaface import RetinaFace
import os
from pprint import pprint
from PIL import Image


def cut_photograph_opt():
    for k in os.listdir("photograph_up_temp"):
        resp = RetinaFace.detect_faces(f"photograph_up_temp/{str(k)}")
        face_coor = []
        pprint(resp)
        image = Image.open(f".\photograph_up_temp\{k}")
        for i in range(1, len(resp) + 1):
            face_coor.append(resp[f"face_{i}"]["facial_area"])

            y1 = face_coor[i - 1][1]
            x1 = face_coor[i - 1][0]
            y2 = face_coor[i - 1][3]
            x2 = face_coor[i - 1][2]

            dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
            if dis > 95:
                cropped_image = image.crop((x1, y1, x2, y2))
                output_folder = f"photograph_up/{k}"

                os.makedirs(output_folder, exist_ok=True)

                output_path = os.path.join(output_folder, f"face{i}.jpg")
                cropped_image.save(f"{output_folder}/face_p_{i}{k.split('.')[0]}.jpg")


def cut_photograph():

    for k in os.listdir("photograph_up_temp"):
        resp = RetinaFace.detect_faces(f"photograph_up_temp/{str(k)}")
        face_coor = []
        pprint(resp)
        image = Image.open(f".\photograph_up_temp\{k}")
        for i in range(1, len(resp) + 1):
            face_coor.append(resp[f"face_{i}"]["facial_area"])

            y1 = face_coor[i - 1][1]
            x1 = face_coor[i - 1][0]
            y2 = face_coor[i - 1][3]
            x2 = face_coor[i - 1][2]

            cropped_image = image.crop((x1, y1, x2, y2))
            output_folder = f"photograph_up/{k}"

            os.makedirs(output_folder, exist_ok=True)

            output_path = os.path.join(output_folder, f"face{i}.jpg")
            cropped_image.save(f"{output_folder}/face_p_{i}{k.split('.')[0]}.jpg")
