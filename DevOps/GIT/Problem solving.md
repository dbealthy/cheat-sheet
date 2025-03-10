## Need to specify how to reconcile divergent branches
This means that was a commit on the local repository and the remote one from another device. Git doesn't know how to handle this situation

- `git config pull.ff only` - Set default behaviour to git in this repository to fast forward commits. It is best default options, because `rebase` and `merge` are too complex to be default for git, it is better to dicide myself what to do.


## Reset all changes and pull
	`git reset --hard HEAD`
	`git pull`


## Move changes uncommited changes to a new branch


1. Stash changes without commiting them 
   `git stash`
2. Create target branch
	`git checkout -b new_branch`
3. Apply changes in current branch
   `git stash apply`
4. Commit and push changes