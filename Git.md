# Git, Github
Git - local opensourse software for version control
Github - website and echosistem, backend that is integrated with git.

### Git workflow
1. Go to project's direcotry
2. Repository inicialization  (create **.git** folder)
> **`git init`**
3. Get info about what is going on
> **`git status`**
4. Add files for git to track. If files were changed they need to be added again
> **`git add file.txt`** 
> **`git add .`** 
5. Fix all changes in project with commit
> **`git commit -m "Commit message"`**
6. To ignore some files and not include them in git repository. I create a file with name *.gitignore* and list all files that i want to be ignored.
	***.gitignore*** content
	>file1.txt
	>file2.py
	>/folder1

	After that add files to tracked
	> **`git add .gitignore`**

7. Commit .gitignore file
>**`git commit -m ".gitignore file added"`**

8. Show branches. Current branch is marked with * simbol (**master** branch by default)
> **`git branch`**
9. Another developer should not add changes to master branch, but create hist branch
> **`git branch newBranchName`**
10. Delete branch
> **`git branch -D branchName`** 
11. Switch to another branch
>**`git cheackout branchName`**
12. Create a new branch and switch to it
>**`git branch -b newBranchName`**
13. Merge/Join branches "myBranch" and "master" from master branch
>**`git merge myBranch`**


### Github workflow
1. Create new repository
2. Connect Git with Github
> **`git config --global user.name "MyUserName"`**
> **`git config --global user.email "MyEmail"`**
3. Connect local repository to remote one. Add remote repository and specify link from github
>**`git remote add origin https://github.com/dbealthy/MyRepositoryName.git`**
4. Push data to remote server
>**`git push -u origin master`**
5. To work on a project another developer should clone repository
>**`git clone https://github.com/dbealthy/MyRepositoryName.git`**
6. For main developer to get changes that another developer maid
>**`git pull`**