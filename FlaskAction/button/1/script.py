import os
from git import Repo


if __name__ == '__main__':

    repo_path = '../'
    
    repo = Repo(repo_path)
    for f in os.listdir(repo_path):
        print(f)
    origin = repo.remote(name='origin')
    
    origin.pull()
    # print(repo.git.status())
    repo.git.add('*')
    repo.index.commit('git push through LOUPEDECK')
    origin.push()