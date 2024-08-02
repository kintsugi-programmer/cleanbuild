from flask import Flask, render_template, request, redirect
import os
import csv
from datetime import datetime
import requests
import json

template_file = 'data/portfolio.js'
user_data_file = 'data/submissions.csv'


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-site')
def form():
    return render_template('create-site.html')

@app.route('/submit', methods=['POST'])
def submit():
    homepage = request.form.get('homepage')
    title = request.form.get('title')
    name = request.form.get('name')
    role = request.form.get('role')
    description = request.form.get('description')
    resume = request.form.get('resume')
    github = request.form.get('github')
    linkedin = request.form.get('linkedin')
    skills = request.form.get('skills')
    email = request.form.get('email')

    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    projects = []
    project_index = 0
    while True:
        project_name = request.form.get(f'project-name-{project_index}')
        if not project_name:
            break
        project_description = request.form.get(f'project-description-{project_index}')
        project_stack = request.form.get(f'project-stack-{project_index}')
        project_source_code = request.form.get(f'project-sourceCode-{project_index}')
        project_live_preview = request.form.get(f'project-livePreview-{project_index}')
        projects.append({
            'name': project_name,
            'description': project_description,
            'stack': project_stack.split(','),
            'sourceCode': project_source_code,
            'livePreview': project_live_preview
        })
        project_index += 1
    
    project_string = ',\n'.join([f"""
    {{
        name: '{project['name']}',
        description: '{project['description']}',
        stack: {json.dumps(project['stack'])},
        sourceCode: '{project['sourceCode']}',
        livePreview: '{project['livePreview']}'
    }}""" for project in projects])

    skills_string = ', '.join([f"'{skill.strip()}'" for skill in skills.split(',')])

    with open(user_data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip_address, timestamp, homepage, title, name, role, description, resume, github, linkedin, skills, email, user_agent, projects])

    with open(template_file, 'r') as file:
        data = file.read()
        data = data.replace('dtx000', homepage)
        data = data.replace('dtx001', title)
        data = data.replace('dtx002', name)
        data = data.replace('dtx003', role)
        data = data.replace('dtx004', description)
        data = data.replace('dtx005', resume)
        data = data.replace('dtx006', linkedin)
        data = data.replace('dtx007', github)
        data = data.replace('dtx008', skills_string)
        data = data.replace('dtx009', email)
        data = data.replace('dtx010', project_string)

    with open(template_file, 'w') as file:
        file.write(data)

    return render_template('finished.html')

@app.route('/finished')
def finished():
    return render_template('finished.html')

if __name__ == '__main__':
    if not os.path.isfile(user_data_file):
        with open(user_data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['IP Address', 'Timestamp', 'Homepage', 'Title', 'Name', 'Role', 'Description', 'Resume', 'Github', 'Linkedin', 'Skills', 'Email', 'User Agent', 'Projects'])

    if not os.path.exists('data'):
        os.makedirs('data')

    app.run(debug=True)