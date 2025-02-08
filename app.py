from flask import Flask, render_template, request, redirect, flash
from google.cloud import storage
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# GCS bucket name
BUCKET_NAME = "sales-data-bucket-13"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file part")
        return redirect("/")

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return redirect("/")

    if file:
        # Upload the file to GCS
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(file.filename)
        blob.upload_from_string(file.read(), content_type=file.content_type)

        flash("File uploaded successfully!")
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)