# repo_tools
Tools for installing/switching GitHub repos and configuring new machines.

On a new or partially configured machine:

    1. install repo tools
        a. ensure git is installed
        b. for LINUX, add the following line to: ~/.git-credentials

             https://rfernand2:CERT_GOES_HERE@github.com

        b. create a github directory on a drive
        c. cd to the github directory
        d. git clone https://github.com/rfernand2/repo_tools


    2. set various environment variables:
        a. add repo_tools directory to PATH
        b. add HOME to point to base of github, .models, .data subdirs
        c. add TOOLS_PYTHON to point to the location of your tools python interpreter

    3. install conda, vscode, etc:
        a. configure_machine.bat


    4. if desired, install XT:
        a. install_xt.bat   (adds to shared_xt conda env)
        b. add directory of XT (where xt) to PATH

    You are ready to use:
        repo
        xt

        
