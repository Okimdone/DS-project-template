git init
dvc init
git commit -m"initialize DS-project"

# Adding remote storage for DVC: changes are apllied to ".dvc/config'
dvc remote add -d dvc-remote /tmp/dvc-storage
git commit .dvc/config -m"configure remote storage"

