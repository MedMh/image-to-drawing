from sketch import app
from sketch.forms import ImageForm
from flask import render_template, url_for
from sketch.picsManager import save_picture, image_to_sketch


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = ImageForm()
    if form.validate_on_submit():
        if form.image_file.data:
            pic_name, pic_path, source_name = save_picture(form.image_file.data, app)
            result = image_to_sketch(pic_name, pic_path, app)
            return render_template('home.html', form=form, source=source_name, result=result)
    return render_template('home.html', form=form)