import requests
from datetime import datetime as dt
import json


url = "http://127.0.0.1:8000/api"

def get_exp_nb(dob_str):
    now_str = dt.strftime(dt.utcnow(), '%Y-%m-%d')
    return int(now_str[:4]) - int(dob_str[:4]) - int(dob_str[5:] > now_str[5:])


portfolio = requests.get('{}/portfolio/1'.format(url)).json()
job_titles = requests.get('{}/jobs_title/?portfolio=1'.format(url)).json()['results']
languages = requests.get('{}/languages/'.format(url)).json()['results']
skills = requests.get('{}/skills/'.format(url)).json()['results']
educations = requests.get('{}/educations/'.format(url)).json()['results']
experience = requests.get('{}/experiences/'.format(url)).json()['results']
projects_temp = requests.get('{}/projects/'.format(url)).json()['results']
projects = []

nb_projects = len(projects)
nb_exp = get_exp_nb(portfolio['dev_start'])

for project in projects_temp:
    project_type = project["project_type"]
    type = requests.get('{}/project_types/{}'.format(url,project["project_type"])).json()


    uploads_temp = []
    uploads = requests.get('{}/uploads/?project=1'.format(url)).json()['results']
    for upload in uploads:
        uploads_temp.append(upload["image"])

    stacks_temp = []
    stacks = requests.get('{}/stacks/?project=1'.format(url)).json()['results']
    for stack in stacks:
        stacks_temp.append(stack['name'])
    

    projects.append(
        {
            'id' : project["id"],
            'name' : project["name"],
            'description' : project["description"],
            'client' : project["client"],
            'type' : type['name'],
            'stacks': stacks_temp,
            'images' : uploads_temp,
        }
    )

api = {
    'portfolio':portfolio,
    'job_titles':job_titles,
    'nb_projects':nb_projects,
    'nb_exp':nb_exp,
    'languages':languages,
    'skills':skills,
    'educations':educations,
    'experience':experience,
    'projects':projects

} 

with open("api.json", "w") as outfile:
    json.dump(api, outfile)