### Git Hidden Folder

There is a hidden folder called `.git` which tells you that our project is a git repo. 

To create it, we need to move to the folder and to run `git init`, to initialize it as a git repo. 

```
mkdir git_project
cd git_project
git init
touch Readme.md
open Readme.md
git status
git commit -a -m "add Readme.md"
```

### Clonning

We can clone a repo using three different ways: 

### HTTPS

```
git clone https://github.com/PeterBridges/Github-Exam.git
```

### Commit 

When we want to commit code we can write git commit which will open up the commit edit message in the editor. It represents additions, modifications and deletions of files. Each commit has a SHA hash. d4868abcc0c686147eddff7b2635e4920645858c

```
git commit -m "Add x changes"
git commit -a -m "Add x changes" 
git commit --amend
git checkout SHA
```

### Branch

Where we can make changes without affecting the entire project we're working on. We can have feature 1 branch, feature 2 branch , main branch and production branch, where we usually have the software releases. 
The process of creating, merging branches etc its called the github workflow. 

```
git branch
git branch -m [branch name]
git checkout [branch name]
git checkout -b [branch name]
git branch -d [branch name]
git branch -m [old name][new name]
```

### Remote 

```
git remote -v
git remote -add [name][url]
git remote remove [name]
git remote rename [old name][new name]
git push
git pull 
git fetch

### Git Config 

Is when it stores the global configurations for git such as email, username, editor, etc. 

Example of config file:
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = ...
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
	vscode-merge-base = origin/main
[branch "production]
    remote = origin
    merge = refs/heads/production
    vscode-merge-base = origin/production


### SSH keys

```
ssh-keygen -t rsa
```

A copy of the private and public key are held in your local computer and a copy of the public key is in github. Github sends a challenge message with the public key and it can only be decrypted with the private key. 


### Log

```Git Log``` shows recent commits made in the git tree.

### Push

When we want to push our local repo to our remote origin or cloud based service (Github)

```git push```

