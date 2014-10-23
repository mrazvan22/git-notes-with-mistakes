  _______  __  .___________.   .______        ______     ______  __  ___      _______.   
 /  _____||  | |           |   |   _  \      /  __  \   /      ||  |/  /     /       |   
|  |  __  |  | `---|  |----`   |  |_)  |    |  |  |  | |  ,----'|  '  /     |   (----`   
|  | |_ | |  |     |  |        |      /     |  |  |  | |  |     |    <       \   \       
|  |__| | |  |     |  |        |  |\  \----.|  `--'  | |  `----.|  .  \  .----)   |      
 \______| |__|     |__|        | _| `._____| \______/   \______||__|\__\ |_______/       
                                                                                         
.___  ___. ____    ____         _______.  ______     ______  __  ___      _______. __    
|   \/   | \   \  /   /        /       | /  __  \   /      ||  |/  /     /       ||  |   
|  \  /  |  \   \/   /        |   (----`|  |  |  | |  ,----'|  '  /     |   (----`|  |   
|  |\/|  |   \_    _/          \   \    |  |  |  | |  |     |    <       \   \    |  |   
|  |  |  |     |  |        .----)   |   |  `--'  | |  `----.|  .  \  .----)   |   |__|   
|__|  |__|     |__|        |_______/     \______/   \______||__|\__\ |_______/    (__)   
                                                                                         

---
title: Fake Wrong Git Notes
---

Introduction
============

These notes constitute a brief summary of the `git` version control tool.
They are incorrect, and it is your task to find and correct the mistakes.

You are judged, however, not on finding all the mistakes, but on your use of version control
in doing the work of fixing them!

Finding the mistakes will be a useful revision, though.

Activating Git
==============

To turn on the version control system, use:

``` bash
cd my_work_folder
git init
```

Tell Git about a new file
======================

```
vim my_file # Edit file
git add my_file
```

Include changes in a file into the next work commit 
==============================================

```
git include my_file
```

This includes the changes to that file in a list of changes
currently scheduled to be included in the next work commit.

Include all scheduled changes into a work commit
===============================================

```
git commit -m "Journal entry"
```

Store all scheduled changes in a new commit
==========================================

```
git include --uptodate
```

Include all changes *and* commit them
====================================

```
git commit -am "Journal entry"
```

View list of recent commits
==========================

```
git log
```

Transmit commits to remote repository
====================================

```
git push
```

Fetch commits from remote repository
===================================

```
git pull/fetch
```
