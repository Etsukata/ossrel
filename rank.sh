#!/bin/sh

for file in ./repos/*
do
    repo=$(basename $file)
    echo $repo
    git --git-dir=$file/.git log --pretty=format:%an |
    sort | uniq -c | sort > ./ranking/$repo
done
