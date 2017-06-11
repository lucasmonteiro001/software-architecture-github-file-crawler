from github import Github, enable_console_debug_logging
import base64
import json
import os
import hashlib

enable_console_debug_logging()

GH = Github()


class RepositoryHelper(object):
    instance = 0

    def __init__(self, repo_name, path):
        super(RepositoryHelper, self).__init__()
        self.repo_name = str(repo_name)
        self.path = str(path)
        self.repo = GH.get_repo(self.repo_name)
        RepositoryHelper.instance += 1

    def get_file_content(self):
        file_content = self.repo.get_file_contents(self.path, "master")
        return str(base64.b64decode(file_content.content).decode('UTF-8'))

    def save_to_file(self):

        hashed_path = hashlib.md5(self.path).hexdigest()

        output_path = 'output/' + self.repo_name.replace("/", "__") + "___" + hashed_path + '.yml'

        # Ignore if file exists
        if os.path.isfile(output_path):
            print str(RepositoryHelper.instance) + " [skipped]: " + self.repo_name
        else:
            file_content = self.get_file_content()
            if file_content == "":
                print str(RepositoryHelper.instance) + " [empty]: " + self.repo_name
            else:
                print str(RepositoryHelper.instance) + " [saved]: " + self.repo_name

            f = open(output_path, 'w')
            f.write(file_content)
            f.close()

    def __str__(self):
        return super(RepositoryHelper, self).__str__()


repositories = open('resultado-compilado-sem-virgula.json', 'r').read().split('\n')

for repo in repositories:
    try:
        repoJson = data = json.loads(repo)
        repository = RepositoryHelper(repoJson['repo_name'], repoJson['path'])
        repository.save_to_file()
    except Exception:
        pass
