all: develop

develop: proto
	protoc --proto_path=./proto/ --python_out=passer/proto proto/types.proto
	protoc --proto_path=./proto/ --python_out=passer/proto proto/service.proto
	python setup.py develop

test:
	tox

release:
	python setup.py sdist upload

clean:
	rm -rf passer.egg-info
	rm -rf passer/proto/*_pb*.py
	rm -rf dist/