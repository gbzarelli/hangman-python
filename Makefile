install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

test_unit:
	. venv/bin/activate && pytest tests/

start:
	. venv/bin/activate && python app/app.py