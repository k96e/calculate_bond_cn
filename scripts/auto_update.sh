#!/bin/bash

git fetch upstream
git checkout main
git merge upstream/main
git status
git checkout --ours blue_archive_gift.csv blue_archive_student_img_path.csv
git add blue_archive_gift.csv blue_archive_student_img_path.csv
git status
cd scripts
python translate_stu.py
cd ..
git add blue_archive_gift.csv blue_archive_student_img_path.csv
git commit -m "Auto update from upstream"
git push