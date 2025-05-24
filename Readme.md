### Git Hidden Folder

There is a hidden folder called `.git` which tells you that our project is a git repo. 

To create it, we need to move to the folder and to run `git init`, to initialize it as a git repo. 

```
mkdir git_project
cd git_project
git init
touch Readme.md
code Readme.md
git status
git commit -a -m "add Readme.md"
```

### Clonning

We can clone a repo using three different ways: 

### HTTPS

```
git clone
```

### Commit 

When we want to commit code we can write git commit which will open up the commit edit message in the editor


### Git Config 

Is when it stores the global configurations for git such as email, username, editor, etc. 

```
git config --list
```

```
git config --global user.name 
git config --global user.email
```

### Log

```Git Log``` shows recent commits made in the git tree.

### Push

When we want to push our local repo to our remote origin or cloud based service (Github)

```git push```

