#!/bin/bash

pip freeze > requirements.txt
read -p "Commit description: " desc
git add . && \
git add -u && \
git commit -m "$desc" && \
git push heroku master
