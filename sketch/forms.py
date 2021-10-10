from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class ImageForm(FlaskForm):
    image_file = FileField('Upload picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Transform')
