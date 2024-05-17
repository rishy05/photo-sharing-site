import os
import json
from pprint import pprint

from compare import check_face
from g_mail import send_file, auth_mail
from drivee import drive_auth, cre_fol, up


def check_submit():
    drive_auth()
    print("SUBMIT BUTTON PRESSED")
    ff = open("data.json", "r")
    conn = json.loads(ff.read())
    ff.close()
    img = {}
    for i in os.listdir("people"):
        t = []

        for x in os.listdir(f"people\{i}"):
            for j in os.listdir("photograph_up"):

                for k in os.listdir(f"photograph_up\{j}"):

                    out = check_face(f"people\{i}\{x}", f"photograph_up\{j}\{k}")
                    if out == True:
                        print("MATCHED")
                        print(i, k, True)
                        fww = f"photograph_up_temp\{j}"
                        print(fww)
                        t.append(fww)
                    okk = []
                    [okk.append(lll) for lll in t if lll not in okk]
                    img[str(i)] = okk
    pprint(img)

    for kk in img.keys():
        print(kk)
        idd = cre_fol(kk, conn[kk][1])
        up(filess=img[kk], iid=idd)


def check_submit_opt():
    drive_auth()
    print("SUBMIT BUTTON PRESSED")
    ff = open("data.json", "r")
    conn = json.loads(ff.read())
    ff.close()
    img = {}
    for i in os.listdir("people"):
        t = []

        for x in os.listdir(f"people\{i}"):
            for j in os.listdir("photograph_up"):
                j_match = False

                for k in os.listdir(f"photograph_up\{j}"):

                    out = check_face(f"people\{i}\{x}", f"photograph_up\{j}\{k}")
                    if out == True:
                        print("MATCHED")
                        print(i, k, True)
                        fww = f"photograph_up_temp\{j}"
                        print(fww)
                        t.append(fww)

                        okk = []
                        [okk.append(lll) for lll in t if lll not in okk]
                        img[str(i)] = okk
                        j_match = True
                        os.remove(f"photograph_up\{j}\{k}")
                        break
                if j_match == True:
                    continue
    pprint(img)

    for kk in img.keys():
        print(kk)
        idd = cre_fol(kk, conn[kk][1])
        up(filess=img[kk], iid=idd)
