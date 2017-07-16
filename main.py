from github import Github, enable_console_debug_logging
import base64
import json
import os
import hashlib
from datetime import datetime


# enable_console_debug_logging()

GH = Github("lmufmg", "senhagithub1!")
# GH = Github("lmmms", "senhagithub1!")
#GH = Github("lucasmonteiro001", "chemical3!")
#print GH.get_rate_limit().rate
# utc_time = datetime.utcfromtimestamp(GH.rate_limiting_resettime)
# print(utc_time.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)"))
#exit()


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

        #print GH.get_rate_limit().rate

    def save_repo_metadata_to_file(self):

        hashed_path = hashlib.md5(self.path).hexdigest()

        output_path = 'output_metadata/' + self.repo_name.replace("/", "__") + "___" + hashed_path + '.yml'

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
            f.write("%s,%s,%s" % (self.repo.language, self.repo.size, self.repo.stargazers_count))
            f.close()

        #print GH.get_rate_limit().rate

    def __str__(self):
        return super(RepositoryHelper, self).__str__()


repositories = open('resultado-compilado-sem-virgula.json', 'r').read().split('\n')

counter = 0

for repo in repositories:
    try:
        counter += 1

        if counter > 2230:
            repoJson = data = json.loads(repo)
            repository = RepositoryHelper(repoJson['repo_name'], repoJson['path'])
            # repository.save_to_file()
            repository.save_repo_metadata_to_file()
    except Exception:
        pass
