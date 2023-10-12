PYTHON_INTERPRETER = ./.venv/bin/python

init:
	python -m venv .venv

clean:
	rm -r .venv

install:
	${PYTHON_INTERPRETER} -m pip install -r requirements.txt

test:
	${PYTHON_INTERPRETER} -m unittest


build-install:
	${PYTHON_INTERPRETER} -m pip install -r build_requirements.txt

build:
	${PYTHON_INTERPRETER} -m build	


clean-install:
	${PYTHON_INTERPRETER} -m pip install -I -r requirements.txt

dht22:
	${PYTHON_INTERPRETER} -m pizero_sensors.DHT22

pip-list:
	${PYTHON_INTERPRETER} -m pip list
