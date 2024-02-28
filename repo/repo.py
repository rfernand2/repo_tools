# repo.py: command line tool for managing a set of Github repositories
imort os
import yaml

fn = "repo.yaml"
with open(fn, "r") as f:
    text = f.read()
    data = yaml.load(text)

def list_repos():
    for repo in data["repos"]:
        print(repo)

list_repos()
