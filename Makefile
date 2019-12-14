env:
	pipenv install
	pipenv shell
test:
	python manage.py test
dev_server:
	python manage.py migrate
	python manage.py loaddata user.json
	python manage.py runserver