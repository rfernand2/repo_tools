# repo_tools
Tools for installing/switching GitHub repos and configuring new machines.

On a new or partially configured machine:

    1. install repo tools
        a. ensure git is installed
        b. create a github directory on a drive
        c. cd to the github directory
        d. git clone https://github.com/rfernand2/repo_tools

    2. for windows:   run windows/config_machine.bat
       for linux:     sh linux/config_machine.sh

    3. if desired, install XT:
        for windows:  install_xt.bat  
        for linux:    sh install_xt.sh

    You are now ready to use:
        repo
        xt

# TODO
	- add command to support associating a userid with an RT name; under the covers, it does this:
		git remote set-url origin https://rfernand2@github.com/MSRDL/TPX-Datasets

Also, you can download the az-pim_windows.exe tool (needed for the elevate command) from: 
	https://github.com/demoray/azure-pim-cli/releases

