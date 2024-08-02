from flask import Flask, render_template, request, redirect, url_for, send_file
from forms import SiteForm
import zipfile
import os
from basher import run_bash_command

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_site', methods=['GET', 'POST'])
def create_site():
    form = SiteForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        # Save the HTML file
        file_path = os.path.join(UPLOAD_FOLDER, f'{title}.html')
        with open(file_path, 'w') as f:
            f.write(f"<html><head><title>{title}</title></head><body>{content}</body></html>")
        return redirect(url_for('download_zip'))
    return render_template('create_site.html', form=form)

@app.route('/download_zip')
def download_zip():
    zip_path = os.path.join(UPLOAD_FOLDER, 'website.zip')
    # Create a ZIP file excluding the zip itself
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(UPLOAD_FOLDER):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path != zip_path:
                    zipf.write(file_path, os.path.relpath(file_path, UPLOAD_FOLDER))
    return send_file(zip_path, as_attachment=True)

# welcome page
# build section
# cleanfolio starts 

# homepage link text
# title text
# Name
# role
# desc
# resume
# social links
# project
# skills
# email

if __name__ == '__main__':
    app.run(debug=True)
