# config our linux machine for repo_tools style of development
cat $GITHUB_DIR/repo_tools/linux/aliases.txt >> ~/.bashrc
source ~/.bashrc

# apply creds to box
$CONDA3_DIR/python $GITHUB_DIR/repo_tools/apply_creds_linux.python

# TODO: install minicode
# TODO: install VSCODE (when we have a UI)