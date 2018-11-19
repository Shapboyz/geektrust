
Solution for Set2Problem1

Installition
1) Create a virtual env with python 3.6
    If python3 is installed - python3.6 -m venv venv
2) Once done, activate the virtual env with
  . Set2Problem1/venv/bin/activate (Linux or)
  source Set2Problem1/venv/bin/activate (Mac and windows)

3) Once activated, change to projectdirectory and copy zipped file.
  Extract zip file and test current package as below
  <!-- (checks for python version, dependecies and tests) -->

  python setup.py test

4) Once, All test are ok. install with below command in same projectdirectory.

  pip install -e .

4) Now run, and it can be use in two ways
  (*) - By importing from terminal (like python package)
    - from Set2Problem1 import takeInput
    - takeInput.take_input(2)
  (*) - or from terminal as (like script)
    python Set2Problem1

Other important topic:-
1) Input :- "Falicornia attacks with 100 H, 101 E, 20 AT, 5 SG"
2) Output :- "Lengaburu deploys 75 H, 50 E, 10 AT, 5 SG and wins"
3) takes care of extra battlians

file structure:-
take_input.py - main file, needs to run with python.
war.py - takes care of all logic steps (creating instances and calculations)
region.py - handles code related to attack and defence regions
battlian.py - handles code related to battlian.

tests/
unit tests to check before running
