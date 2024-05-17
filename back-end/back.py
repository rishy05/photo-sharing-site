from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import os
import shutil
import json

from user import cut_user
from photographer import cut_photograph, cut_photograph_opt
from sub import check_submit, check_submit_opt
from purg import pur

app = Flask(__name__)

cors = CORS(app)
app.config["UPLOAD_FOLDER_U"] = "people_temp"
app.config["UPLOAD_FOLDER_P"] = "photograph_up_temp"

os.makedirs(app.config["UPLOAD_FOLDER_P"], exist_ok=True)
os.makedirs(app.config["UPLOAD_FOLDER_U"], exist_ok=True)

app.config["UPLOAD_FOLDER_UU"] = "people"
app.config["UPLOAD_FOLDER_PP"] = "photograph_up"

os.makedirs(app.config["UPLOAD_FOLDER_PP"], exist_ok=True)
os.makedirs(app.config["UPLOAD_FOLDER_UU"], exist_ok=True)


@app.route("/photographer", methods=["POST"])
def photo_file():
    files = request.files.getlist("file")

    if len(files) == 0:
        return jsonify({"error": "No files selected"})

    for file in files:
        filename = file.filename
        print(filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER_P"], filename))
        print(f"File saved: {filename}")
        cut_photograph_opt()

    check_submit_opt()
    print("Checked successfully")

    return jsonify({"message": f"{len(files)} file(s) received successfully"})


@app.route("/user", methods=["POST"])
def user_file():
    data = {}

    files = request.files.getlist("file")
    maill = request.form.get("email")
    namee = request.form.get("name")

    data[str(namee)] = [files, maill, namee]
    print(data)

    print(
        files,
    )

    ff = open("data.json", "r")
    existing = json.loads(ff.read())
    ff.close()
    print(existing)
    existing[str(namee)] = [f"{namee}.jpg", maill, namee]
    print(existing)
    ff.close()
    with open("data.json", "w") as fw:
        fw.write(json.dumps(existing))
    fw.close()

    if len(files) == 0:
        return jsonify({"error": "No files selected"})

    for file in files:
        pathhh = f"""{app.config["UPLOAD_FOLDER_U"]}"""
        filename = f"{data[namee][-1]}_o.jpg"
        print(filename)
        file.save(os.path.join(pathhh, filename))
        print(f"File saved: {filename}")
        cut_user(namee, filename)

    return jsonify({"message": f"{len(files)} file(s) received successfully"})


@app.route("/purge", methods=["GET"])
def purge():
    print("Purge clicked")
    pur("people")
    pur("people_temp")
    pur("photograph_up")
    pur("Photograph_up_temp")
    print("Purged successfully")
    return jsonify({"message": "purged successfully"})


@app.route("/submit", methods=["GET"])
def sub():
    check_submit()
    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
