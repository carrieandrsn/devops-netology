 karinaanderson$ git checkout git-rebase
Branch 'git-rebase' set up to track remote branch 'git-rebase' from 'origin'.
Switched to a new branch 'git-rebase'
 karinaanderson$ git rebase -i main
Auto-merging branching/rebase.sh
CONFLICT (content): Merge conflict in branching/rebase.sh
error: could not apply 6286052... git-rebase 1
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 6286052... git-rebase 1
 karinaanderson$ vi branching/rebase.sh
 karinaanderson$ git add branching/rebase.sh
 karinaanderson$ git rebase --continue
Auto-merging branching/rebase.sh
CONFLICT (content): Merge conflict in branching/rebase.sh
error: could not apply a04447a... git-rebase 2
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply a04447a... git-rebase 2
 karinaanderson$ vi branching/rebase.sh
 karinaanderson$ git add branching/rebase.sh
acBook-Air-karinaanderson:devops-netology karinaanderson$ git rebase --continue
[detached HEAD 4e4a433] Merge branch 'git-merge' into HEAD. Rebase test
 Date: Wed Aug 25 00:32:17 2021 +0500
Successfully rebased and updated refs/heads/git-rebase.
 karinaanderson$ git push -u origin git-rebase
To https://github.com/carrieandrsn/devops-netology
 ! [rejected]        git-rebase -> git-rebase (non-fast-forward)
error: failed to push some refs to 'https://github.com/carrieandrsn/devops-netology'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
 karinaanderson$ git push -u origin git-rebase -f
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 453 bytes | 226.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/carrieandrsn/devops-netology
 + a04447a...4e4a433 git-rebase -> git-rebase (forced update)
Branch 'git-rebase' set up to track remote branch 'git-rebase' from 'origin'.
 karinaanderson$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
 karinaanderson$ git merge git-rebase
Merge made by the 'recursive' strategy.
 branching/rebase.sh | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
 karinaanderson$ git push
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 236 bytes | 236.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/carrieandrsn/devops-netology
   be35789..df8e2a3  main -> main
