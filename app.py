from __future__ import annotations

import os
import tempfile
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, send_file, url_for
from pdf2docx import Converter
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"pdf"}
MAX_CONTENT_LENGTH = 20 * 1024 * 1024

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/convert")
def convert_pdf():
    if "pdf_file" not in request.files:
        flash("Nenhum arquivo enviado.")
        return redirect(url_for("index"))

    uploaded_file = request.files["pdf_file"]
    if uploaded_file.filename == "":
        flash("Selecione um arquivo PDF para converter.")
        return redirect(url_for("index"))

    if not allowed_file(uploaded_file.filename):
        flash("Formato inválido. Envie um arquivo PDF.")
        return redirect(url_for("index"))

    safe_name = secure_filename(uploaded_file.filename)
    base_name = Path(safe_name).stem

    with tempfile.TemporaryDirectory() as temp_dir:
        input_path = Path(temp_dir) / safe_name
        output_path = Path(temp_dir) / f"{base_name}.docx"
        uploaded_file.save(input_path)

        converter = Converter(str(input_path))
        try:
            converter.convert(str(output_path), start=0, end=None)
        finally:
            converter.close()

        return send_file(
            output_path,
            as_attachment=True,
            download_name=f"{base_name}.docx",
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
