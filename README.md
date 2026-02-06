## Scaffold

1. Create a Python Virtual Environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`.
2. Create empty files:`MakeFile`,`requirements.txt`,`main.py`,`Dockerfile`,`mylib/__init__.py`.
3. Populate `Makefile`.
4. Setup Continuous Integration, i.e check code for issues like lint errors.
5. Build cli using Python Fire library `./cli-fire.py --help` to test logic