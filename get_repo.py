import subprocess
import csv
#git clone git@github.com:snyk/snyk-ls.git
git_prefix = 'https://github.atl.pindrop.net/'

py_projects = []  # List for Python projects
go_projects = []  # List for Go projects
js_projects = []  # List for JavaScript projects
#all_projects = (py_projects,go_projects,js_projects)
snyk = ('ls', '-la')

with open("Pytest-csv.csv", "r") as data_file:
    csv_data = csv.reader(data_file)
    header = next(csv_data)  # Skip header

    for line in csv_data:
        #repo_url = git_prefix + line[1] + ".git"
        if line[2] == "py":
            py_projects.append(line[1]+line[3]+".git")  # Store Python projects
        elif line[2] == "go":
            go_projects.append(line[1])  # Store Go projects
        elif line[2] == "js":
            js_projects.append(line[1])  # Store JavaScript projects
''' Print results
print("Python Projects:", py_projects)
print("Go Projects:", go_projects, "- These are Go projects")
print("JavaScript Projects:", js_projects)

for i in py_projects:
    print(py_projects,pindrop_git)            
'''
def clone_repos(project_list):
    for repo in project_list:
        print(f"Cloning:{repo}")
        #subprocess.run(["git clone", git_prefix+repo])  # Use git clone command to download the repo
        print("git clone",git_prefix+repo)
    subprocess.run(snyk)


# Clone projects for each type
clone_repos(py_projects)
# clone_repos(go_projects)
# clone_repos(js_projects)

