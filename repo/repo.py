# repo.py: command line tool for managing a set of Github repositories
import os
import sys
import yaml

'''
This tool depends on the following environment variables:
    - GITHUB_DIR            (the parent directory of all the github repos )
    - CONDA3_DIR            (the ../anaconda3 directory)
'''

class RepoMgr:
    def __init__(self, fn):
        dir_name = os.path.dirname(__file__)
        fn = os.path.join(dir_name, fn)

        with open(fn, "r") as f:
            data = yaml.safe_load(f)
            self.repos = data["repos"]

            # sort by key
            self.repos = dict(sorted(self.repos.items()))

            self.github_dir = os.path.expandvars("$GITHUB_DIR")

        self.set_commands([])

    def print_items(self, items, show_sizes=False):

        if show_sizes:
            print("\n  {:20}\t{:>16}\t{:>16}\t{:60}\t{:}".format("NAME", "REPO SIZE", "CONDA SIZE", "URL", "DESCRIPTION"))
        else:
            print("\n  {:20}\t{:60}\t{:}".format("NAME", "URL", "DESCRIPTION"))

        for rd in items:
            installed = "yes" if rd["installed"] else "no"
            if show_sizes:
                print("  {:20}\t{:16,}\t{:16,}\t{:60}\t{:}".format(rd["name"], rd["file_size"], rd["conda_size"], rd["url"], rd["desc"]))
            else:
                print("  {:20}\t{:60}\t{:}".format(rd["name"], rd["url"], rd["desc"]))

    def update_entry(self, repo, update_size=False):
        '''
        update fields:
            - installed: True if the repo is installed
            - dir: the directory of the repo
            - conda: the conda environment to use
        '''
        rd = self.repos[repo]
        url = rd["url"]
        simple_dir = rd["dir"] if "dir" in rd else os.path.basename(url)
        conda = rd["conda"] if "conda" in rd else repo

        repo_dir = self.github_dir + "/" + simple_dir

        rd["name"] = repo
        rd["installed"] = os.path.exists(repo_dir)
        rd["dir"] = simple_dir
        rd["conda"] = conda

        if update_size:
            conda_path = os.path.dirname(os.path.expandvars("$CONDA3_DIR")) + "/envs/" + conda
            #print(conda_path)
            conda_path = os.path.abspath(conda_path)

            file_size = self.get_dir_size(repo_dir)
            conda_size = self.get_dir_size(conda_path)

            rd["file_size"] = file_size
            rd["conda_size"] = conda_size
        else:
            rd["file_size"] = None
            rd["conda_size"] = None

    def get_dir_size(self, dir_name):
        size = 0

        for path, dirs, files in os.walk(dir_name):
            for f in files:
                fp = os.path.join(path, f)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)

        return size

    def list_repos(self, filter, show_sizes=False):
        print_items = []
        for repo, rd in self.repos.items():
            self.update_entry(repo, update_size=False)

            show = True
            if filter:
                text = repo + str(rd["installed"]) + rd["url"] + rd["desc"]
                if not filter.lower() in text.lower():
                    show = False

            if show:
                self.update_entry(repo, update_size=show_sizes)
                print_items.append(rd)

        self.print_items(print_items, show_sizes)

    def go(self, cmd):
        if cmd not in self.repos:
            print("repo {} not found".format(cmd))
            return

        self.update_entry(cmd, update_size=False)
        repo = self.repos[cmd]
        conda = repo["conda"]

        repo_dir = self.github_dir + "/" + repo["dir"]

        # create a batch file to affect conda environment
        cmds = []
        call = "call " if "nt" in os.name else ""
        cmds.append("{}conda deactivate".format(call))
        cmds.append("{}conda activate {}".format(call, conda))

        if "nt" in os.name:
            cmds.append("cd /d " + repo_dir)
            if "env_vars" in repo:
                for var, value in repo["env_vars"].items():
                    value = os.path.expandvars(value)
                    cmds.append("set " + var + "=" + value)
        else:
            cmds.append("cd " + repo_dir)

        
        self.set_commands(cmds)

    def install_repo(self, cmd):
        if cmd not in self.repos:
            print("repo {} not found".format(cmd))
            return

        self.update_entry(cmd)
        repo = self.repos[cmd]
        url = repo["url"]
        repo_dir = self.github_dir + "/" + repo["dir"]
        size = repo["file_size"]
        conda = repo["conda"]
        branch = repo["branch"] if "branch" in repo else None

        if size:
            print("repo {} is already installed".format(cmd))
            return

        if not os.path.exists(repo_dir):
            clone_cmd = "git clone " + url + " " + repo_dir
            if branch:
                clone_cmd += " --branch " + branch

            print(clone_cmd)

            os.system(clone_cmd)

            if "nt" in os.name:
                fn_create_conda = "{}/create_conda.bat".format(repo_dir)
            else:
                fn_create_conda = "source {}/create_conda.sh".format(repo_dir)

            cmds = []
            if "nt" in os.name:
                cmds.append("cd /d " + repo_dir)
            else:
                cmds.append("cd " + repo_dir)
            cmds.append(fn_create_conda)
            cmds.append("rt")    # echo newly installed repo
            self.set_commands(cmds)

    def set_commands(self, cmds):
        ext = "bat" if "nt" in os.name else "sh"
        fn = "{}/repo_commands.{}".format(self.github_dir, ext)
        with open(fn, "w") as f:
            if ext == "bat":
                f.write("@echo off\n")

            for cmd in cmds:
                f.write(cmd + "\n")

    def get_current_repo_entry(self, update_sizes=False):
        cwd = os.path.abspath(os.getcwd())
        ghd = os.path.abspath(self.github_dir)
        repo_entry = None

        # print("cwd: {}, ghd: {}".format(cwd, ghd))
        # print(self.repos)

        if cwd.lower().startswith(ghd.lower()):
            repo_name = cwd[len(ghd)+1:]
            if "\\" in repo_name or "/" in repo_name:
                repo_name = os.path.dirname(repo_name)
            
            #repo = os.path.abspath(ghd + "/" + repo)
            #print(repo)

            for key, entry in self.repos.items():
                self.update_entry(key, update_size=update_sizes)
                #print(entry["dir"])

                if repo_name ==entry["dir"]:
                    repo_entry = entry
                    break

        return repo_entry

    def current(self):
        repo_entry = self.get_current_repo_entry(update_sizes=True)
        if repo_entry:
            self.print_items([repo_entry], show_sizes=True)

        else:
            print("not currently in a known repo")

    def help(self):
        print("usage:")
        print("  repo                  (show info about current repo)")
        print("  repo go <name>        (change to the specified repo)")
        print("  repo install <name>   (install the specified repo)")
        print("  repo list [filter]    (show info about all/matching repos)")
        print("  repo sizes [filter]   (show sizes of all/matching repos)")
        print("  repo username <name>  (associate the specified Github username with this repo) ")
        print("  repo help             (show this help information)")
        print("  repo <name>           (shortcut for go <name>)")

    def associate_username(self, username):
        if not username:
            print("username is required")
            return

        repo_entry = self.get_current_repo_entry()
        if repo_entry:
            url = repo_entry["url"]
            url = url.replace("://", "://" + username + "@")
            #cmd = "git remote set-url origin https://{}@github.com/MSRDL/TPX-Datasets".format(username)
            cmd = "git remote set-url origin {}".format(url)
            print(cmd)
            os.system(cmd)

        else:
            print("not currently in a known repo")

def command(cmd, cmd2):

    repo_mgr = RepoMgr("repos.yaml")

    if not cmd:
        repo_mgr.current()

    elif cmd == "list":
        repo_mgr.list_repos(cmd2)

    elif cmd == "sizes":
        repo_mgr.list_repos(cmd2, True)

    elif cmd == "install":
        repo_mgr.install_repo(cmd2)

    elif cmd == "username":
        repo_mgr.associate_username(cmd2)

    elif cmd == "help":
        repo_mgr.help()

    else:
        if cmd == "go":
            cmd = cmd2
        repo_mgr.go(cmd)

if __name__ == "__main__":
    #print(sys.argv)

    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    cmd2 = sys.argv[2] if len(sys.argv) > 2 else ""

    #command(cmd, cmd2)
    command("username", "rfernand2")
    #command("", "")
