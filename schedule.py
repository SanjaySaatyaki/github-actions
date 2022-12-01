from actions_toolkit import core
from actions_toolkit import github
from actions_toolkit.github import Context, get_octokit


my_token = core.get_input('MYTOKEN',required=True)
print(my_token)
octokit = get_octokit(my_token)

context = Context()

user_repo = f'{context.repo.owner}/{context.repo.repo}'
repo = octokit.rest.get_repo(user_repo)
print(repo.get_commits)
