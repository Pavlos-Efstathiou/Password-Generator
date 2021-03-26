rm -rf dist/*
python3 setup.py sdist
/home/$(whoami)/.local/bin/twine upload dist/*

