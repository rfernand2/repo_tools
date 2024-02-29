# add things to path
# echo 'export PATH=$PATH:~/github/repo_tools' >> ~/.bashrc

# add commands
echo "alias tools='cd ~/github/repo_tools'" >> ~/.bashrc
echo "alias gh='cd ~/github'" >> ~/.bashrc
echo "repo() { python ~/github/repo_tools/repo/repo.py \"\$@\"; . ~/github/repo_commands.sh }" >> ~/.bashrc
