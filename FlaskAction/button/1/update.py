from git import Repo

repo_path = '../'
repo = Repo(repo_path)


def main_update():
        
    if repo.is_dirty(untracked_files=True):
        print("There are unstaged changes in the repository.")
        return "rickroll-roll.gif"
        return "exploded.jpg"
    else:
        print("There are no unstaged changes in the repository.")
        return "image.jpg"