.PHONY: tests clean

init:
	pip3 install -r requirements.txt
	pip3 install --editable .

tests:
	nosetests3 tests

install:
	pip3 install .

clean:
	rm -rf build
	rm -rf boilerplate.egg-info
	rm -f boilerplate/*.so

