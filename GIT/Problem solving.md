## Need to specify how to reconcile divergent branches
This means that was a commit on the local repository and the remote one from another device. Git doesn't know how to handle this situation

- `git config pull.ff only` - Set default behaviour to git in this repository to fast worward commits. It is best default options, because `rebase` and `merge` are too complex to be default for git, it is better to deside myself what to do.
- 
