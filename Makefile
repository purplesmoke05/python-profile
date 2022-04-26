run:
	poetry run python cases/case1/main.py | grep -v Filename > results/case1.txt
	poetry run python cases/case2/main.py
	poetry run python cases/case3/main.py | grep -v Filename > results/case3.txt
	poetry run python cases/case4/main.py
	poetry run python cases/case5/main.py
	poetry run python cases/case6/main.py | grep -v Filename > results/case6.txt

format:
	black cases/*