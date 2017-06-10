from github import Github
import base64
import json
import os

GH = Github()


class RepositoryHelper(object):
    instace = 0

    def __init__(self, repo_name, path):
        super(RepositoryHelper, self).__init__()
        self.repo_name = str(repo_name)
        self.path = str(path)
        self.repo = GH.get_repo(self.repo_name)
        RepositoryHelper.instace += 1

    def get_file_content(self):
        file_content = self.repo.get_file_contents(self.path, "master")
        return base64.b64decode(file_content.content).decode('UTF-8')

    def save_to_file(self):

        output_path = 'output/' + self.repo_name.replace("/", "__") + '.yml'

        # Ignore if file exists
        if os.path.isfile(output_path):
            print str(RepositoryHelper.instace) + " skipped: " + self.repo_name
        else:
            f = open(output_path, 'w')
            f.write(self.get_file_content())
            f.close()
            print str(RepositoryHelper.instace) + " " + self.repo_name + ": processed"

    def __str__(self):
        return super(RepositoryHelper, self).__str__()


repositories = open('resultado-compilado-sem-virgula.json', 'r').read().split('\n')

for repo in repositories:
    repoJson = data = json.loads(repo)
    repository = RepositoryHelper(repoJson['repo_name'], repoJson['path'])
    repository.save_to_file()