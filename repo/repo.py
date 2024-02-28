# repo.py: command line tool for managing a set of Github repositories
import os
import sys
import yaml

class RepoMgr:
    def __init__(self, fn):
        dir_name = os.path.dirname(__file__)
        fn = os.path.join(dir_name, fn)

        with open(fn, "r") as f:
            data = yaml.safe_load(f)
            self.repos = data["repos"]

            # sort by key
            self.repos = dict(sorted(self.repos.items()))

            if "nt" in os.name:
                self.github_dir = data["github_dir"]["windows"]
            else:
                self.github_dir = data["github_dir"]["linux"]

        self.set_commands([])

    def print_items(self, items):
        print("\n  {:20}\t{:>16}\t{:60}\t{:}".format("NAME", "SIZE", "URL", "DESCRIPTION"))

        for rd in items:
            installed = "yes" if rd["installed"] else "no"
            print("  {:20}\t{:16,}\t{:60}\t{:}".format(rd["name"], rd["size"], rd["url"], rd["desc"]))

    def update_entry(self, repo, update_size=False):
        '''
        update fields:
            - installed: True if the repo is installed
            - dir: the directory of the repo
            - conda: the conda environment to use
        '''
        rd = self.repos[repo]
        url = rd["url"]
        dir_name = rd["dir"] if "dir" in rd else os.path.basename(url)
        conda = rd["conda"] if "conda" in rd else repo

        repo_dir = self.github_dir + "/" + dir_name

        rd["name"] = repo
        rd["installed"] = os.path.exists(repo_dir)
        rd["dir"] = repo_dir
        rd["conda"] = conda

        if update_size:
            size = self.get_dir_size(repo_dir)
            rd["size"] = size
        else:
            rd["size"] = None

    def get_dir_size(self, dir_name):
        size = 0

        for path, dirs, files in os.walk(dir_name):
            for f in files:
                fp = os.path.join(path, f)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)

        return size

    def list_repos(self, filter):
        print_items = []
        for repo, rd in self.repos.items():
            self.update_entry(repo, update_size=True)

            show = True
            if filter:
                text = repo + str(rd["installed"]) + rd["url"] + rd["desc"]
                if not filter.lower() in text.lower():
                    show = False

            if show:
                print_items.append(rd)

        self.print_items(print_items)

    def go(self, cmd):
        if cmd not in self.repos:
            print("repo {} not found".format(cmd))
            return

        self.update_entry(cmd)
        repo = self.repos[cmd]
        conda = repo["conda"]

        url = repo["url"]
        repo_dir = repo["dir"]

        # create a batch file to affect conda environment
        cmds = []
        cmds.append("call conda deactivate")
        cmds.append("call conda activate " + conda)
        cmds.append("cd /d " + repo_dir)
        self.set_commands(cmds)

    def install_repo(self, cmd):
        if cmd not in self.repos:
            print("repo {} not found".format(cmd))
            return

        self.update_entry(cmd)
        repo = self.repos[cmd]
        url = repo["url"]
        repo_dir = repo["dir"]
        size = repo["size"]
        conda = repo["conda"]

        if size:
            print("repo {} is already installed".format(cmd))
            return

        if not os.path.exists(repo_dir):
            os.system("git clone " + url + " " + repo_dir)

            fn_create_conda = "{}/create_conda.bat".format(repo_dir)

            cmds = []
            cmds.append("cd /d " + repo_dir)
            cmds.append(fn_create_conda)
            cmds.append("repo")    # echo newly installed repo
            # cmds.append("call conda deactivate")
            # cmds.append("call conda activate " + conda)
            self.set_commands(cmds)

        # else:
        #     os.system("git -C " + repo_dir + " pull")

    def set_commands(self, cmds):
        fn = "{}/repo_commands.bat".format(self.github_dir)
        with open(fn, "w") as f:
            f.write("@echo off\n")

            for cmd in cmds:
                f.write(cmd + "\n")

    def current(self):
        cwd = os.getcwd().lower()
        ghd = os.path.abspath(self.github_dir).lower()

        if cwd.startswith(ghd):
            repo = cwd[len(ghd)+1:].lower()
            if "\\" in repo or "/" in repo:
                repo = os.path.dirname(repo)

            self.update_entry(repo, update_size=True)

            rd = self.repos[repo]
            self.print_items([rd])

        else:
            print("not in a repo")


        #os.system("git rev-parse --show-toplevel")

    def help(self):
        print("usage:")
        print("  repo                  (show info about current repo)")
        print("  repo go <name>        (change to the specified repo)")
        print("  repo install <name>   (install the specified repo)")
        print("  repo list [filter]    (show info about all/matching repos)")
        print("  repo help             (show this help information)")
        print("  repo <name>           (shortcut for go <name>)")


def command(cmd, cmd2):

    repo_mgr = RepoMgr("repos.yaml")

    if not cmd:
        repo_mgr.current()

    elif cmd == "list":
        repo_mgr.list_repos(cmd2)

    elif cmd == "install":
        repo_mgr.install_repo(cmd2)

    elif cmd == "help":
        repo_mgr.help()

    else:
        if cmd == "go":
            cmd = cmd2
        repo_mgr.go(cmd)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    cmd2 = sys.argv[2] if len(sys.argv) > 2 else ""

    command(cmd, cmd2)
    #command("", "")