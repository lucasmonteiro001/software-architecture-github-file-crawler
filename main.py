from github import Github
import base64

g = Github()

# repo = g.get_repo("yonglehou/ceryx")
# file_contents = repo.get_file_contents("docker-compose.yml", "master")

repo = g.get_repo("thomasleveil/kontena")
file_contents = repo.get_file_contents("server/docker-compose.yml", "master")

print base64.b64decode(file_contents.content).decode('UTF-8')

# for repo in g.get_user().get_repos():
#     print repo.name

