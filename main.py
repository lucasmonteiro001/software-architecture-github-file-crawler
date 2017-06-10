from github import Github
import base64
import json

GH = Github()


class RepositoryHelper(object):
    def __init__(self, repo_name, path):
        super(RepositoryHelper, self).__init__()
        self.repo_name = str(repo_name)
        self.path = str(path)
        self.repo = GH.get_repo(self.repo_name)

    def get_file_content(self):
        file_content = self.repo.get_file_contents(self.path, "master")
        return base64.b64decode(file_content.content).decode('UTF-8')

    def __str__(self):
        return super(RepositoryHelper, self).__str__()


repositories = open('resultado-compilado-sem-virgula.json', 'r').read().split('\n')

for repo in repositories:
    repoJson = data = json.loads(repo)
    repository = RepositoryHelper(repoJson['repo_name'], repoJson['path'])
    print repository.get_file_content()

exit()

g = Github()

repo = g.get_repo("thomasleveil/kontena")
file_contents = repo.get_file_contents("server/docker-compose.yml", "master")

print base64.b64decode(file_contents.content).decode('UTF-8')
