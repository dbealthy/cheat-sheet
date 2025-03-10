## Need to specify how to reconcile divergent branches
This means that was a commit on the local repository and the remote one from another device. Git doesn't know how to handle this situation

- `git config pull.ff only` - Set default behaviour to git in this repository to fast forward commits. It is best default options, because `rebase` and `merge` are too complex to be default for git, it is better to dicide myself what to do.


## Reset all changes and pull
	`git reset --hard HEAD`
	`git pull`


## Move not committed changes to a new branch


1. Stash changes without committing them 
   `git stash`
2. Create target branch
	`git checkout -b new_branch`
3. Apply changes in current branch
   `git stash apply`
4. Commit and push changes


## Squash commits
- Check branch history 
``` bash
git log --graph --oneline
```
- Run interactive `rebase` 
``` bash
git rebase -i <starting_commit_that_will_be_kept>^
```

- Commit editor will pop, i should choose which commits i want to **pick** (include) and which i want to **squash**. Replace `pick` on commits i want to squash with `squash` and close editor.

- Remove unnecessary messages from squashed commits and edit **picked** commits' messages

## Delete commits
source: https://mlops.systems/posts/2023-04-28-removing-git-commits.html

Everything is the same as `squash`-ing commits but instead of command `squash` we use `drop`


## Change base for a branch
source: https://stackoverflow.com/questions/10853935/change-branch-base
```
git rebase --onto newBase oldBase feature/branch
```