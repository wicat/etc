#!/bin/bash
# Script for creating new git projects.
# Created by Ekira
# 2017/02/18

if [ ! -n "$1" ] ; then
    echo "ERROR: need a gitrepo name, usage: newgit [gitrepo name]"
else
    gitrepo=/git/${1}
    if [ ! -d "$gitrepo" ] ; then
        git init --bare $gitrepo
        chown -R git:git $gitrepo
    else
        echo "ERROR: gitrepo existed, try another repo name."
    fi
fi
