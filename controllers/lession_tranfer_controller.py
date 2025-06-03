from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from forms.lession_tranfer_form import UploadForm
import uuid
from config import Config
import os
from models.imgclassifier import ImageClassifier

def lession_transfer():
    form = UploadForm() 
    model=ImageClassifier()
    if form.validate_on_submit():
        file = request.files.get("file")
        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)

        class_name, confidence=model.predict(filepath)

        return render_template('transfer_result.html',
                               class_name=class_name,
                               confidence=confidence,
                               filename=filename
                               )

    return render_template('lession_transfer.html', form=form)