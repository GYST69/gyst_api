# How to run project locally:

- on your local enviroment install poetry:
> `pip install poetry`
- install dependencies:
> `poetry install`
- to run commands in virtual enviroment use `poetry run`:
> `poetry run python3 manage.py runserver`
- or you can run commands directly from shell:
> `poetry shell` 
- then: 
> `python3 manage.py runserver`
- to exit shell simply type:
> `exit`
---
- to add new dependency:
> `poetry add <some_package>`
- to remove dependency:
> `poetry remove <some_package>`